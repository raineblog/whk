import sys
import os
import re
import hashlib
import time
from urllib.parse import urlparse
import httpx  # 需要 pip install httpx[http2] pyside6

from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QLineEdit, QPushButton, QLabel, QMessageBox, QFrame, QHBoxLayout)
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt, QMimeData, QUrl, QThread, Signal, Slot, QTimer

# --- 配置区域 ---
MAX_CLIPBOARD_LEN = 4096  # 超过这个长度的字符串不处理，节省性能
ALLOWED_EXTENSIONS = ('.svg', ) # 仅对这些后缀进行预加载，你可以加 '.png' 等

class PreloaderWorker(QThread):
    """
    后台下载线程：
    负责在检测到剪贴板变化后，静默下载内容到内存。
    """
    finished = Signal(str, bytes, str) # url, content, content_type
    error = Signal(str, str) # url, error_msg

    def __init__(self):
        super().__init__()
        self.target_url = None
        # 全局 Session，复用 TCP 连接，启用 HTTP/2
        self.client = httpx.Client(http2=True, follow_redirects=True, trust_env=True, timeout=10.0)
        self.client.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        })

    def preload(self, url):
        self.target_url = url
        self.start()

    def run(self):
        url = self.target_url
        if not url:
            return

        try:
            # 发起请求
            response = self.client.get(url)
            response.raise_for_status()
            
            content = response.content
            content_type = response.headers.get('content-type', '')
            
            # 发送成功信号
            self.finished.emit(url, content, content_type)

        except Exception as e:
            self.error.emit(url, str(e))

class SvgHelperApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SVG 极速助手 (预加载版)")
        self.resize(500, 650)
        
        # 状态变量
        self.current_url = ""      # 当前剪贴板的 URL
        self.cached_data = None    # 预加载成功的数据 (content, content_type)
        self.is_downloading = False 
        
        # 创建下载目录
        self.save_dir = os.path.join(os.getcwd(), "svg_downloads")
        os.makedirs(self.save_dir, exist_ok=True)

        # 初始化后台线程
        self.worker = PreloaderWorker()
        self.worker.finished.connect(self.on_preload_finished)
        self.worker.error.connect(self.on_preload_error)

        # 监听系统剪贴板
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.on_clipboard_change)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # 1. 状态指示灯
        self.status_bar = QLabel("等待复制...")
        self.status_bar.setStyleSheet("background-color: #ddd; padding: 5px; border-radius: 4px;")
        self.status_bar.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_bar)

        # 2. URL 显示
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("检测到的链接...")
        self.url_input.setReadOnly(True)
        layout.addWidget(self.url_input)

        # 3. 核心按钮
        self.btn_save = QPushButton("💾 保存并复制文件 (Pending)")
        self.btn_save.setMinimumHeight(50)
        self.btn_save.setEnabled(False) # 初始禁用，直到检测到链接
        self.btn_save.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.btn_save.clicked.connect(self.save_cached_file)
        layout.addWidget(self.btn_save)

        # 4. 预览区域
        self.svg_container = QFrame()
        self.svg_container.setFrameShape(QFrame.StyledPanel)
        self.svg_container.setStyleSheet("background-color: #f8f8f8; border: 1px solid #ccc;")
        svg_layout = QVBoxLayout(self.svg_container)
        self.svg_widget = QSvgWidget()
        svg_layout.addWidget(self.svg_widget)
        layout.addWidget(self.svg_container, stretch=1)

        self.setLayout(layout)

    def sanitize_filename(self, url, content_hash):
        """
        处理文件名：
        1. 解析 URL 获取原本文件名
        2. 正则过滤，只保留字母、数字、下划线
        3. 拼接 Hash 后7位
        """
        try:
            path = urlparse(url).path
            basename = os.path.basename(path)
            name_part, ext = os.path.splitext(basename)
            if not ext: ext = ".svg"
            
            # 正则：只保留 a-z, A-Z, 0-9, _
            clean_name = re.sub(r'[^a-zA-Z0-9_]', '', name_part)
            
            # 如果原文件名全是乱码被清空了，给个默认名
            if not clean_name:
                clean_name = "image"
            
            return f"{clean_name}_{content_hash}{ext}"
        except:
            return f"image_{content_hash}.svg"

    def on_clipboard_change(self):
        """
        剪贴板变化时的处理逻辑 (核心预加载逻辑)
        """
        # 防止自我触发：如果是我们自己写入的文件，跳过
        mime_data = self.clipboard.mimeData()
        if mime_data.hasUrls(): 
            return # 忽略文件复制，只处理文本

        if not mime_data.hasText():
            return

        text = mime_data.text().strip()
        
        # 1. 性能熔断：太长的不看 (防止复制整本小说时卡顿)
        if len(text) > MAX_CLIPBOARD_LEN:
            return

        # 2. 格式校验：必须是 http 开头
        if not text.startswith(("http://", "https://")):
            return

        # 3. 后缀校验：简单的预过滤，确保是目标类型
        # 为了更智能，可以忽略 ? 后面的参数再判断
        clean_url_for_check = text.split('?')[0].lower()
        if not clean_url_for_check.endswith(ALLOWED_EXTENSIONS):
            return

        # --- 通过校验，开始预加载 ---
        self.current_url = text
        self.url_input.setText(text)
        self.cached_data = None # 清空旧缓存
        
        self.status_bar.setText("⚡ 检测到链接，正在后台预加载...")
        self.status_bar.setStyleSheet("background-color: #fff3cd; color: #856404; padding: 5px;")
        
        self.btn_save.setText("⏳ 正在下载...")
        self.btn_save.setEnabled(True) # 允许点击（如果用户点击太快，会在 save 函数里等待）
        self.is_downloading = True
        
        # 启动线程下载
        self.worker.preload(text)

    @Slot(str, bytes, str)
    def on_preload_finished(self, url, content, content_type):
        """下载完成回调"""
        # 确保下载的还是当前剪贴板的链接 (防止用户快速连续复制)
        if url != self.current_url:
            return

        self.cached_data = (content, content_type)
        self.is_downloading = False
        
        self.status_bar.setText("✅ 预加载完成！点击下方按钮即可秒存。")
        self.status_bar.setStyleSheet("background-color: #d4edda; color: #155724; padding: 5px;")
        self.btn_save.setText("🚀 立即保存并复制文件")
        
        # 可选：下载完直接预览 (如果不希望预览抢占焦点，可以不加这行)
        # 临时保存一个预览文件用于渲染
        temp_preview = os.path.join(self.save_dir, ".preview_temp.svg")
        with open(temp_preview, 'wb') as f:
            f.write(content)
        self.svg_widget.load(temp_preview)

    @Slot(str, str)
    def on_preload_error(self, url, error_msg):
        if url != self.current_url:
            return
        self.is_downloading = False
        self.status_bar.setText(f"❌ 预加载失败: {error_msg}")
        self.status_bar.setStyleSheet("background-color: #f8d7da; color: #721c24; padding: 5px;")
        self.btn_save.setText("重试 / 失败")

    def save_cached_file(self):
        """用户点击按钮时触发"""
        if self.is_downloading:
            QMessageBox.information(self, "请稍候", "正在极速下载中，请稍等片刻...")
            return

        if not self.cached_data:
            QMessageBox.warning(self, "无数据", "没有可用的数据，请重新复制链接。")
            return

        content, _ = self.cached_data
        
        try:
            # 1. 计算 Hash
            file_hash = hashlib.sha256(content).hexdigest()[:7]
            
            # 2. 生成清洗后的文件名
            filename = self.sanitize_filename(self.current_url, file_hash)
            file_path = os.path.join(self.save_dir, filename)

            # 3. 写入硬盘
            with open(file_path, 'wb') as f:
                f.write(content)

            # 4. 复制文件到剪贴板
            self.copy_file_to_clipboard(file_path)

            self.status_bar.setText(f"🎉 已保存: {filename} | 文件已在剪贴板")
            self.status_bar.setStyleSheet("background-color: #cce5ff; color: #004085; padding: 5px;")
            
        except Exception as e:
            QMessageBox.critical(self, "保存失败", str(e))

    def copy_file_to_clipboard(self, file_path):
        """核心：将文件路径封装为文件对象放入剪贴板"""
        mime_data = QMimeData()
        url = QUrl.fromLocalFile(os.path.abspath(file_path))
        mime_data.setUrls([url])
        # 注意：这里修改剪贴板会触发 dataChanged，
        # 但我们在 on_clipboard_change 里加了 mime_data.hasUrls() 判断来避免死循环
        self.clipboard.setMimeData(mime_data)

    def closeEvent(self, event):
        self.worker.client.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SvgHelperApp()
    window.show()
    sys.exit(app.exec())
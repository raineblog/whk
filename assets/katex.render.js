const scriptSrc = document.currentScript ? document.currentScript.src : "";
const katexBase = scriptSrc.substring(0, scriptSrc.lastIndexOf("/") + 1);

const loadKaTeX = () => {
    if (window.__katexLoaded) return Promise.resolve();
    if (window.__katexLoading) return window.__katexLoading;

    window.__katexLoading = new Promise((resolve, reject) => {
        // Load CSS
        const link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = katexBase + "katex/katex.min.css";
        document.head.appendChild(link);

        // Load Scripts sequentially
        const scripts = [
            "katex/katex.min.js",
            "katex/contrib/mhchem.min.js",
            "katex/contrib/auto-render.min.js",
            "katex/contrib/copy-tex.min.js"
        ];

        const loadNext = (i) => {
            if (i >= scripts.length) {
                window.__katexLoaded = true;
                resolve();
                return;
            }
            const script = document.createElement("script");
            script.src = katexBase + scripts[i];
            script.onload = () => loadNext(i + 1);
            script.onerror = (e) => {
                console.error("Failed to load KaTeX asset:", scripts[i], e);
                reject(e);
            };
            document.head.appendChild(script);
        };
        loadNext(0);
    });
    return window.__katexLoading;
};

document$.subscribe(({ body }) => {
    loadKaTeX().then(() => {
        renderMathInElement(body, {
            delimiters: [
                { left: "$$", right: "$$", display: true },
                { left: "$", right: "$", display: false },
                { left: "\\(", right: "\\)", display: false },
                { left: "\\[", right: "\\]", display: true }
            ],
            macros: {
                // https://github.com/whk-wiki/whk-wiki/blob/main/config/macros.config.js
                "\\i": "\\mathrm{i}",
                "\\d": "\\mathrm{d}",
                "\\C": "\\mathbb{C}",
                "\\R": "\\mathbb{R}",
                "\\Q": "\\mathbb{Q}",
                "\\Z": "\\mathbb{Z}",
                "\\N": "\\mathbb{N}",
                "\\P": "\\mathbb{P}",
                "\\degree": "^\\circ",
                "\\op": "\\operatorname",
                "\\la": "\\left\\langle",
                "\\ra": "\\right\\rangle",
                "\\lc": "\\left\\lceil",
                "\\rc": "\\right\\rceil",
                "\\lf": "\\left\\lfloor",
                "\\rf": "\\right\\rfloor",
                "\\lv": "\\left\\lvert",
                "\\rv": "\\right\\rvert",
                "\\paren": "\\left({#1}\\right)",
                "\\bracket": "\\left[{#1}\\right]",
                "\\brace": "\\left\\{{#1}\\right\\}",
                "\\ceil": "\\left\\lceil{#1}\\right\\rceil",
                "\\floor": "\\left\\lfloor{#1}\\right\\rfloor",
                "\\vert": "\\left\\lvert{#1}\\right\\rvert",
                "\\vec": "\\bm",
                "\\vecc": "\\overrightarrow",
                "\\mol": "\\operatorname{mol}",
                "\\thermo": "\\ce{#1};\\quad\\Delta H=\\pu{#2}",
                "\\cat": "\\ce{催化剂}",
                "\\heat": "\\triangle",
                "\\poly": "\\ce{-\\!\\!\\![ #1 ]_n\\!\\!\\!\\!\\!-}",
                "\\el": "#1\\mathrm{#2}^{#3}",
                "’": "'",
                "，": ",",
                "。": ".",
                "；": ";",
                "：": ":",
                "！": "!",
                "？": "?",
                "【": "[",
                "】": "]",
                "（": "(",
                "）": ")",
                "、": ",",
                "—": "-",
                "…": "\\dots",
                "·": "\\cdot",
                "\\pH": "p\\ce{H}",
                "\\pOH": "p\\ce{OH}",
                "\\con": "\\left[\\ce{#1}\\right]",
                "\\rank": "\\operatorname{rank}",
                "\\trans": "^{\\mathrm{T}}",
                "\\sgn": "\\operatorname{sgn}",
                "\\environment": "\\begin{#1} #2 \\end{#1}",
                "\\matrix": "\\begin{matrix} #1 \\end{matrix}",
                "\\pmatrix": "\\begin{pmatrix} #1 \\end{pmatrix}",
                "\\bmatrix": "\\begin{bmatrix} #1 \\end{bmatrix}",
                "\\Bmatrix": "\\begin{Bmatrix} #1 \\end{Bmatrix}",
                "\\vmatrix": "\\begin{vmatrix} #1 \\end{vmatrix}",
                "\\Vmatrix": "\\begin{Vmatrix} #1 \\end{Vmatrix}"
            },
            trust: true,
        });
    }).catch(err => {
        console.error("KaTeX rendering failed due to asset loading error:", err);
    });
});
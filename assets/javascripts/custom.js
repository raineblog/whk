function m_error() {
	document.getElementsByClassName('edit_history')[0].setAttribute('href', '{{ config.repo_url }}');
	document.getElementsByClassName('facts_modified')[0].innerHTML = ('最近没更新过这个页面');
	document.getElementsByClassName('page_contributors')[0].innerHTML = ('本页面是自动生成的');
	document.getElementsByClassName('page_edit_url')[0].setAttribute('href', '#');
}

function foo(response) {
	var data = response.data;
	var num = response.data.length;
	if (data && data[0]) {
		var t = new Date(data[0].commit.author.date);
		var ti = t.toLocaleDateString('zh-CN', { timeZone: "Asia/Shanghai", hour12: false }) + " " + t.toLocaleTimeString('zh-CN', { timeZone: "Asia/Shanghai", hour12: false });

		var author_list = document.getElementsByClassName('page_contributors')[0].innerHTML.split(', ');
		author_list = author_list.filter((e) => { return e != 'AFOI-wiki' })
		for (var i = 0; i < num; ++i) {
			author_list.push(data[i].author.login);
		}

		var cnts = author_list.reduce(function (obj, val) {
			obj[val] = (obj[val] || 0) + 1;
			return obj;
		}, {});
		//Use the keys of the object to get all the values of the array
		//and sort those keys by their counts
		var sorted = Object.keys(cnts).sort(function (a, b) {
			return cnts[b] - cnts[a];
		});
		var index = sorted.indexOf('24OI-bot');
		if (index > -1) {
			sorted.splice(index, 1);
		}
		sorted = sorted.map(function (x) {
			return `<a href=https://github.com/${x}>${x}</a>`
		})
		document.getElementsByClassName('facts_modified')[0].innerHTML = (ti);
		document.getElementsByClassName('page_contributors')[0].innerHTML = (sorted.join(', '));
	} else m_error();
}

function m_get_info(site_author) {
	var cur = document.getElementsByClassName('page-time')[0];
	if (cur) {
		var comments = document.getElementById('gitment_container');
		var pos = 0;
		if (comments) {
			pos -= comments.textContent.length;
		}
		comments = document.getElementById('__comments');
		if (comments) {
			pos -= comments.textContent.length;
		}
		var textLength = 0;
		if (pos < 0) textLength = (document.getElementsByClassName('md-content__inner')[0].textContent.slice(0, pos).replace(/\s/g, '').length - document.getElementsByTagName('h1')[0].textContent.replace(/\s/g, '').length - document.getElementsByClassName('page-copyright')[0].textContent.replace(/\s/g, '').length - 4);
		else textLength = (document.getElementsByClassName('md-content__inner')[0].textContent.replace(/\s/g, '').length - document.getElementsByTagName('h1')[0].textContent.replace(/\s/g, '').length - document.getElementsByClassName('page-copyright')[0].textContent.replace(/\s/g, '').length - 4);
		if (textLength <= 0) cur.innerHTML = '<p>本页面还在建设中，欢迎参与完善！</p>';
	}

	document.getElementsByTagName("html")[0].lang = "zh-Hans"; // change language to 'zh-Hans' for Han.js.

	// var url = document.getElementsByClassName('page_edit_url')[0].href.split('?ref=')[1];
	var url = document.getElementsByClassName('page_edit_url')[0].href.split('docs')[1];
	var sub = document.getElementsByClassName('page_edit_url')[0].href.split(site_author + '/')[1].split('/edit')[0];
	// var url = document.URL.replace(/http\S+\.org\//gi, '').replace(/#\S+$/gi, '').slice(0, -1);
	var script = document.createElement('script');

	console.log(url);
	console.log(sub);

	if (typeof (url) != 'undefined') {
		console.log("WOW1");
		document.getElementsByClassName('edit_history')[0].setAttribute('href', 'https://github.com/' + site_author + '/' + sub + `/commits/main/docs${url}`);
		script.src = 'https://api.github.com/repos/' + site_author + '/' + sub + `/commits?path=docs${url}&callback=foo`;
		console.log(script.src);
		document.getElementsByTagName('head')[0].appendChild(script);
	} else {
		console.log("ERROR1");
		m_error();
	}
}

document$.subscribe(({ body }) => {
	hljs.highlightAll();
	console.log("subscribe");
	$(function () {
		$(window).scroll(function () {
			if ($(this).scrollTop() > 200) { $('#scroll-page-top, #scroll-page-top-new').fadeIn(); }
			else { $('#scroll-page-top, #scroll-page-top-new').fadeOut(); }
		}); $('#scroll-page-top, #scroll-page-top-new').click(function () { $('html,body').animate({ scrollTop: 0 }, 500); return false; });
		$('#scroll-page-top, #scroll-page-top-new').hover(function () {
			$(this).animate({ 'opacity': '1' }).css({ 'background-color': '#e7ebf0', 'color': '#6a86a4' });
		}, function () {
			$(this).animate({ 'opacity': '0.7' }).css({ 'background': '#AAA', 'color': '#FFF' });;
		});
	});
	renderMathInElement(body, {
		delimiters: [
			{ left: "$$", right: "$$", display: true },
			{ left: "$", right: "$", display: false },
			{ left: "\\(", right: "\\)", display: false },
			{ left: "\\[", right: "\\]", display: true }
		],
	});
});

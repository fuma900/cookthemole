chrome.extension.sendMessage({}, function(response) {
	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {
		clearInterval(readyStateCheckInterval);

		// ----------------------------------------------------------
		// 					!!! SITE SPECIFIC !!!
		// ----------------------------------------------------------

		var instr = [];
		var b = [];
		var a = $("span.plaincharacterwrap");
		for (i=0; i<a.length; i++) {
			b[i] = a[i].innerText;
		}

		// ----------------------------------------------------------
		// 					!!! GENERAL !!!
		// ----------------------------------------------------------

		instr = b.join('').split('.');
		$.each(instr, function(k,v){
			instr[k] = $.trim(v);
		});

		chrome.runtime.sendMessage({method:'instr', data:instr});

		console.log(instr);

	}
	}, 10);
});
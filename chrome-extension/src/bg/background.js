// if you checked "fancy-settings" in extensionizr.com, uncomment this lines

// var settings = new Store("settings", {
//     "sample_setting": "This is how you use Store.js to remember values"
// });


//example of using a message handler from the inject scripts
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
  	chrome.pageAction.show(sender.tab.id);
    sendResponse();
  });

chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
		if (request.method == 'instr'){
			console.log(request.data);
			data = request.data;
			jQuery.each(data, function(k,v){
				chrome.tts.speak(v, {'enqueue': true, 'rate': 0.9, 'pitch':0.8});
				console.log(k+": "+v);
			});
		}
	});
/*
function showPageAction(tabId, changeInfo, tab){
	chrome.tabs.getSelected(null, function(tab) {
		url = tab.url;
	    var matches = url.match(/^https?\:\/\/([^\/:?#]+)(?:[\/:?#]|$)/i);
		var domain = matches && matches[1];  // domain will be null if no match is found
		console.log(domain);
		console.log(url);
		if(domain == 'allrecipes.com'){chrome.pageAction.show(tab.id)};
	});
}

chrome.tabs.onUpdated.addListener(showPageAction);
*/
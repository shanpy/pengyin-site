.. title: Use Google Custom Search In Your Website
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Web Development Tips
.. tags: Web Developement Tips, Google
.. slug: use-google-custom-search-in-your-website
.. authors: Pengyin Shan
.. description: Use Google Custom Search In Your Website

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

You need a google account to use Google Custom Search Engine. Go to "www.google.com/cse" and sign in with your Google account.
images/posts/google_cse.PNG 

In the console, click "New search engine" on left menu, then input the website url you want to search from. You also need a name for this new search engine. After finsih setup, click "CREATE" button.
images/posts/google_cse_create.PNG 

You need to use `Search Engine ID` for creating RESTful service. To do this, select "Edit search engine" on left menu. In the dropdown, select your search engine. Select "Basics" panel on right, then click "Search engine ID" in details part. A pop up box will appears with your Search Engine ID.
images/posts/google_cse_id.PNG 

You also need your api key for creating RESTful service. To do this, you need a project and get its API key in *Google Developers Console*. You can do this by log in "console.developers.google.com" and select "Credentials" in "APIs & auth" menu. You will see API key appearing on right panel.

Then go back to your Custom Search panel. In "Details" part on right, click "Get Code" button (just near "Search Engine ID" button). Copy the code on this page and paste it into a '<div>' where you want the Google search bar appears.

You may want to use RESTful api to get results from Google custom search engine. The format of requested url is: `https://www.googleapis.com/customsearch/v1?key=XXX&cx=XXX&q=XXX`. You should put your API key as `key` parameter, your search engine Id as `cx` paramter, and the string your want to search as `q` parameter.

You can also add query parameters at the end of request url, such as `&callback=` for returning `JSON-P` object. Please refer to "https://developers.google.com/custom-search/json-api/v1/using_rest" if you need

Here is an example using AngularJS:

	:::javascript
	//We want to search "javascript" using Custom Search Engine
	var url = 'https://www.googleapis.com/customsearch/v1?key=XXX&cx=XXX&q=javascript&callback=JSON_CALLBACK';
		   	$http.jsonp(url).success(function(data, status, headers, config){
		   		for (var i = 0; i < data.items.length; i++) {
		   	        var item = data.items[i];
		   	        document.getElementById("callback").innerHTML += "<br/>" + item.htmlTitle;
		   	        //This will return all searchign result's title
		   	      }
		   	})
		   .error(function (data, status, headers, config) {
		   		window.console.log("error: " + data + " status: " + status + " headers: " + headers + " config: " + config);
		    });
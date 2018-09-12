.. title: Possible Ajax Error Code and Reasons
.. date: 2015-08-13
.. modified: 2015-09-29
.. category: JavaScript
.. tags: Java, Ajax, jQuery, JSON, Spring MVC
.. slug: possible-ajax-error-code-and-reasons
.. authors: Pengyin Shan
.. description: This post records all error codes (400,401...) from jQuery Ajax call to Java/Spring MVC, with possible reasons of these codes.

##400 (Bad Request)

- In jQuery, no `JSON.stringify()` is used to parse JavaScript object to JSON object

- Use `$.ajax()` but doesn't include `type: "GET/POST/etc"` in AJAX body

##406 (Not Acceptable Response)

- Check your authority setting. One of my Spring MVC project has requirement:  user group 1 can only access sub-URL of `/test/user1`. So if I make a URL mapping to `/test/`, AJAX call will fail and give me a `406` error

##404 (Not Found Errors)

Very common error. Can have different reasons:

- `dataType`, `contentType`, `mimeType` may not corresponding to correct type.

- In Spring MVC, no `@ResponseBody` or `@RequestBody` is added in controller. For example: `public @ResponseBody String test(@RequestBody final String id)` is good. But `public String test(@RequestBody final String id)` can generate a 404 error in client side.

##No response (Back-end finsih processing but front-end give no response)

- Check your jQuery version and check if you are using `$.ajax({done: function(data../){}, fail: function(jqXHR...){}});`. If so, try to check your jQuery to later version, or replace with `$.ajax({success: function(data...){}, error: function(jqXHR...) })`
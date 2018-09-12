.. title: Ajax and Spring MVC Controller
.. date: 2015-01-13
.. modified: 2015-05-29
.. category: Java
.. tags: Java, Spring, Ajax, jQuery
.. slug: ajax-and-spring-mvc-controller
.. authors: Pengyin Shan
.. description: This post includes my experience when working with AJAX and JSON, using jQuery with Spring MVC Framework.

Note
>Before you through two cases below, make sure you check your **web.xml** and get the `<url-pattern>`:
>- If your web.xml set up default url-pattern `/`, when you refer a link, you don't need to add any suffix on it.
>- If your web.xml set up any url-pattern, such as `html` or `htm`, when you refere a link, in `ajax` or `windown.location.href`, you need to add `html` or `htm` suffix after it. *But don't add these suffix in spring controller request mapping*.

Case 1. Pass JSON Data to Controller in Ajax Call, using $.ajax()
-----------------------------------------------------------------

>Notes on 01/13/2015: I had trouble using `$.post()` to post JSON data. I doubt something is wrong but I haven't figure out why. Currently I just use `$.ajax()`*

PROS
>Ajax is good for **large dataset**, so you can avoid possible "timeout" problem in case 2.

>Ajax has **success** and **error** option, so you can check status of ajax call, and give response based on feedback.

CONS
>You need to come back this page after an ajax call!**, no matter you success or fail.

So, if you want to go to another page, you need to use another `window.href` or other functions to call another controller, then follow that controller to go to another page.

Process of using Ajax:

    :::javascript

    //Assume we have a json object 'json'
    $.ajax({
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        }
    });


TIP
>You may want to substitude `application/json` with `application/html` to avoid possible.

Case 2. Pass JSON Data as URL parameter, and Handle it in Spring MVC Controller
-------------------------------------------------------------------------------

PROS
>You are free to go to another page or call other controllers after you pass data to controller.

CONS
>Not good to handle large dataset. If you put too much stuff in URL, you may get "time out" problem.

One of the easiest way to handle json object is to pass it directly to URL. I tried following methods:
>1. Pass data as pure json object, and make it as part of URL
>2. Pass data as pure jsob object, and make it as a parameter in URL
>3. Pass data as a string, and make it as part of URL
>4. Pass data as a astring, and make it as a parameter in URL

Assume the code for JSON object in JavaScript is:

    :::javascript

    var json = [];
    var obj = {};
    obj.age = 5;
    obj.name = "test";
    json.push(obj);


So the code for JSP page can be:

    :::javascript

    var testUrl = "/project/json_operation/" + json;
    window.location.href = testUrl;

    var testUrl = "/project/json_operation?json=" + json;
    window.location.href = testUrl;

    var testUrl = "/project/json_operation/" + JSON.stringify(json);
    window.location.href = testUrl;

    var testUrl = "/project/json_operation?json=" + JSON.stringify(json);
    window.location.hre = testUrl;


And the code for Spring Controller can be:

    :::java

    /*
    *1 and 3: not work.
    *For 1: Spring will recognize json as [object%20Object] in url
    *For 1 and 3: Spring cannot find
    */
    @RequestMapping(value="/springtest/{jsonstuff}")
    public ModelAndView test(@PathVariable("jsonstuff") JSONObject json){
    //Or @PathVaraible("jsonstuff") String json
    }
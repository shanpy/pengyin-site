.. title: Ajax and Java Servlet
.. date: 2015-08-03
.. modified: 2015-08-13
.. category: Java
.. tags: Java, Ajax, jQuery, Servlet
.. slug: ajax-and-java-servlet
.. authors: Pengyin Shan
.. description: This post describe the way to using AJAX with JSP/Servlet Java Web Apps.

I was working on an old Java web application today. This java web app used to pass data by using URL parameter, and I wanted to change it to passing data by using AJAX with JSON object, since there will be more data being passed in the future.

After working a while I realized I need to write this post becasue:

1. Pure JSP/Servlet java app is a little bit different from Spring MVC Java web app

2. I'm digging into Spring MVS so much that it's a little bit tough to change back to old way :)

So, if you have a JSP/Servlet Java web app and you want to use AJAX with JSON object, you have to write code in three places:

###1. JSP with jQuery

You want to have `jQuery` library in your JSP file to make sure you can use AJAX.

    :::javascript
    $.ajax({
            type: "POST",
            url: 'your <url-pattern> in web.xml'
            data: JSON.stringify(json_object),
            contentType: 'application/json',
            dataType: 'json',
            //mimeType: 'application/json'
            success: function(data){
                //Process your data that is being passed back...
            },
            error: function(jqXHR, textStatus, errorThrown ){
                //Deal with error occation
            }
            });
    //New Version:
     $.ajax({
            type: "POST",
            url: 'your <url-pattern> in web.xml'
            data: JSON.stringify(json_object),
            contentType: 'application/json',
            dataType: 'json'
            }).done(function(data){
                //Process your data that is being passed back...
            }).fail(fuction(){
                //Deal with error occation
            }).always(function(){
                //Same as 'complete' in old version, operate after done/fail
            });
    //You can also use $.post(url, data, success, dataType) as a new way

>In the code above, `contentType` and `dataType` (and `mimeType` if exists) is very important because wrong value of these attributes can give you a `404` or `500` error.

####contentType

Default value: `application/x-www-form-urlencoded; charset=UTF-8`

This is the data type **when you send data to server**.

####dataType

Default value: Guess(`xml`, `json`, `script`, `html`)

This is the data type **when server pass data back to you**.

####mimeType

A mime type to override the XHR mime type. This is the data type **when server pass data back to you**.

Form Mozilla, MIME types describe the media type of content either in email or served by web servers or web applications.

MIME types are intended to help guide a web browser in *how the content is to be processed and displayed*. Examples of MIME types are:

- `text/html` for normal web pages
- `text/plain` for plain text
- `application/octet-stream` meaning "download this file"
- `application/x-java-applet` for Java™ applets
- `application/pdf` for Adobe® PDF documents.

So if you want you browser to access data like `xml`, `json`, `script` or `html`, `dataType` is good enough. However, if you want to let your browser detect PDF file or other data types, you need to set `mimeType`.

###2. web.xml

>After working with Spring MVC for a while, I realizae I can forget web.xml easily. Make sure you register your servlet in web.xml.

You need to regiseter your servlet in `web.xml` file in your project. Example:

    :::xml
    <servlet>
        <!-- Give a servlet name for using in web.xml -->
        <servlet-name>proctorprocess</servlet-name>
        <!-- This is the class of your servlet -->
        <servlet-class>edu.fsu.odl.cat.cber2.ProctorProcessServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <!-- Same servlet name as above -->
        <servlet-name>proctorprocess</servlet-name>
        <!-- This is the url you want to put as url -->
        <url-pattern>/ProctorProcess</url-pattern>
    </servlet-mapping>

###3. Servlet

If you pass JSON object to your servlet, you may want to use `org.json`, `com.fasterxml.jackson` or `gson` external library to help you dealing with JSON object in Java.

Example code for post operation:

    :::java
    //You want your class extends HttpServlet
    public class ProctorProcessServlet extends HttpServlet{
        protected void doPost(HttpServletRequest request, HttpServletResponse response){
            try{
                String json = "";
                BufferedReader br = new BufferedReader(new InputStreamReader(request.getInputStream()));
                if(br != null){
                    json = br.readLine(); //json should be the string of your JSON object
                    //Process your JSON object
                }
                //Assume you want to pass JSON object back
                response.setContentType("application/json");
                PrintWriter out = response.getWriter();
                JSONObject sample = new JSONObject();
                //Process sample
                 out.print(sample);
                 out.flush();
                 //Now you finish your post operation and come back to JSP
            }
            catch(Exception e){
                //...
            }
        }

This post will be udpated when I learned more about AJAX in my work experience.

###Tips

####org.apache.catalina.LifecycleException: Failed to start component

If you include `org.json` jar file in your project, and you encourter `org.apache.catalina.LifecycleException: Failed to start component` exception when you try to deploy to Tomcat:

Make sure you add your jar files to `Web Deployment Assebly` in your project properies. Following <a href="http://stackoverflow.com/questions/16362302/java-servlet-error-with-jsonobject">this post</a> and you will be fine.
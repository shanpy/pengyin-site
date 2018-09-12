.. title: RequestDispacher and Redirection in Java Web App
.. date: 2015-08-05
.. category: Java
.. tags: Java, Ajax, Servlet
.. slug: requestdispacher-redirection-in-java
.. authors: Pengyin Shan
.. description: This post describe the way to using RequestDispacher and redirect in Java Web App.

This post only talks about `RequestDispacher` in Java web app. If you want to know more about using servlet in Java, I have another related post: <a href="http://pengyin-shan.com/blog/ajax-and-java-servlet">Ajax and Java Servlet</a>.

###Dispach

This <a href="http://www.xyzws.com/servletfaq/what-is-the-defferent-between-getnameddispatcher-and-getrequestdispatcher/3">article</a> from www.xyzws.com is very useful.

`RequestDispacher` is used to formard a client's request to another 'place', which including another servlet, another JSP, etc.

In a servlet, there are three ways to get RequestDispacher:

####RequestDispatcher dispatch = request.getRequestDispatcher(path);

Using this, *path* can be:

- either a path related to your current request, such as `subhome.html`

- or a servlet name in your `web.xml` file

- or a abosute path related to your current contaxt, such as `/subpage/subjome.jsp`


####RequestDispatcher dispatch = getServletContext.getRequestDispatcher(path)

Using this, *path* **must** start with `/`, such as `/subpage/subjome.jsp`

####RequestDispatcher dispatch = getServletContext.getNamedDispatcher("string")

This method must take the servlet name as its parameter. The servlet name is definded in `web.xml` as  <servlet-name> sub-element of the <servlet> element. The request is dispatched to that corresponding servlet.

Example in `web.xml`:

	:::xml
	<servlet>
		<!-- Use testProctor for getting RequestDispatcher -->
        <servlet-name>testProctor</servlet-name>
        <servlet-class>com.test.proctortest</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>testProctor</servlet-name>
        <url-pattern>/test_proctor</url-pattern>
    </servlet-mapping>

Before/After get your RequestDispacher, you can use `request.addAttribute(something)` or other functions to add stuff to your request.

###Go to another place

After you finish process HttpRequest or HttpResponse, there are three ways to 'leave' for another place:

####RequestDispatcher.forward(request, response) | RequestDispatcher.include(request, response)

There is a greate <a href="http://way2java.com/servlets/difference-between-include-and-forward-in-requestdispatcher/">article</a> from way2java.com to explain the difference between `RequestDispatcher.forward()` and `RequestDispatcher.include()`.

These are main differences bewtween these two methods:

- `include()` will **include** another file in your current file, the send back to client. This is like `<include /footer.jsp/>` but on server side. `forward()` will **forward** the client to another page/servlet.

- `include()` will return back to original servlet, but `forward()` will go directly to client.

- So, if you need response from *two* servlet, use `include()`. If you only need reponse from last servlet, use `forward()`. *Note include() does have limitation for second servlet accessing information from first servlet*.

- `include()` will give client the response from the **same** servlet which he requested. `forward()` will give client the response from a different servlet.

- Generally, you want to use `include()` when **static** information needs to be included, such as Banner Content or Copyright Information. `forward()` should be used to include **dynamic** information, or when you want to use servlet as a Controller.

####HttpResponse.sendRedirect(String)

The differnce between `forward()/include()` and `HttpResponse.sendRedirect()` is very obvious:

- `SendRedirect` is just for re-direction. If you have any data, it has to be transferred by **session** or being included in **URL**. This request is **visible** in browser as a new request. i.e. it is a **client side redirect**.

- `forward()/include()` is server side operation, which is not visible to browser. You can use `request.getAttribute()` to get data.
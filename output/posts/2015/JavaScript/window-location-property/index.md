.. title: Window.Location Property
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: JavaScript
.. tags: JavaScript
.. slug: window-location-property
.. authors: Pengyin Shan
.. description: This post introduces some common properties of **window.location**, based on introduction pages on <a href="https://developer.mozilla.org/en-US/docs/Web/API/window.location">MDN</a> and <a href="http://www.w3schools.com/jsref/obj_location.asp">w3schools</a>.



**window.location** is a **read-only** property, but you can also sign a string to it. It has some commenly used properties:

##location.hash

You can add **anchor** to URL, using a **#** character. For example: `www.example.com/blog.html#blog_1`.

Use the example above, `window.console.log(location.hash) => #blog_1`. Returned value include **#**.

When you set a hash, do not include **#**.

##location.href

Return entire URL. When you assign it, you can assign whole URL, relative URL, anchor only or protocal, based on your need. Following examples all work well:
`location.href="#blog_1"`
`location.href="mailto:abc@example.com"`
`location.href="test.html"`
`location.href=ftp//test.com`

##location.origin

*Not supported by IE*

Return protolcol.hostname and port number of a URL. An example is `httpw://www.example.com:1112`

*Note* If the port number is not specified in URL, some browsers will not display port number.

This is a **read-only** property, so you can not set it.

##location.host

You can use this property to get/set **hostname** and **port** of URL. Normally should return "www.xyz.com".

*Note*: If the port number is not specified in URL, some browsers will not display port number.

You can use `location.host = "hostname:port"` to set host.

**location.hostname** **location.port** **location.protocal**

Similar as above, these properties returns hostname/port/protocal of URL. Normally should return "www.xyz.com".

You can do get/set for all of these properties.

If a port is not specified in URL or is scheme's default port,such as `80` or `443`,some browser return 0 or nothing.

##location.pathname

Return **directoy path** of a URL. For example: `/WEB-INF/Views/Test.jsp

You can do get/set for this property.

##location.search

Return the **querying string** part of a URL, which is normally the part **?** and string after it in URL.

You can do get/set for it. For example, a possible result can be `?id=111`.

##location.assign(URL)

Load a new document.

##location.replace(URL)

Same as `location.assign()`, but **you cannot use "back" button to go back to previous page**.

You can combine it with **hash**. For example: `location.replace("http://www.example.com/#" + location.pathname)`

##location.reload()

Same as the "reload" button in browser, reloading current document.

Use `location.reload(true)` to force reloading document.
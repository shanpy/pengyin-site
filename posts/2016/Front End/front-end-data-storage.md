.. title: Frond End Data Storage
.. date: 2016-08-16
.. category: Front End
.. tags: HTML5, JavaScript
.. slug: front-end-data-storage
.. authors: Pengyin Shan
.. description: One of my recent project involving in front-end data storage and processing. This is a study note of current ways of data storage in client side.



#Reference List

- <a href="http://www.w3schools.com/html/html5_webstorage.asp">HTML Local Storage</a> from *w3schools.com*

- <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage">Window.localStorage</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage">Window.sessionStorage</a> from MDN

- <a href="http://www.tutorialspoint.com/javascript/javascript_cookies.htm">JavaScript and Cookies</a> from *Tutorialspoint.com*

- <a href="http://www.tutorialspoint.com/html5/html5_web_storage.htm">HTML5 - Web Storage</a> from *Tutorialspoint.com*

#Cookie

Cookie is the most efficient method of remembering and tracking small amount of information in client side.

#Web Storage

Web storage is for large amount of data.

So far, Web storage is widely supported by most browsers, from IE8 to most of mobile browser(except Opera Mini). So when I needs to store a large amount of data with capability requirement for most browsers, this is currently my best choice.

There are two parts of web storage: **local storage** and **session storage**.

Data for web storage are passed by `key-value` pair.

##Local Storage

Compared to session storage, local storage has **no expiration time**.

###Usage

`localStorage` object can be used directly. Like `window.localStorage`.

To remove a key-value pair, use `remove('key')`, like `localStorage.remove('lastname')`.

to clear all key-value pair, use `localStorage.clear()`.

####`getItem` and `setItem`

`getItem('key','value') and setItem('key','value')` is used to get/set data item.

Here is an example from W3CSchool:

    :::javascript
    // Store
    localStorage.setItem("lastname", "Smith");
    // Retrieve
    document.getElementById("result").innerHTML = localStorage.getItem("lastname");

####Use direct attribute

Another way is to assign attribute to `localStorage` object:

    :::javascript
    // Store
    localStorage.lastname = "Smith";
    // Retrieve
    document.getElementById("result").innerHTML = localStorage.lastname;

##Session Storage

Following a difference between local storage and session storage:

- For session storage, data are lost after **session end**. i.e. data are delete after use close a browser window/tab.

- For session storage, opening a page in *new tab or window* will cause a new session to be **initiated**.

###Usage

The way to use session storage is the same as the way to use local storage, except the object is now `window.sessionStorage`.

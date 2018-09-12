.. title: Collection of Tips for Creating/Controlling Dropdown on Web Page
.. date: 2015-06-04
.. category: JavaScript
.. tags: JavaScript, CSS, HTML5, jQuery, Bootstrap3, Dropdown
.. slug: create-controll-dropdown
.. authors: Pengyin Shan
.. description:  This post records all the ways I found online and tested in my job for creating/controlling dropdowns in web page. I'll update this post when I find more useful tips.



In my job, I always counter problem of creating dropdowns for web development project. Sometimes I can use Bootstrap, jQuery. Sometimes I have to use pure JavaScript. I also need to perform control options to dropdowns ocationally.

I want to write this post to record all ways and tips for creating dropdown, for future reference.

Pure JavaScript
===============

Simpliest Dropdown Option
---------------------------

The simplest dropdown is just created by `<select>` and `<option>` tag. Usually you wrap a few `<option>` blocks in a `<select>` block.

For each `<option>`, You can assign `value` attribute to it. There are other attributes such as `selected` or `label`.

For `<select>`, you can also set attributes such as `size` or `name`.

>`autofocus`, `form` and `required` are attributes for HTML5. Please check browser support setting before use them.

Example from W3Schools:

    :::html
    <select>
        <option value="1">A</option>
        <option value="2">B</option>
        <option value="3">C</option>
    </select>


Dropdown Menu (One or Multiple Level)
-------------------------------------

I found this <a href="http://javascript-array.com/scripts/simple_drop_down_menu/#">post</a> and this <a href="http://javascript-array.com/scripts/multi_level_drop_down_menu/?st">post</a> from <a href="http://javascript-array.com/">JavaScript Array</a> website are very classical. I've tested them and I highly recommend using them for pure dropdown menu.

###Single Level

I have read through the code. Here are my explanations. You are free to add font or hover effects in real world.

HTML Structure:

    :::html
    <!--Container of Many First Level Menus-->
    <ul>
        <li>
            <!--First Level Menu 1 -->
            <a href="#" onmouseover="mopen('m1')" onmouseout="mclosetime()">First Level Menu 1</a>

            <!--Links of First Level Menu 1 -->
            <div id="m1" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
                <a href='#'>Link1</a>
                <a href='#'>Link1</a>
            </div>
        </li>

        <li>
            <!--First Level Menu 2 -->
            <a href="#" onmouseover="mopen('m2')" onmouseout="mclosetime()">First Level Menu 2</a>

            <!--Links of First Level Menu 2 -->
            <div id="m2" onmouseover="mcancelclosetime()" onmouseout="mclosetime()">
                <a href='#'>Link2</a>
                <a href='#'>Link2</a>
            </div>
        </li>
    </ul>

CSS Structure (You may need to some tags to id in real world):

    :::css
    /* Outside Container */
    ul
    {   margin: 0;
        padding: 0;
        z-index: 30
    }

    ul li
    {   margin: 0;
        padding: 0;
        list-style: none;
        float: left;
    }

    /* First Leval Menu */
    ul li a
    {   display: block;
        margin: 0 1px 0 0; /* adjust as you need */
        padding: 4px 10px; /* adjust as you need */
        width: 60px;
        text-align: center;
        text-decoration: none;
    }

    ul li a:hover
    { }

    ul div
    {   position: absolute;
        visibility: hidden;
        margin: 0;
        padding: 0;
    }

        ul div a
        {   position: relative;
            display: block;
            margin: 0;
            padding: 5px 10px; /* adjust as you need */
            width: auto;
            white-space: nowrap; /* Specify that the text in <p> elements will never wrap */
            text-align: left; /* adjust as you need */
            text-decoration: none;
        }

        ul div a:hover
        {  }

JavaScript Structure:

    :::javascript
    // Copyright 2006-2007 javascript-array.com

    var timeout = 500;
    var closetimer  = 0;
    var ddmenuitem  = 0;

    // open hidden layer
    function mopen(id)
    {
        // cancel close timer
        mcancelclosetime();

        // close old layer
        if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';

        // get new layer and show it
        ddmenuitem = document.getElementById(id);
        ddmenuitem.style.visibility = 'visible';

    }
    // close showed layer
    function mclose()
    {
        if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
    }

    // go close timer
    function mclosetime()
    {
        closetimer = window.setTimeout(mclose, timeout);
    }

    // cancel close timer
    function mcancelclosetime()
    {
        if(closetimer)
        {
            window.clearTimeout(closetimer);
            closetimer = null;
        }
    }

    // close layer when click-out
    document.onclick = mclose;

###Mutiple Level

With jQuery
===========

update coming soon...



With Bootstrap3 and jQuery
===========================

update coming soon...
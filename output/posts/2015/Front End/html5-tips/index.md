.. title: HTML5 Tips
.. date: 2015-01-13
.. modified: 2015-07-02
.. category: Front End
.. tags: HTML5, JavaScript, jQuery
.. slug: html5-tips
.. authors: Pengyin Shan
.. description: During JavaScript development in my job, I found HTML5 has some interesting features. I want to make notes of these features for future usage. Till July 2015, following features has been updated: Canvas, Drag and Drop.

#Canvas

###HTML

    :::html
    <canvas style="width:1000px; height:1000px;" id="thecanvas"></canvas>

###JavaScript Operation

####Get Context (2d)
    :::javascript
    var oCanvas = document.getElementById("thecanvas");
    var oCtx = oCanvas.getContext("2d");

####Add Text and Edit Text Style
    :::javascript
    //Example of Text Shadow. If you make them to 0, you can remove text shadow
    oCtx.shadowColor = "#000000";
    oCtx.shadowOffsetX = 0.5;
    oCtx.shadowOffsetY = 0.5;
    oCtx.shadowBlur = 0.5;
    //Example of Text Style
    oCtx.font = "normal 18px Arial";
    oCtx.fillStyle = "#ccc";
    //Draw Text
    oCtx.fillText("Hello World", 0, 0); //x-axis and y-axis

####Draw Existing Image to Canvas
    :::javascript
    var imageObj = new Image();
    //get src of existing image
    imageObj.src = document.getElementById('existing_image').src;
    oCtx.drawImage(imageObj, 0, 0); //x-axis and y-axis

####Download Canvas as Image
    :::javascript
    /**Create a (hidden) image to hold canvas data:
    <img hidden src="" id="downloadCanvas" />
    **/
    var dataURL = oCanvas.toDataURL('image/png');
    document.getElementById('downloadCanvas').width = oCanvas.width;
    document.getElementById('downloadCanvas').height = oCanvas.height;
    document.getElementById('downloadCanvas').src = dataURL;
    /**
    If you want to have a download link to download canvas image, make sure you have HTML such as:
    <a id="downloadBanner" href="#" class="button" download="banner_result.png">Download</a>
    Note "download" attribute is able to re-name the downloadable image.
    **/
    document.getElementById('downloadBanner').href = dataURL;

####Clear Canvas
    :::javascript
    //You may want to do this to remove unwanted elements from canvas
    oCtx.clearRect(0, 0, oCanvas.width, oCanvas.height);

#Drag and Drop

Examples are taken from <a href="www.w3schools.com/html/html5_draganddrop.asp">w3schools.com</a>.

###General Process

Draable stuff has `draggable = 'true'` attribute; has `ondragstart` attribute, which takes a method.

Destination stuff has `ondrop` and `ondragover` attribute. Both of them take method.

###ondragstart

This attribute takes a JavaScript method. This method takes a `event` parameter and describe what will happen when you start to drag.

You need to set the data to drag by using `event.dataTransfer.setData(format, event.target.id)`:

>`format` above can be `text`, `text/plain`, `text/html` etc, or `URL` format.

>This function set up the data that is take via `event.target.id`, which is the `id` for draggable stuff, and temparary store it. Note `event.target` now pointing to draggable stuff.

###ondragover

This attribute takes a JavaScript method. This method takes a `event` parameter and describe what will happen when you drag stuff over elements without drop the stuff.

Basic set up is `event.preventDefault()`, which prevents browser asking elements doing default behavior.

###ondrop

This attribute takes a JavaScript method. This method takes a `event` parameter and describe what will happen when you drop the draggable stuff.

First, you should do `event.preventDefault()`, which prevents browser asking elements doing default behavior.

Then, you need to get the data that you dragged by using `event.dataTransfer.getData(format)`. The format should corresponding what you had in `event.dataTransfer.setData()` method.

>The method will return all data that has same format.

You can get current dropdown container by using `event.target` (instead of draggable element). You can choose to append your draggable stuff by using

	:::javascript
	event.target.appendChild(document.getElementById(event.dataTransfer.getData(format))

if you passed `id` in `ondragstart`'s method. Or you can do whatever you want.
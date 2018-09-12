.. title: JavaScript Library Experience: FullCalendar
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: JavaScript
.. tags: JavaScript, jQuery, Bootstrap3
.. slug: javascript-library-experience-fullcalendar
.. authors: Pengyin Shan
.. description: This post describes my experience in using a JavaScript library - <a href="http://fullcalendar.io/">FullCalendar</a> to create calendar with events, using Java as back-end.



##First Impression and Basic Usage

I got a request in my work, asking me to research a open source JavaScript calendar library. The calendar should be able to do following:

>Add/Load/Delete Events, which needs a commucation with back-end. Event content can be configured, which means developer can over write event trigger function. Also developer can set up event time plot.

>Different views, as least have day,week,month view. Also user should have a way to view details in other years.

So I check FullCalendar and the demo looks ok for me. I decide to try it. Official website gave a simple piece of code for basic usage:

	:::html

	<link rel='stylesheet' href='fullcalendar/fullcalendar.css' />
	<script src='lib/jquery.min.js'></script>
	<script src='lib/moment.min.js'></script>
	<script src='fullcalendar/fullcalendar.js'></script>
	$(document).ready(function() {
	    $('#calendar').fullCalendar({
	    })
	});

It looks simple, but I encourted following problems and it takes a while to figure out solution:

##Problem 1
**The confusion of CDNJS source**

FullCalendar official website gives out `CDN` host source for `css` file and `javascript` file, which is the way I preferred, comparing to use local file. However, only three files are given with `CDN` url, which misleading me to thought *I only need these three files to run FullCalendar*, which is **wrong**.

After I run code in browser, I got error message in console, telling that **moment is not defined as function**. This error remind me that I need other JavaScript file to provide basic functionality.

##Answer 1

Make sure you have `fullcalendar.css`, `jquery.js`, `moment.js`, `fullcalendar.js` for basic setup.** `moment.js` needs to be put before `fullcalendar.js`.

##Problem 2
**CSS Style Problem (Cause my headache :)**

After I solve the problem above, I was able to see calendar data in browser, but **no style has been applied**. To solve the problem, I first try following solution:

>User console to compare my code and demo code. It turns out that we had same code/classes. The only problem is my classes in code didn't have style applied on.

>Change browser. *This is not a browser problem*.

>Re-check code to make sure if I miss any necessary stylesheet.*No*

>First check if all `CDN`
resources loading successfully. Then replace all `CDN` resource to local resource, and make sure all resources are in same version. *Not Work*

>Use a old stable version for FullCalender. *Not Work*

>Back to demo code and demo source code, make sure we have same JavaScript setting. *No difference between two codes.*

>- So I have to seek help on Google. A <a href="http://stackoverflow.com/questions/25178565/fullcalendar-layout-broken-because-css-loading-after-javascript-layout-calculati">post</a> in *StackOverflow* helps with this problem.

##Answer2
**Load Stylesheet in JavaScript**

I should adjust code as following:

	:::javascript

	$(document).on("ready", function() {
	    //This is the code to load stylesheet
	    $("<link rel='stylesheet' type='text/css' href='fullcalendar.css' />").appendTo("head");
	    $(window).on("load", function() {
	        $('#calendar').fullCalendar({
	        });
	    });
	});

It turns out that different from normal file loading process in front-end development, I need to **load source javascript file first, then after DOM is ready, loading stylesheet.**

>In this case, when `DOM` is ready, stylesheet is appending. The after DOM finish loading style sheet and begin to load `window`, my javascript code trigger.

**Important Notes**
- `$(document).ready` triggers after `HTML` elements has been loaded.
- `onload` event occurs later, after all content elements, such as `image`, has been loaded.
- Next time I get this probelm, I should try to load stylesheet later, using `"<link/>".appendTo("head")`.
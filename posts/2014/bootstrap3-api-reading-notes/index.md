.. title: Bootstrap3 API Reading Notes
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Front End
.. tags: CSS, Bootstrap3, JavaScript, jQuery
.. slug: bootstrap3-api-reading-notes
.. authors: Pengyin Shan
.. description: This is an old blog I created when I started to learn Bootstrap3, recording my thoughs after reading Bootstrap3 API Documentation

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

#CSS Part

This is a reading note for Bootstrap 3 Official API CSS part, including everything I think that will be useful for future web development.

Bootstrap3 needs to have `<!DOCTYPE html>` on top for html5 recogization purpose.

Bootstrap3 has "Mobile first" principle, so `<meta name="viewport" content="width=device-width, initial-scale=1">` should be added in `<head>` tag.

Bootstrap3 **requires** a container to hold all codes. so make sure add it before insert any more codes. Containers can not be nested:

	:::html
	<div class="container">
	...
	</div>

	<!--Or use this for a full width of device-->
	<div class="container-fluid">
	...
	</div>

##Grid System

In Aug 2014, I read a very good tutorial about grid system in bootstrap3 from http://www.tutorialrepublic.com/twitter-bootstrap-tutorial and wrote some notes:

- 12 content boxes in all devices

- mobile deivce has 1 column and 12 rows; tablet has 2 column and 6 rows

- desktop has 3 column and 4 rows

- large desktop has 4 column and 3 rows

- if col-md-* is different for each column, `.clearfix` help with reduce visible block to make sure 12 column grid

	:::html
	<!--First two lines has total grid of 6X2 = 12 grids, so use clearfix for next line. This row will have two equal width column-->
	<div class="row">
	<div class="col-md-6"><p>Box</p></div>
	<div class="col-md-6"><p>Box</p></div>
	<div class="clearfix visible-md-block"></div>
	</div>

	<!--First two lines has total grid of 4X3 = 12 grids, so use clearfix for next line. This row will have three equal width column-->
	<div class="row">
	<div class="col-md-4"><p>Box</p></div>
	<div class="col-md-4"><p>Box</p></div>
	<div class="col-md-4"><p>Box</p></div>
	<div class="clearfix visible-md-block"></div>
	</div>

Responsive utility class `.visible-md/xs/sm/lg-block` make `.clearfix` effectly only in special scale device. For example, if `.visible-xs-block`, this block will only be viewed on xs device(phone)

As a conclution, The way `clearfix visilbel-xs/sm/md/lg` work is everytime when a 12 grid appears, a `clearfix visible-XX-block` without any content *needs to appear*. For example:

	:::html
	<div class="row">
	<div class="col-sm-6 col-md-4 col-lg-3"><p>Box 1</p></div>
	<div class="col-sm-6 col-md-4 col-lg-3"><p>Box 2</p></div>
	<div class="clearfix visible-sm-block"></div>
	<!--There are 6*2=12 grids already, insert a clearfix with sm-->
	</div>

	<div class="row">
	<div class="col-sm-6 col-md-4 col-lg-3"><p>Box 3</p></div>
	<div class="clearfix visible-md-block"></div>
	<!--There are 4*3=12 grids already, insert a clearfix with md -->
	</div>
	<div class="row">
	<div class="col-sm-6 col-md-4 col-lg-3"><p>Box 4</p></div>
	<div class="clearfix visible-sm-block"></div>
	<!--Another 6*2 appears, so insert another clearfix with sm-->
	</div>
	<div class="row">
	<div class="clearfix visible-lg-block"></div>
	<!--There are 3*4 grid, so use clearfix with large-->
	</div>

`xs`: less than 768px; sm: 768 to 992; md: 992 to 1200; lg: larger than 1200

Similar as visible, there are `.hiddle-xs`, `.hidden-sm` `.hidden-md` and `.hidden-lg`, hide in special scale

Similarly there is print class: `.visible-print-block`: when print, hide block elements; `.visilble-print-inline/.visible-print-block`: hide inline/inline-block in print; `.hiddle-print`: hide elements in print

Other useful things that I got from Bootstrap offical API about Grid System is:

- The gap between columns is adjusted by **padding**.

- If more than 12 columns in a row, extra columns will be put to new line as one unit.

- If there is no `col-lg-`, then styles that apply to `col-md-` will also affect page on large device.

Place grid columns in any `class="row"`:

	:::html
	<div class="container-fluid">
	  <div class="row">
	    ...
	  </div>
	</div>

	<!-- `.col-md-offset-*` can be used to move columns to the right. `*` is how many columns this column moves: -->
	<div class="row">
		<div class="col-md-4"></div>
		<div class="col-md-4 col-md-offset-4"></div>
		<!-- last column will move to right, starting from the 9th column -->
	</div>

It is safe to use **nested column**. But make sure `class="row"` is added to nested part.

#Components Part


##Pannels*

Table or List can be added in panel body for format.

	:::html
	<div class="panel panel-default">
	<!--panel-default can be changed to panel-primary, panel-success, etc-->
		<div class="panel-heading">This page is disabled</div>
		<!--The way to define pannel heading-->
		<div class="panel-body">
		TextTest
		</div>
		<div class="panel-footer clearfix">
		<!--add panel footer-->
			<div class="pull-right">
			<!--This will make footer to the right of the panel-->
				<a href="#" class="btn btn-primary">Learn More</a>
			</div>
		</div>
	</div>

It is useful to put pannel with tables or list-groups. Just make `.panel` class wrap `.panel-heading`, `.panel-body`, and `.table`or`.list-group`.

	:::html
	<div class="panel panel-default">
		<div class="panel-heading">Panel Heading</div>
		<div class="panel-body">Panel Body</div>
		<ul class="list-group">
			<li class="list-group-item">Item One</li>
		</ul>
	</div>

##Breadcrumb

A breadcrumb is a navigation scheme that indicates the user's location in a website or web application. For example: `Home/Library/Data`.

	:::html
	<ul class="breadcrumb">
		<li><a href="#">Home</a></li>
		<li><a href="#">Products</a></li>
		<li class="active">Accessories</li>
	</ul>

##Pagination (Page Number Indicator)

	:::html
	<ul class="pagination pagination-sm">
	<!--'pagination-sm' can be skipped or change to -xs/-lg, etc. This is used to define size of pagination-->
		<li><a href="#">&laquo;</a></li>
		<!-- Left page arrow-->
		<li class="disabled"><a href="#">1</a></li>
		<!--item can be disabled-->
		<li class="active"><a href="#">2</a></li>
		<!--Active Page Number-->
		<li><a href="#">&raquo;</a></li> <
		!-- Right page arrow-->
	</ul>

Bootstrap3 also have *previous/next* indicator, which is called *Pager*

	:::html
	<ul class="pager">
		<li class="previous"><a href="#">&larr; Previous</a></li>
		<!-- two class can make button aligned to left and right of window. &larr is a left arrow -->
		<li class="next disabled"><a href="#">Next &rarr</a></li>
		<!-- pager can be disabled -->
	</ul>

##Labels and Badges

	:::html
	<h2>Bootstrap heading
	<span class="label label-default">New</span>
	</h2>
	<!-- create inline label 'new' for heading. 'label-default' can be replaced with label-success, etc -->
	<li>
	<a href="#">Notification <span class="badge">5</span></a>
	</li>
	<!-- badge is the number indicator for email or notification button. For example, a 5 will show if there are 5 notifications -->

##Progress Bar

	:::html
	<!-- .progress-stripped is a class to make colorful effect. .active is a class to make animate effect -->
	<div class="progress progress-stripped active">
		<!-- process-bar-success can be replaced by process-bar-warning, etc -->
		<div class="progress-bar process-bar-success" style="width: 60%">
			<span class="sr-only">20% Complete</span>
		</div>
	</div>

Process bar can also add label to indicate the numbered process. Reference: http://getbootstrap.com/components/#progress-label.

##Jumbotron

Jumbotron is used as a header panel with important content, that can be put on top of homepage. For example, a Header combined with a paragraph and a read-more button

	:::html
	<div class="jumbotron">
		<h1>Welcome to Website</h1>
		<p>Key Notes: XXX...</p>
		<p><a href='#' class="btn btn-primary">LearnMore</a></p>
	</div>

##Wells

Wells componet make a part of content like sink in well. Used for static text.

	:::html
	<div class="well well-large/well-small">
	In a well...
	</div>

##Close icons

A X icon on right of panel so that user can close this panel after read it

	:::html
	<div class="alert alert-warning">
		<a href="#" class="close" data-dismiss="alert"> &times;</a>
		<strong>Warning!</strong> There is a problem
	</div>

##Bootstarp3 Help Class

`.pull-left/.pull-right` will floats an element to left or right

`.text-muted` make a element grayed out by change its color value

`.clearfix` clear the float of any element

##Buttons

###Available Classes:

`btn-default/primary/info/success/warning/danger/link`: define attributes of button

`btn-lg/sm/xs`: define size of button

`btn-block`: define a button that covers full width of parent element

`diabled`: disable a button

`data-loading-text="Loading..."`: can be add when a button is in loading state (automatically turn off in firefox)

Toggle Button (hover effect): `data-toggle="button"`

###Button group:

	:::html
	<div class="btn-group/btn-group-vertical btn-group-lg/sm/xs">
	<!-- Can add btn-group-justified to make group buttons alignment justified -->
		<button type="button" class="btn btn-primary">Left</button>
		<button type="button" class="btn btn-primary">Right</button>
		<div class="btn-group">
		    <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
		    Button Group can be nested
		    </button>
		</div>
	</div>

`.button-toolbar`: class that wrap several `.button-group`s.

Justified button groups: use `.btn-group-justified`. You must **wrap each button in a button-group**:

	:::html
	<div class="btn-group btn-group-justified">
	  <div class="btn-group">
	    <button type="button" class="btn btn-default">Test Button1</button>
	  </div>
	  <div class="btn-group">
	    <button type="button" class="btn btn-default">Test Button2</button>
	  </div>
	</div>

###Available Methods for Button

`$().button('toggle')`: change any button to toggle state

	:::javascript
	$(document).ready(function(){
		$('#myButton').click(function(){
			$(this).button('toggle');
			});
	});

`$().button('loading')`: when loading, button is disabled and text is swapped with the value of 'data-loading-text' attribute of button element

`$().button('reset')`: reset button state by swapping text to original text

`$().button(string)`: reset button to show this string

##Dropdown

Dropdown can be done within navabar, nav or buttons. Reference: http://getbootstrap.com/components/#btn-dropdowns-single

	:::html
	<!-- 'nav nav-pills' is nav, 'btn-group' is button -->
	<div class="navbar navbar-static">
		<div class="navbar-inner">
			<a href='#' class="First">
			First
			</a>
			<ul role="navigation" class="nav">
				<li class="dropdown">
					<a href="#" data-toggle="dropdown" class="dropdown-toggle">
					First Dropdown <b class="caret"></b>
					</a>
					<ul class="dropdown-menu">
						<li><a href='#'>Second Dropdown</a></li>
						<!-- <li class='divider'></li> can be add here if a button dropdown needs a divider -->
					</ul>
				</li>
			</ul>
		</div>
	</div>
	<!-- a button can be directly used as dropdown: <button data-toggle...>Dropdown <span class="caret"></span></button> -->

###Available Methods for Dropdown

`$().dropdown('toggle')`: toggle item for a given dropdown

###Available Events for Dropdown

`show.bs.dropdown`: trigger when show instance method is called. can be reached by `event.relatedTarget`

`shown.bs.dropdown`: triger when a dropdown is visible. Will wait for css.
can be reached by event.relatedTarget

`hide.bs.dropdown/hidden.bs.dropdown`: same except hide instance

	:::javascript
	//After click ok button, dropdown will be expanded
	$(document).ready(function(){
		$(".dropdown").on("show,bas.dropdown",function(e){
			var linkedText = $(e.relatedTarget).text();
			//linkedText will be firstClass item in dropdown
			alert("Click on OK button to view the dropdown menu for -" + linkText);
			});
	});

##Tooltip

For performance reasons, tooltip must be initialized first

	:::javascript
	$(document).ready(function(){
		$(".classOfItem a").tooltip();
		//Assume that structure of item is .classOfItem <a>...</a>
	});

Trigger while set position of tooltip

	:::javascript
	$(".classOfItem").tooltip({placement: 'top/right/buttom/left'});

###Available Method for Tooltip

`$().tooltip(options)`: attach tooltip to elements, options can be found online, include titile, delay, etc

`$().tooltip('show'/'hide'/'toggle'/'destory')`: show/hide/toggle/destroy tooltip

##Popover

Popover is like tooltip but is a panel with header and body content. It also needs to be initialize first

	:::javascript
	#(document).ready(funtion(){
		$(".classOfItem a").popover();
		//Same as tooltip. Popover can set position when triggered. See tooltip part for detail
	});

Popover has similar method as tooltip: options/show/hide/toggle/destroy.

##Alerts

	:::html
	<div class="alert alert-warning">
		<!-- 'alert-warning' can be changed to error/success/info -->
		<a href="#" class="close" data-dismiss="alert">&times;</a>
		<!-- enable close button for this alert message. Need JavaScript plugin-->
		<strong>Warning!</strong>There was a problem!
	</div>

`.alert-link` adds link in alerts:

	:::html
	<div class="alert" role="alert">
	  You must click <a href="#" class="alert-link">Link to other url</a> !
	</div>

###Available Methods for Alerts

`$().alert`: wrap all alert with close functionality

	:::javascript
	$(.close).click(function(){
		$(".alert").alert();
	});

`$().alert('close')`: close a alert box

##Tabs

To use tab in nav bar, create `<ul>` with `class="nav nav-tab"` and each `<li>` has a `href`

Tabs can be add dynamically with any javascript: simply specify the `data-toggle="tab"` on each tab, as well as create a `.tab-pane` with unque ID for every tab and wrap them in `.tab-content`.

Create dynamic tab with javascript:

	:::javascript
	$(document).ready(function(){
		$("#myTab a").click(function(e){
			//Note this function is defined on a href link
			e.preventDefault();
			$(this).tab('show');
			//Method to activate a tab using .tab('show')
			});
	});

#Form Part

Any element with `.form-control` has `width:100%;` by default.

You can nest the `.input-group` in `.form-group` but don't mix them directly.

Vertical Form in Bootstrap3:

	:::html
	<form role="form">
		<div class="form-group">
			<label for="example"></label>
			<input type="" id="example" class='form-control' placeholder=''>
		</div>
	</form>

Inline Form in Bootstrap3 (i.e. For a device that has less than 768px width`.xs`, the elements that listed inline in larger device will list in block)

	:::html
	<form class='form-inline' role="form">
		<div class='form-group'>
			<label for="examle">You must always add labels. You can use .sr-only class to hide it</label>
			<input type="" class="form-control" id="example"/> //Define grid for input area
				<input ...>
		</div>
	</form>

##Supported Form Controls

All html5 input type are supported: `text`, `password`, `datetime`, `datetime-local`, `date`, `month`, `time`, `week`, `number`, `email`, `url`, `search`, `tel`, `color`

`<fieldset>` can be used to wrap a few form-group in order to easily apply style.

`.disabled` can be added to `.radio` or `.checkbox` or `<fieldset>` to disable these elements.

`.checkbox-inline` or `.radio-inline` create inline-element. They needs to be wrpped in `<label>`:

	:::html
	<label class="checkbox-line">
		<input type="checkbox" id="test" value="test"> test
		<!-- 'test' here can be skipped if this checkbox don't need any label. But this input must always be wrapped in <label> tag.-->
	</label>

`.form-control-static` can be put in a `<p>` tag to create a text that hold the place as a input field

	:::html
	<div class="form-group">
		<label for="test">Test:</label>
		<p class="form-control-static" id="test">This is a text</p>
	</div>

After using Javascript to valid data in input field, '.has-warning',`.has-error` or `.has-success` can be added to input fields to show validation result. `<span class="glyphicon plyphicon-warning-sign form-control-feedback>` can be added after `<input>` field if optional icons are needed.

`<span class=".help-block"` can add help text under input field

##Input Group

To add icon, put `<span class='input-group-addon'></span>` inside a input-group class

To add button attched to input, use `.input-group-btn`for a span and add button in span. Put this span right after input box.

Input group can have height class `.input-group-lg`.

#Image and Media Part

Use Bootstrap3 to modify shape of image: `.img-rouned`,`.img-circle`,`.img-thumbnail`.

`.thumbnail` define a div with shape of thumbnail. div can include jpg file. Best use with grid class.

Media Objects: create layout like twitter or Linkedin name signature

	:::html
	<div class='media'>
		<a href="#" class="pull-left">...
		<!--This part will be left panel, best to put thumbnail in -->
		</a>
		<div class="media-body">
			<h1 class="media-heading">
			Header
			</h1>
			<p>.
			Body
			</p>
		</div>
	</div>

Reference Glyphicon library: `<span class="glyphicon glyphicon-class-name"></span>`.

#List and Nav Part

##List

Horizontal list: <ul class='list-inline'>

Horizonal Defination List: work is on left, corresponding explanation is on right

	:::html
	<dl class="dl-horizontal">
		<dt>Word</dt>
		<dd>Explanation</dd>
	</dl>

List Groups (like a vertical nav bar):

	:::html
	<ul class='list-group'>
		<li class="list-group-item"></li>
	</ul>

Make list group hyperlink (vertical nav bar)

	:::html
	<div class="list-group">
		<a href='#' class="list-group-item (active)">
			<span>
				<!--You can dd .glyphicon for icons before text. span is easier to use-->
			</span>
		</a>
	</div>

##Nav Bar

Create nav bar in tabs: `<ul class="nav nav-tabs"><li class="active">`. To add icon to tabs, just put span.

Create nav bar in pills: `<ul class="nav nav-pills"><li>`.

Create vertical nav bar: `<ul class="nav nav-pills nav-stacked">`.

Dropdown nav bar:

	:::html
	<ul class="nav nav-tabs">
		<li class="dropdown">
			<a href="#" data-toggle="dropdown" class="dropdown-toggle">FirstClass<b class="caret"></b></a> //First class menu
				<ul class="dropdown-menu">
					<li>... //Second class items

To make a justified nav bar, or make any elements justify-aligned, use `nav-justified` class. The way to use it is:

	:::html
	<ul class='nav-justified'>
		<li>...</li>
		<li>...</li>
		<li>...</li>
	</ul>

Disable nav bar items:

	:::html
	<li class="disabled">
		content
	</li>

A full example:

	:::html
	<nav role="navigation" class="navbar navbar-default">
		<!--First class nav bar-->
		<div class="navbar-header">
			<button type="button" data-target="#navbarCollapse" data-toggle="collapse" class="navbar-toggle">
			<!--Header is the button that when change to mobile, the only item that will not be put to menu button-->
				<span class="iron-bar"></span>
				<span class="iron-bar"></span>
				<!--put as many as the number of nav items-->
			<a href="#" class="">NavBarHead</a>
		</div>
		<div id="navbarCollapse" class="collapse navbar-collapse">
			<ul class="nav navbar-nav">
				<li class="dropdown">
					<a data-toggle="dropdown" class="dropdown-toggle" href="#">
					FirstClassItem <!-- //Item that is going to have dropdown-->
					<b class="caret"></b>
					</a>
						<ul role="menu" class="dropdown-menu">
							<li>
							<a href="#">SecondClassItem</a>
							</li>
							<!--Can add <li class="divider"></li> as divider between items-->

Fixed position nav bar: add `.navbar-fixed-top/.navbar-fixed-bottom` in `nav` tag.

Full width nav bar: add `.navbar-static-top/bottom` in `nav` tag

Nav Bar with Search Form:

	:::html
	<div id="navbarCollapse" class="collapse navbar-collapse">
		<form role="search" class="navbar-form navbar-left">
			<div class="form-group">
				<input type="text" placeholder="search" class="form-control">

Inversed navbar (color): add `.navbar-inverse` in `nav` tag

#Table Part

`.table-striped` make table's nth row has different color than n-1th row

`.table-bordered` add border

`.table-hover` add hover effect

`.table-condensed` cut the cell padding in half. Most obviously cell height is in half size.

	:::html
	<table class="table table-XXX">
	<thead></thead>
	<tbody></tbody>
	</table>

Responsive Table in Bootstrap3: `.table-responsive`. Will add scroll bar if table width is larger than container width, when device size is under 768px(i.e.`.xs`);

#Text Part

`.small` crates grey and smaller font

`.lead` creates standing-out font

text alignment class: `text-left`, `text-center`, `text-right`, `text-justify`, `text-nowrap`

text style class: `<b>`:bold, `<big>`:bigger, `<code>`:computer code, `<i>`:italic, `<mark>`:highlight, `<strong>`: strong, `<sub>/<sup>`:lift and move down font, `<ins>`: unline, `<del>`: delete line

text style class:

-`.text-lowercase`

-`.text-uppercase`

-`.text-capitalize`: only first letter of each work will be upper case

Bootstrap text emphasis class (text with color):

-`.text-muted`: greyed out

-`.text-primary`: important, default is blue

-`.text-success`: default is green

-`.text-info`: default is blue-grey

-`.text-warning`: default is brown

-`.text-danger`: default is red

Quotes:

-`<blockquote>`: start of a block of quote

-`<cite>`: cite author name

-`.pull-right`: all block text align is right













































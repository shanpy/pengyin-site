.. title: Reading Notes for D3.js Part I (Chapter 1 to Chapter 5)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-1-to-5
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part I (Chapter 1 to Chapter 5)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for "Interactive Data Visualization for the Web - An Introduction to Designing with D3" by *Scott Murray*, pulished by O'Reilly

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 2: D3 Introduction

D3 is a short-name for *Data-Driven Documents*. The data is from data provider (users, customers, etc) and the documents are documents based on web, such as HTML, SVG.

The process that D3 create data-driven document is:

- Load data to browser cache

- Bind data to elements in document, and create new element if need

- Analysis bound datum for each element and set up virtualization attribute. Finish transforming element.

- Transitioning element based on user input

Transforming is very important. You will need to create transforming rule in this step.

D3.js is great for explaining data instead of exploring data.

D3.js will not hide you original data in client side.

#Chapter 3: Basic Skill in Web

GeoJSON is similar to JSON, specailly for geograpic data, like points(longitude, latitude) or shapes.

Make sure not decling too many global object. All global variables are attributes for `window` object. You can declare one or few gloal object then assign attribute to this global object.

In SVG, if `x` is getting larger, graph will move towards *right*. If `y` is getting larger, graph will move towards *bottom*.

##Graphs in SVG:

`rect`: `x` and `y` is the location of left top corner.

	:::html
	<rect x="0" y="0" width="500" height="50"/>

`circle`: `cx` and `cy` is the location of center of circle. `r` is radius.

`ellipse`: similar to `circle`, but instead of `r`, it needs `rx` and `ry`.

`line`: `x1` and `y1` is used for location of starting point. `x2` and `y2` is used for location of end point. *You must use `stroke` to assign color to line so you can see it*.

	:::html
	<line x1="0" y1="0" x2="500" y2="0" stroke="black"/>

`text`: creatign text. `x` is the left top corner of text, `y` is the base line of text. Letters like *p* or *y* have parts that are under base line. `font-family | font-size | etc` can be used to add style to text.

##Style/Attribute for SVG Element

`fill`: fill color

`stroke`: border color

`stroke-width`: width of border

`opacity`: how transparent the graph will be

You can also assign `.class` to svg element for style. Same attributes will apply:

	:::html
	<circle cx="50" cy="50" r="50" class="test"/>

	<style type="text/css">
		.test{
			fill: red;
			stroke: yellow;
			stroke-width: 2;
		}
	</style>

In SVG, there is no layer or `z-index`, so the sequence that elements are inserted is the sequence of the real graph. They can be partially or fully covered by other graphs.

It is really important to check if user's browser supports SVG or not first. *Modernizr* (http://modernizr.com) can be used for this.

	:::html
	<script type="text/javascript" src="path_to_modernizr.js"></script>
	<script type="text/javascript">
		Modernizr.load({
			test: Modernizr.svg && Modernizr.inlinesvg,
			yep : [
				path_to_d3.js, path_to_other_css_file
			]
		});
	</script>

#Chapter 4: Install D3.js

It is important to set `<meta charset="utf-8">` for correctly compile D3.js.

#Chapter 5: Data

`.select("tag_name")`: reference the first element that has tag_name.

`.text("content_of_text")`: insert text.

##Use CSV

D3 can load CSV file via `d3.csv()`:

	:::javascript
	d3.csv("test.csv", function(data){
		console.log(data);
	});

All data, includes number, is saved as string in csv after you load it.

`d3.csv()/d3.json()/d3.tsv()` are *asynchromous* methods, which means other javascript methods will run *at the same* time when these method runs. Also, asynchromous will run not matter if the data file is successfully loaded or not.

To avoid any program based on asynchromous, you can declare a global variable first, then call `d3.csv()` with a `error` parameter. After finish loading data, if these is no error, assign data to this global variable. Then you can call other functions that should run after successfully load data. Put error handing message if there is any error.

	:::javascript
	<!--This is the code part from book -->
	var dataset;
	d3.csv("food.csv", function(error, data) {
		if (error) {
			console.log(error);
			// Output error message if there is any error
		} else {
			console.log(data);
			// If there is no error, assign loaded data to global variable, then call other functions
			dataset = data;
			generateVis();
			hideLoadingMsg();
		}
	});

To create a new element with data binding, use `enter()`.This method can create new placefolder if dataset has more elements than existing elements. Next method can operate based on new placeholder(s):

	:::javascript
	<!--This is the code part from book -->
	var dataset = [ 5, 10, 15, 20, 25 ];

	d3.select("body").selectAll("p") //currently no 'p' element exist, but you can select them first.
	.data(dataset) //bind data in dataset
	.enter() //create 5 placeholders
	.append("p") //insert 'p' element to these 5 placeholders
	.text("New paragraph!"); //each holder has text

	/*
	Result:
	<p>"New paragraph!"</p>
	<p>"New paragraph!"</p>
	<p>"New paragraph!"</p>
	<p>"New paragraph!"</p>
	<p>"New paragraph!"</p>

	Each number in dataset is binding to the '__data__' attribute for each 'p' element. You can find it in console. For example, the first 'p' element has a `__data__` attribute. Value is 5.
	*/

As long as you use `data()` method, you can access a anonymous function that has a parameter `d`. `d` is the value of the corresponding data in dataset. You can use this function in continous methods whenever you need. For example:

	:::javascript

	<!--Link to the code above-->
	.data(dataset)
	.enter()
	.append("p")
	.text(fucntion(d){
		return "test " + d;
	});

	/*
	Result:
	<p>test 5</p>
	<p>test 10</p>
	<p>test 15</p>
	<p>test 20</p>
	<p>test 25</p>
	*/















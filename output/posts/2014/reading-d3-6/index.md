.. title: Reading Notes for D3.js Part II (Chapter 6)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-6
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part II (Chapter 6)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 6 : Draw Graph basiced on Data

code example for this chapter is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-II.html">*here*</a>. This part involves lots of code practice.

Everything is `rectangular` for browser. Using `div` is the easiest way to draw a *Bar Chart*.

###code part I

`attr()` set up the value for a DOM attribute, such as `.attr('class','bar')`

`style()` add css style to an element

`classed()` quickly add/delete class to an element, such as `.classed('bar',true/false)` to add/delete a class `bar` to an element

`select().selectAll().data().enter()` put data to `data`, then use/create elements using `selectAll()`, append them in `select()`, for example:

	:::javascript
	d3.select(document.getElementById("test")) //select the space that is a div "test"
		.selectAll('div') //create divs in 'test' div
		.data(dataset).enter(); //for each new div, put data to it

##Draw SVG

###code part II

For each `SVG` element, all its properties are defined by `property='XXX'`, such as `<element property = 'value'></element>`

First step is always create a `SVG` element:

	:::javascript
	var w = 200; //This is pixel
	var h = 100;
	var svg = d3.select(document.getElementById('chapter6').getElementsByClassName("2")[0])
									.append('svg')
									.attr('width',w)
									.attr('height',h);
	//Create size of svg

Then draw a circle:

	:::javascript
	var dataset = [10,9,15,25,18,26,11,13];
	var circles = svg.selectAll('circle')
					.data(dataset)
					.enter()
					.append('circle'); //create circle and put data in

	circles.attr('cx',function(d,i){
				return (i*20)+10;
				})
				.attr('cy',h/2)
				.attr('r',function(d){
				return d;
				})
				.attr('fill','yellow')
				.attr('stroke','pink');
				//Add center point and radius. Then add color to it

##Draw Bar Chart

###code part III

In D3, always choose element that you need, even before it is created.

`SVG` only support alignment through *left-upper* corner. To make sure bar chart using bottom alignment:

- make the `y`, which is the vertical point of alignment point, equals to `total height - its own height`

- then make each bar has height equal to its data.

Make color be ratio to data:

	:::javascript
	//add color to rectangular. Make each bar has color ratio to its data
	rect.attr('fill',function(d){
			return("rgb(0,0,"+(d*10)+")");
	});

The way to add `tags` is the same to add `rect`:

	:::javascript
	//create text
	var text = svg.selectAll('text')
					.data(dataset)
					.enter()
					.append('text');

	//set text position. Adjust position a little bit
	text.attr('x',function(d,i){
					return i*(w/dataset.length)+5;
					})

	text.attr('y', function(d){
					return h-(d+5);
					});

	//add text value
	text.text(function(d){
					return d; //Get integer value in JavaScript
					});

	//set font family
	text.attr('font-family','sans-serif')
			.attr('font-size','1em')
			.attr('fill','blue')
			.attr('text-anchor','middle'); //set text alignment

##Draw Scatter Plot

###code part IV

For a scatter plot, data should look like an array of arrays:

	:::javascript
	var dataset = [
									[5,10],
									[15.30],
									[60,75],
									[99,35]
				];
	//First Numer is X axis, Second Numer is y axis

The way to draw a scatter plot is generating lots of circles on `svg`, each circle is a point:

	:::javascript
	//prepare data
	var dataset = [
					[5,10],
					[115,130],
					[40,40],
					[160,100],
					[199,135]
					];

	//create svg element
	var w = 300; //This is pixel
	var h = 150;
	var svg = d3.select(document.getElementById('chapter6').getElementsByClassName("4")[0])
	.append('svg')
	.attr('width',w)
	.attr('height',h);

	//create circles
	var circle = svg.selectAll('circle')
	.data(dataset)
	.enter()
	.append('circle');

	//set up cx, cy, r
	circle.attr('cx',function(d){ //Here, d is the single array in array group
						return d[0]; //note it should be first element in array
					}).attr('cy',function(d){
						return h-d[1]; //y should be second element in array
					});

	//Make area of circle be proportional to data, using A = π*r^2. We just assume y is the area here
	circle.attr('r',function(d){
						return Math.sqrt(d[1]/3.14) + 5;
					}).attr('fill','pink');

	//Add Tags
	var text = svg.selectAll('text')
						.data(dataset)
						.enter()
						.append('text');

	text.text(function(d){
						return d[0] + "," + d[1];
					});

	text.attr('x',function(d){
						return d[0];
					});
	text.attr('y',function(d){
						return h-d[1];
					});
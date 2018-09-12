.. title: Reading Notes for D3.js Part III (Chapter 7)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-7
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part III (Chapter 7)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 7 : Scale (Linear)

code example for this chapter is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-III.html">**here**</a>. This part involves lots of code practice.

In D3, the scales are the functions that has parameters. You pass value to these functions, then they pass out values based on scale.

`input domain` means possible range for input values

`output range` means possible range for output values, mostly by pixels.

`normalization` means based on possible min and max value, transfer a value to a new value *between 0 and 1*. This is what we are doing for linear scale.

##Create Scale

###Code Part I

	:::javascript
	var scale = d3.scale.linear(); //Now scale is a function for linear scale

	scale.domain([100,500]); //set up input domain

	scale.range([10,350]); //set up output range

	//now scale(100) will return 10, scale(300) will return 180

##Zoomed Scatter Plot

###Code Part II

We can make the input range more flexiable by using `d3.min()` and `d3.max()`. Normall we can just do `d3.min(dataset)`. To get max value from an array of arrays:

	:::javascript
	var dataset = [
					[50,100],[20,200],[74,40],[0,300]
					];
	d3.max(dataset,function(d){
		return d[0];//This will compare x value for single array. d[1] will compare y value
	})

	//Full Code to create Zoomed Scatter Plot
	var w = 400;
	var h = 250;
    //Add padding to make sure circle will not be cut to half
    var padding = 50;

	var dataset = [
				[50,50],[20,120],[74,35],[85,85],[60,99]
				];

	//X Axis: Make input domain be max in dataset, based on x value. Output range is the width of SVG
	var xScale = d3.scale.linear()
					.domain([0, d3.max(dataset, function(d){ return d[0];})])
					.range([5,w-padding]);

	//Y Axis: Make input range be max in dataset, based on y value. Output range is the height of SVG
	var yScale = d3.scale.linear()
					.domain([0, d3.max(dataset, function(d){ return d[1];})])
					.range([h-padding,5]);	//Note normally larger y is at bottom. We change to make larger y on top

    //Radius: Make a self defined scale so that the radius is between 2 and 5, but still show scales
    var rScale = d3.scale.linear()
    				.domain([0, d3.max(dataset, function(d){ return d[1];})])
    				.range([2,5]);


	//Create SVG and Add Border to it
	var svg = d3.select(document.getElementById("chapter7").getElementsByClassName('2')[0])
				.append('svg')
				.attr('width',w)
				.attr('height',h);

	//create a scatter plot
	var circle = svg.selectAll('circle')
			.data(dataset)
			.enter()
			.append('circle');

	//Set cx, cy to new value based on scale
	circle.attr('cx',function(d){
		return xScale(d[0]);
	});

	circle.attr('cy',function(d){
		window.console.log(yScale(d[1]));
		return yScale(d[1]);
	});

	circle.attr('r',function(d){
		return rScale(d[1]);
	});

	circle.attr('fill','green');

	//Set tag based on scale
	var text = svg.selectAll('text')
					.data(dataset)
					.enter()
					.append('text');

	text.text(function(d){
					return d[0] + "," + d[1];
				});

	text.attr('x',function(d){
		return xScale(d[0]);
	});
	text.attr('y',function(d){
		return yScale(d[1]);
	});
	text.attr('fill','pink');

	//Now if svg change, the position of circles will adjust automatically

##Other Methods and Scales

`scale.nice()`: Extend the domain so it starts and ends on nice round values. Following formula: `exp(round(log(dx))-1)`. For example, `[0.998, 2.5555]` to `[1,2.5]`

`scale.rangeRound()`: Round ranges to closest `intenger`

`scale.clamp()`: Force all values that *out of range* to be in closest range, i.e, max or min value.

`scale.sqrt`: square root scale

`scale.pow`:  power scales, following `y = mx^k + b`

`scale.log`: log scales, following `y = mlog(x) + b`

`scale.quanitize`: a variant of linear scales with a discrate rather than continuous range. for example `quantize(0.49)` returns 0 and `quantize(0.51)` returns 1

`scale.quantile`: map an input domain to a discreate range. Input domain is `discreate` value

`scale.ordinal`: input domain is un-qualified value. For example, `apple` or `monkey`

`d3.time.scale`: scale for date and time
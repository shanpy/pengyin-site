.. title: Reading Notes for D3.js Part IV (Chapter 8)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-8
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part IV (Chapter 8)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 8 : Axes

code example for this chapter is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-IV.html">**here**</a>. This part involves lots of code practice.

The axes in D3 are functions with parameters. Differnt from scale, axes function will not return anything. Instead, it will geneate elements such as axes line, axes tags, etc.

Note: *Axes function only apply to SVG*

Using `d3.svg.axis(scale)` to set up axis with certain scale.

Using `axis.orient('bottom/top/left/right')` to set up location of tags in axis.

Using `svg.append('g').call(axis)` to append axis to svg. `g` means a *group* element. This *group* element includes `path`,`line` and `text` elements for axis.

You can give style to axis, using *css*. By using `.attr('class','class_name')`, you can assign class to `g` group, then set style in style sheet using `.class_name line{}` or `.class_name text()`. `path` and `line` can share same rule in stylesheet.

*Note: you should use svg attributes in style sheet, instead of css attributes*

`shape-rendering` style make sure the number of tags in axis is as clear as pixels.

You can move axis to bottom/left/right using `transform` attribute and `translate()` function. For example:

	:::javascript
	//...
		.attr('transform','translate(0,10)')
		//move axis down in 10. Note positive y means going down

		.attr('transform','translate(10,0)')
		//move axis right in 10. This usually apply to y-axis.

`.ticks(number)` is to set how many axis tags you want. This is just a suggestion, D3 will *automatically* adjust to it.

`d3.format()` can set up a format. For example, `d3.format('.1%'')` means make a number to keep one decimal point, then add '%' after it. Then you can use `axis.tickFormat(d3.format('.1%''))` to make this apply to axis tags, if you want.

*Code Example for this Chapter* <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-IV.html">You can check result of code here</a>

	:::html
	<!--style after adding axis-->
	<style type="text/css">
			.axis path,
			.axis line {
			  fill: none;
			  stroke: green;
			  shape-rendering: crispEdges;
			}

			.axis text{
				font-size: 10px;
			}
	</style>

	<script type="text/javascript">


		//set up SVG
		var h = 400;
		var padding = 5;

		//set up random data set
		var dataset = [];
		var numOfPoint = 6; //we want 10 point
		var xRange = Math.random() * 100;
		var yRange = Math.random() * 100;
		for(var count=0; count<numOfPoint; count++){
			var newx = Math.floor(Math.random() * xRange);
			var newy = Math.floor(Math.random() * yRange);
			dataset.push([newx,newy]); //Add array to empty array
		}

		var svg = d3.select(document.getElementById('chapter8').getElementsByClassName('1')[0])
					.append('svg')
					.attr('width', '100%') //This can make svg take full width of div
					.attr('height','400');

		var w = document.getElementsByTagName('svg')[0].offsetWidth; //get width of svg, assign it to w variable

		//set up scatter plot
		var circle = svg.selectAll('circle')
					.data(dataset)
					.enter()
					.append('circle');

		var xScale = d3.scale.linear()
					 	.domain([0, d3.max(dataset,function(d){ return d[0]; }) + padding])	//add extra padding to make sure leftest circle not be cut through middle
					 	.range([0, w-padding*3]);
		var yScale = d3.scale.linear()
						.domain([0, d3.max(dataset, function(d){return d[1]; })+padding])
						.range([h-padding*3,0]);
		var rScale = d3.scale.linear()
						.domain([0, d3.max(dataset, function(d){ return d[1]; })])
	    				.range([5,15]);

	    circle.attr('cx',function(d){
	    	return xScale(d[0]);
	    }).attr('cy',function(d){
	    	return yScale(d[1]);
	    }).attr('r',function(d){
	    	return rScale(d[1]);
	    }).attr('fill','pink');

	    //set up tag for scatter plot
	    var text = svg.selectAll('text')
	    				.data(dataset)
	    				.enter()
	    				.append('text');
	    text.text(function(d){
	    	return d[0] + ',' + d[1];
	    });
	    text.attr('x',function(d){
	    	return xScale(d[0]);
	    }).attr('y',function(d){
	    	return yScale(d[1]);
	    });

	    //Add line betwen these points
		var lineFunction = d3.svg.line()
	                        .x(function(d) { return xScale(d[0]); })
	                        .y(function(d) { return yScale(d[1]); })
	                        .interpolate("linear");
	    svg.append('path').attr('d',lineFunction(dataset))
	    				.attr('stroke','blue')
	    				.attr('stroke-width','1')
	    				.attr('fill','none');

	    //set up axis
	    var xAxis = d3.svg.axis()
	    				.scale(xScale) //use scale
	    				.orient('bottom') //make axis at bottom
	    				.ticks(5);//make only 5 tags for axis
	    var yAxis = d3.svg.axis()
	    				.scale(yScale)
	    				.orient('right') //make axis on left
	    				.ticks(7);//make only 7 tags for axis

	    //Append axis to svg
	    svg.append('g')
	    	.attr('class','axis')
	    	.attr('transform','translate(0,'+(h-padding*4) + ')') //make x axis move down, with the distance of h-padding*2
	    	.call(xAxis); //add axis
	    svg.append('g')
	    	.attr('class','axis')
	    	.attr('transform','translate(' + padding*4 + ',0)')	//make y axis move right, with the distance of padding
	    	.call(yAxis);

	</script>


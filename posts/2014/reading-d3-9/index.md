.. title: Reading Notes for D3.js Part V (Chapter 9)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-9
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part V (Chapter 9)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 9 : Animation

code example for this chapter is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-V.html">**here**</a>. This part involves lots of code practice.

##Transition and Animation

When we `refresh` a d3 chart, we can use `transition` to add `animation` to this chart, so it looks better.

`ordinal scale` can show the `discreate` domain, such as a set of names or categoires. These names or categories will be shown by a set of sequence, from left to right, equally.

You only need an `array` that contais name of categories to set of `range` of an `oridinal scale`. For example, `.domain([1,4,22,44)`.

`d3.range()` can automatically generate continous array, normally we can use `d3.range(dataset.length)` for `x` position of each bar in chart.

`range()` or `rangeBands()` can be used to do automatically `banding`. For example, `.rangeBands([0,w])` can automatically divide `0` to `w` to several parts. All parts have same width. `.rangeBands([0,w], 0.2)` means to set the `gap` between each part to be `20%` of each part's width.

`rangeRoundBands()` is similar to `rangeBands()`. It will round the output to `integer`.

`function(d,i){...}` can automatically get `i`, which is the *index* for `d` value. For example, `attr('x',function(d,i){ return xScale(i); }` will autotically set position for each `d` value.

Steps to update a d3 chart :

- Change value of dataset

- Re-binding new value to existing elements

- Re-set attribution so that new elements can be visible

To add a `event listener`, you can do `d3.select('p').on('click',functon(){...})`

`.transition()` is used to add animation when you refresh your chart. This function needs to be inserted *before* changing of any attribute, and *after* select new elements. For example, `.data(dataset).transition().attr(...)`. D3 will automatically add transition value after you call this function.

Default duration for a `transition` is `1000`, which is 1000ms or 1s. `.duration()` can be used to set up duration. You must push this function *after* calling `.transition()`. For example, `.transition().duration(2000)` can change duration to 2s.

It is more proper to set small transition(such as `click`) to `150ms`. Long transition, such as refresh all chart, should be set to `1000ms`.

To change the animation of transiton, you can use `ease()`. Default value is `cubic-in-out`. It is proper to add this function *after* `transition()`. Other animations are:

- `linear`: `ease('linear')`

- `circle`

- `elastic`

- `bounce`

`delay()` can be set to define when to start transition. You can pass a certain value, or a function to it, such as `.delay(function(d,i){ return i*1000;});`. This will make the animation of last element later than previous element, by 1s.

	:::javascript
	//...
	.transition()
	.delay(function(d,i){
		return i/dataset.lenght*1000;
		//This will make i ratioly to dataset, then times 1000. Total time not change, time for each element is different.
	})

`each()` can be used to add opeartion when transition start or end. each accepts two parameters:

- `start` or `end`. You can use `this` to get current element.

- a function that will run when start or end transition

Element can only have *one* transition animation at any time. So you *can not* add more `transition()` in a `each('start',function(){...})`. But you *can* do this in `each('end',function(){...}`.

	:::javascript
	.each('end',fucntion(){
		d3.select(this) //Select current single element
			.transition() //You can not add this in start function
			.attr('fill',red);
	});

	//you can also do .each(function(d,i){...})

You can do continues transition in 3.0 version:

	:::javascript
	//...
	.transition()
	.attr('cx',function(d){
		return xScale(d[0]);
	})
	.attr('cy',fuction(d){
		return yScle(d[1]);
	})
	.transition()
	.attr('fill','yellow');

##Clip-Path

`clipPath()` can create an `area`, so that only when element's part is *inside* this area, this part can be seen. Steps are:

- Define `clipPath` and give it an id.

- Put a visible element in `clipPath`, such as `rect` or `circle`

- Add a reference to `clipPath` on the element that use `clipPath`

>
	:::javascript
	//Define clipPath
	svg.append('clipPath')
		.attr('id','chart-area')
		.append('rect') //Make this clipPath to a rectange
		.attr('x',padding)
		.attr('y',padding)
		.attr('width',w-padding*3)
		.attr('height',h-padding*2);

	//Create circle
	svg.append('g') //create new g element and set id
		.attr('id','circles')
		.attr('clip-path','url(#chare-area)') //add reference to clipPath
		.selectAll('circle')
		.data(dataset)
		.enter()
		.append('circle')
		...

	//Now all circle elements has been wrapped in a group, this group has a reference to a rectange that has size of all svg.
	//If any circle is out of this rectangle, the out part will be cut.

##Add or Remove Element

To *add new* rectangle(or other elments), re-select and re-append `rects`, then after `enter()`, use `attr('x',w)` to make the new bar to right most right of svg, so no one can see it. The use `transition().attr('x',...).attr('y',...).attr('width',...).attr('height',...)` to make it in with animation. Now new element will be on *right* of old elements.

To *delete* existing element, using `exit()`. You can firstly remove *first* element from dataset by using `dataset.shift()`, then do:

	:::javascript
	bars.exit().transition()
				.attr('x',w)
				.remove(); //remove last element from DOM

	//You should update tags if you have any

##Key-Value Pair Dataset

D3 has `index` with each value in dataset automatically. However, you may needs to define your own `key` when you need. You can define `key-value` pair in dataset if you need:

	:::javascript
	var dataset = [{key:'apple',value:1},
					{key: 1, value: 200}];
	// {} define object
	// [] define array

Now you need to use `d3.value` to access value. You can set `var key = function(d){ return d.key;}` for future usage, the use `.data(dataset,key)` to assign dataset.

Now to let the *left most* bar remove from *left*, use `.exit().transition().attr('x',-xScale.rangeBand()`.

##Code Example For This Chapter

You can check the interative version from <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-V.html">**here**</a>.

	:::javascript
	//Code Part I: Transition Animation

	//set up random data set
	var dataset = [];
	    var maxValue = 80;
	    for(var count = 0; count<10; count++){
	    	var value = Math.round(Math.random()*maxValue);
	    	var key = Math.round(Math.random()*count*10);;
	    	var pair = {};
	    	pair.key = key;
	    	pair.value = value;
	    	dataset.push(pair);
	    }

	var key = function(d){
		return d.key;
	}
	//set up svg
	var h = 400;
	var padding = 5;

	var svg = d3.select(document.getElementById('chapter9').getElementsByClassName('1')[0]).append('svg')
		.attr('width','100%')
		.attr('height',h);

	var w = document.getElementsByTagName('svg')[0].offsetWidth;

	//set up ordinal scale
	var xScale = d3.scale.ordinal()
				.domain(d3.range(dataset.length))
				//return an array that has same length as dataset. Here should be 0,1,...,9
				.rangeRoundBands([0,w],0.05);
				//Banding: d3 will calculate from 0 to w, how many bands it can be divided. And we set the gap between each band is 5%. We use rangRoundBands to get integer value.

	var yScale = d3.scale.linear()
					.domain([0, d3.max(dataset, function(d){return d.value;})])
					.range([h-padding,0]);

	//Create Ractangular
	svg.selectAll('rect').data(dataset).enter().append('rect')
		.attr('x',function(d,i) {
			return xScale(i); //using x scale, set up i, which is the corresonding index 0,1,...10 for d.
		})
		.attr('y',function(d){
			return yScale(d.value); //y's position should be the same as before
		})
		.attr('width', xScale.rangeBand())//now d3 will automatically set up width of each bar, based on xScale
		.attr('height', function(d){
			return h-yScale(d.value); //height needs to following scale first, then using height minus
		})
		.attr('fill',function(d){
		return 'rgb(120,233,' + Math.round(d.value/8*50) + ')';
	});

	//Add Tag
	var text = svg.selectAll('text').data(dataset).enter().append('text');
	text.text(function (d){
		return d.value;
	});
	text.attr('x',function(d,i){
		return xScale(i)+xScale.rangeBand()/2;
	}).attr('y',function(d){
		return yScale(d.value) + padding*3;
	}).attr('fill', 'pink');

	//set up axis
	var xAxis = d3.svg.axis()
    				.scale(xScale)
    				.orient('top')
    				.ticks(10)
    var yAxis = d3.svg.axis()
    				.scale(yScale)
    				.orient('right')
    				.ticks(10);

	svg.append('g').attr('class','axis xaxis')
		.attr('transform','translate(0,'+(h-padding) + ')')
    	.call(xAxis);
    svg.append('g').attr('class','axis yaxis')
    	.attr('transform','translate(' + padding + ',0)')
    	.call(yAxis);


    //Add Trigger Event for Button
    d3.select(document.getElementById('btn')).on('click',function(){
    	//Note: we now have new dataset
	    var dataset2 = [];
	    var maxValue = 80;
	    for(var count = 0; count<dataset.length; count++){
	    	var value = Math.round(Math.random()*maxValue);
	    	var key = count;
	    	var pair = {};
	    	pair.key = key;
	    	pair.value = value;
	    	dataset2.push(pair);
	    }

		//update yScale to make sure y axis will change. If you change size of new dataset, you need to update x scale also!
		yScale.domain([0, d3.max(dataset2, function(d){return d.value})]);

    	//update rectange
    	svg.selectAll('rect').data(dataset2)
    		.transition() //add transition animation
    		.delay(function(d,i){
    			return i/dataset2.length * 1000;  //delay time: make each bar's animation later than previous one, proporationaly. So last one will delay 1000ms, last two will delay less than 1000ms, etc
     		})
    		.duration(1000) //add duration of anitmation: 1000 ms
    		.each('start',function(){
    			d3.select(this).attr('stroke','black'); //for each item, do this at the start of animation. Note you can not add another transition() here. If so current transition will be interrupt
    		})
    		.attr('x',function(d,i){
    			return xScale(i);
    		})
    		.attr('y',function(d){
    			return yScale(d.value);
    		})
    		.attr('height', function(d){
    			return h-yScale(d.value);
    		}).attr('fill', function(d){
				return 'rgb(120,100,' + d.value*10 + ')';
			})
			.transition()
			.duration(2000)
			.attr('fill','grey'); //Since previous transition has done, You can add another transition() here.This one will not interrupt privous transition


	    //update tag
	    svg.selectAll('text').data(dataset2)
	    	.transition() //add transition animation
    		.duration(2500) //add duration of anitmation: 5000 ms
	    		.text(function(d){
	    			return d.value;
	    		})
	    		.attr('x',function(d,i){
	    		return xScale(i)+xScale.rangeBand()/2;
	    		})
	    		.attr('y',function(d){
	    		return yScale(d.value) + padding*3; //in y axis. if you add a position number, it will go down.
	    		});

	    //Update Axis
	    svg.select(".xaxis").transition().duration(1000).call(xAxis);
	    svg.select('.yaxis').transition().duration(1000).call(yAxis);

    });

	    //Code Part II: Add Or Remove Element

	    d3.select(document.getElementById('add')).on('click',function(){

	    /*add a new element to dataset
	    var maxValue = 50;
	    var newNumber = Math.round(Math.random() * maxValue);
	    dataset.push(newNumber);
	    */

	    var maxValue = 50;
	    var minValue = 30;
	    	var pair = {};
	    	pair.key = Math.round(Math.random()*minValue);
	    	pair.value = Math.round(Math.random()*maxValue);
	    	dataset.push(pair);

	    //Update xScale since dataset change its length and max may need to change
	    var xScale = d3.scale.ordinal()
				.domain(d3.range(dataset.length))
				.rangeRoundBands([0,w],0.05);
		var yScale = d3.scale.linear()
					.domain([0, d3.max(dataset, function(d){return d.value;})])
					.range([h-padding,0]);

	    //re-select all rectangulars and create new bar element
	    var bars = svg.selectAll('rect').data(dataset);
	    bars.enter() //get new elements. Note: add transition() here will cause error
	    	.append('rect') //use append() to create this new element
 	    	.attr('x', w) //re-define width
	    	.attr('y',function(d){
	    		return yScale(d.value);
	    	})
	    	.attr('width',xScale.rangeBand())
	    	.attr('height', function(d){
	    		return h-yScale(d.value);
	    	})
	    	.attr('fill',function(d){
	    		return 'rgb(50,150,' + d.value*20 + ')';
	    	});

	    //Update attributes of new bar element
	    svg.selectAll('rect')
	    		.attr('x',function(d,i){
	    		return xScale(i);
	    	}).attr('y',function(d){
	    		return yScale(d.value) + padding*3;
	    	}).attr('width', xScale.rangeBand())
	    	.attr('height',function(d){
	    		return h-yScale(d.value);
	    	});

	   //re-update tags
	   var text = svg.selectAll('text').data(dataset,key).transition(); //note we don't need enter() and append() here because there is no new element
	   text.text(function(d){
	   	return d.value;
	   });
	   text.attr('x',function(d,i){
	   	return xScale(i) + xScale.rangeBand()/2;
	   }).attr('y',function(d){
	   	return yScale(d.value) + padding*3;
	   }).attr('fill','black');
	});

	//Remove a Bar from right
	d3.select(document.getElementById('remove')).on('click',function(){
		dataset.shift();//remove the first element from dataset.

		var bars = svg.selectAll('rect').data(dataset,key); //note you add key here to make sure key is self-defined, instead of default index
		bars.exit() //Returns the exit selection: existing DOM elements in the current selection for which no new data element was found
			.transition()
			.duration(1000)
			.attr('x', -xScale.rangeBand()) //remove from left
			.remove(); //remove the elements in the current selection fromt the current document

		//update tags
	    var text = svg.selectAll('text').data(dataset,key);
	   			  text.text(function(d,i){
				   	return d.value;
				   });
				   text.attr('x',function(d,i){
				   	return xScale(i) + xScale.rangeBand()/2; //after remove, i still start from 0. However the key now start from second element
				   }).attr('y',function(d){
				   	return yScale(d.value) + padding*3;
				   }).attr('fill','orange');
	});











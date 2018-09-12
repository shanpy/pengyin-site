.. title: Reading Notes for D3.js Part VII (Chapter 11)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-11
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part VII (Chapter 11)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 11 : Layout

code example for Chapter 11 is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-VII.html">**here**</a>.

All Layouts for D3 are:

- `Bundle`: assign `Holten` algorithem to `edge`

- `Chord`: generate `chord diagram`

- `Cluster`: generate `dendrogram`

- `Force`: generate and assign `nodes` following physics

- `Hierarchy`: there are sevel layer in chart. Each chart inherience layout from previous layer

- `Histogram`: generate `histogram`

- `Pack`: generate layout based on `circle packing`

- `Partition`: generate adjacency diagrams: a space-filling variant of a node-link tree diagram

- `Pie`: generate pie chart

- `Stack`: generate base line for a series of bars

- `Tree`: generate tree chart

- `Treemap`: generate a group of rectangles. Each reactangles size is based on radio of data.

##Pie Chart

Step one: given a dataset(array of numbers), you can use `var pie = d3.layout.pie()` to convert this dataset to a *new* dataset with numbers ready for pie chart.

Step two: you can use `d3.svg.arc()` to create `arc` for pie chart. This function will generate a `path` variable, which can draw any shape in SVG:

	:::javascript
	var outRadius = h/2;
	//If h is smaller, make outter radius to h/2 so center will be at the center of height
	var inRadius = 0;
	var arc = d3.svg.arc()
					.innerRadius(inRadius)
					//set the inner radius of arc to 0 so that they can all center a point. You can also set to other value if you need
					.outerRadius(outRadius);

Step 3: create new group and make arcs in this group to comine a pie chart. Then add `path` element to store arcs data and generate shape:

	:::javascript
	//After code above

	var arcs = svg.selectAll('g.arc') //This is the way to wrap elements to group when creating elements!
				.data(pie(dataset)) //Or you can use d3.layout.pie(dataset) to convert original dataset
				.enter()
				.append('g') //you only append g here
				.attr('class','arc') //create class for easier usage
				.attr('transform','translate('+outRadius+', '+outRadius+')');
				//This step move arcs to certain position for pie chart


	//A color function to call default ten d3 colors
	var color = d3.scale.category10();


	//Now add path to generate shape
	arcs.append('path')
		.attr('fill',function(d,i){
		return color(i); //d3 will automatically find d and i based on dataset
		})
		.attr('d',arc); //Assign arc created by arc() function

	//Add Tags for this pie chart
		arcs.append('text').attr('transform',function(d){
			return "translate(" + arc.centroid(d) + ')';  //centroid is the center point of any shape. Here means move tag to center of shape
		}).attr('text-anchor','middle')
		.text(function(d){
			return d.value; //Use d.value here because new dataset make d as key-value pair
		});

##Stack Layout

Step 1: Assume you have a dataset which contains objects with attributes, you need to *re-organize* this dataset to objects with `x-y` attribues. `x` is the `ID` value. `y` is the actally value of original data:

	:::javascript
	//Sample Dataset
	var dataset = [
		{apple:25, banana: 50, peach: 150},
		{apple:177, banana: 98, peach: 35},
		{apple: 59, banana: 87, peach: 120}
	];

	//Re-origanize dataset. Each key group become a array. x means index, y is the value
	dataset = [
		[{x:0,y:25}, {x:1,y:177}, {x:2,y:59}], //apple group
		[{x:0,y:50}, {x:1,y:98}, {x:2,y:87}], //banana group
		[{x:0,y:150}, {x:1,y:35}, {x:2,y:120}] //peach group
	];

Step 2: similar to pie chart, use `d3.layout.stack(dataset)` to re-generate dataset. Note this will generate a `y0` value as *baseline* for each object, which equals to the *total* of all `y` value for its previous object / the minimum y-position of the value:
images/posts/stack chart data.png 

Step 3: Assign `x`,`y`,`width`,`height` attribute to each rect. You need to use `d.y0` and `d.y` for `y` and `height`:

	:::javascript
	var rects = groups.selectAll('rect').data(function(d){
		return d;
	}).enter().append('rect')
	.attr('x', function(d,i){
		return xScale(i);
	})
	.attr('y',function(d,i){
		return d.y0;
	})
	.attr('height',function(d,i){
		return yScale(d.y);
	})
	.attr('width',xScale.rangeBand())
	.attr('fill',function(d,i){
		return color(d.y0);
	})
	.attr('stroke','black');

	//This will create a bar chart with three columns, which are the three objects in original dataset

	//Each column will have three ractangle, representing three attributes for each object in original dataset

##Force Directed Layout

This layout is *dragable* by user, and the chart will move following physic role. This layout use `graph`, which is combined by `node` and `edge`.

Step 1: This layout needs special dataset which defining `nodes` and `edges` object. `nodes` has `name` attribute. `edges` has `source` and `target` and `weight` attributes, which defines the *from* and *to* attribute for each edge, with *line weight*:

	:::javascript
	var dataset = {
		nodes: [
			{name: 'apple'}, //name of nodes
			{name: 'peach'},
			{name: 'banana'},
			{name: 'pear'},
			{name: 'pineapple'}
		],
		edges: [
			{source:0, target:1, weight:1}, //edges linking nodes.Has a source and a target
			{source:1, target:2, weight:2},
			{source:2, target:3, weight:3},
			{source:3, target:4, weight:4},
			{source:4, target:2, weight:5}
			//Important: make sure last source connect back to existing source!
		]
	};

Step 2: Using `d3.layout.force()` to initailize dataset. You need to set `.nodes()` and `.links()` with data in dataset, then set `size` of how far user can drag. Use `start()` to finish initialization:

	:::javascript
	//Initialize force-directed graph
	var force = d3.layout.force()
						.nodes(dataset.nodes)
						.links(dataset.edges)
						.size([w,h])
						.linkDistance([50]) //distance between each node
						.charge([-100]) //how much nodes wanting to escape from each other
						.start();

Step 3: Set attributes for `nodes` and `ages`. At the ends of `nodes` attribute, make sure use `.call(force.drage)` to enable the ability of dragging.

	:::javascript
	//Create line to connecting nodes
	var edges = svg.selectAll('line')
					.data(dataset.edges)
					.enter()
					.append('line')
					.style('stroke','black')
					.style('stroke-width',function(d){
						return d.weight;
					});

	//Create circle as nodes
	var color = d3.scale.category10();

	var nodes = svg.selectAll('circle')
					.data(dataset.nodes)
					.enter()
					.append('circle')
					.attr('fill',function(d,i){
						return color(i);
					})
					.attr('r', 5)
					.call(force.drag);		//start the function to drag circles.

Step 4: Define what is going to happen in `tick`, which means define the behavior of chart when a time frame pass by. Here we want for each time frame, chart will update nodes and edges:

	:::javascript
	//Define tick: what is going to happen for each time second
	force.on('tick',function(){
		edges.attr('x1',function(d){
			return d.source.x; //x1 of edge to be x of source
		}).attr('y1',function(d){
			return d.source.y //y1 of edge to be y of source
		}).attr('x2',function(d){
			return d.target.x;
		}).attr('y2',function(d){
			return d.target.y;
		});

		nodes.attr('cx',function(d){
			return d.x;
		}).attr('cy',function(d){
			return d.y;
		})
	})

##Code for This Chapter

An interacive version is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-VII.html">**here**</a>.

	:::html

	//Part I Code

	//create random dataset
	var numberOfData = 10;
	var dataset = [];
	for(var i=1; i<numberOfData; i++){
		dataset.push(Math.round(Math.random()*i*30));
	}


	//create svg
	var h= 300;
	var padding = 5;
	var svg = d3.select(document.getElementById('chapter11').getElementsByClassName('1')[0]).append('svg').attr('height',h).attr('width','100%');
	var w = document.getElementsByTagName('svg')[0].offsetWidth;

	//Get pie value data from d3.layout.pie function
	var pie = d3.layout.pie();
	dataset = pie(dataset);

	//create pie chart based on new dataset. Use d3.svg.arc() and path to create arc
	var outRadius = h/2;
	var inRadius = 0;
	var arc = d3.svg.arc().innerRadius(inRadius).outerRadius(outRadius); //assign two radius to arc

	//Put arcs to group, and binding data
	var arcs = svg.selectAll('g.arc') //This is how to add class elements to a group
					.data(dataset)
					.enter()
					.append('g')
					.attr('class','arc')
					.attr('transform','translate(' + outRadius + ', ' + outRadius + ')');
					//transform to right with outRadius value, transform to button with outRadius value

	//Add path element and put arc to it
	arcs.append('path')
		.attr('fill',function (d) {
			return 'rgb(100,' + Math.round(d.value) + ",200)"; //You need to use d.value here because data source now is pie.
		}).attr('d',arc);

	//Add Tags for this pie chart
	arcs.append('text').attr('transform',function(d){
		return "translate(" + arc.centroid(d) + ')';  //centroid is the center point of any shape. Here means move tag to center of shape
	}).attr('text-anchor','middle')
	.text(function(d){
		return d.value;
	});

	</script>

	<!--Part II Code-->
	<script type="text/javascript">
	//Sample Dataset
	var dataset = [
		{apple:25, banana: 50, peach: 150},
		{apple:177, banana: 98, peach: 35},
		{apple: 59, banana: 87, peach: 120}
	];

	//Re-origanize dataset. Each key group become a array. x means index, y is the value
	dataset = [
		[{x:0,y:25}, {x:1,y:177}, {x:2,y:59}], //apple group
		[{x:0,y:50}, {x:1,y:98}, {x:2,y:87}], //banana group
		[{x:0,y:150}, {x:1,y:35}, {x:2,y:120}] //peach group
	];

	//Use d3.layout.stack() to modify dataset
	var stack = d3.layout.stack();
	stack(dataset);

	//create svg
	var h = 500;
	var padding = 5;
	var svg = d3.select(document.getElementById('chapter11').getElementsByClassName('2')[0]).append('svg').attr('width','100%').attr('height',h);
	var w = document.getElementsByTagName('svg')[1].offsetWidth;

	//create scale
	var xScale = d3.scale.ordinal()
				.domain(d3.range(dataset.length))
				.rangeRoundBands([0,w],0.05);
	var yScale = d3.scale.linear()
					.domain([0, d3.max(dataset,function(d){
						return d3.max(d,function(d,i){
							return d.y + d.y0;
						});
					})])
					.range([h-padding,0]);

	//Add a group for each row of data
	var groups = svg.selectAll('g').data(dataset).enter().append('g').attr('class','group');

	//Add bar chart
	var color = d3.scale.category10();

	var rects = groups.selectAll('rect').data(function(d){
		return d;
	}).enter().append('rect')
	.attr('x', function(d,i){
		window.console.log("x: " + xScale(i) + " y: " + d.y + " y0: " + d.y0);
		return xScale(i);
	})
	.attr('y',function(d,i){
		return h-d.y0;
	})
	.attr('height',function(d,i){
		return yScale(d.y);
	})
	.attr('width',xScale.rangeBand())
	.attr('fill',function(d,i){
		return color(Math.round(d.y)/10);
	})
	.attr('stroke','black');

	//add tags
	var text = groups.selectAll('text').data(function(d){
		return d;
	}).enter().append('text');
	text.text(function(d,i){
		return d.y;
	});
	text.attr('x',function(d,i){
		return xScale(i) + xScale.rangeBand()/2;
	}).attr('y',function(d,i){
		return h-d.y0-padding;
	}).attr('fill', 'blue');;
	</script>

	<!--Part III Code-->
	<script type="text/javascript">
	//data should be a group, contains a nodes array group and an edges arraygroup
	var dataset = {
		nodes: [
			{name: 'apple'}, //name of nodes
			{name: 'peach'},
			{name: 'banana'},
			{name: 'pear'},
			{name: 'pineapple'}
		],
		edges: [
			{source:0, target:1, weight:1}, //edges linking nodes.Has a source and a target
			{source:1, target:2, weight:2},
			{source:2, target:3, weight:3},
			{source:3, target:4, weight:4},
			{source:4, target:2, weight:5}
			//Important: make sure last source connect back to existing source!
		]
	};


	//create svg
	var h=300;
	var padding=5;
	var svg = d3.select(document.getElementById('chapter11').getElementsByClassName('3')[0]).append('svg').attr('width','100%').attr('height',h);
	var w = document.getElementsByTagName('svg')[2].offsetWidth;

	//Initialize force-directed graph
	var force = d3.layout.force()
					.nodes(dataset.nodes)
					.links(dataset.edges)
					.size([w,h])
					.linkDistance([50]) //distance between each node
					.charge([-100]) //how much nodes wanting to escape from each other
					.start();

	//Create line to connecting nodes
	var edges = svg.selectAll('line')
					.data(dataset.edges)
					.enter()
					.append('line')
					.style('stroke','black')
					.style('stroke-width',function(d){
						return d.weight;
					});

	//Create circle as nodes
	var color = d3.scale.category10();

	var nodes = svg.selectAll('circle')
					.data(dataset.nodes)
					.enter()
					.append('circle')
					.attr('fill',function(d,i){
						return color(i);
					})
					.attr('r', 5)
					.call(force.drag);		//start the function to drag circles.

	//Define tick: what is going to happen for each time second
	force.on('tick',function(){
		edges.attr('x1',function(d){
			return d.source.x; //x1 of edge to be x of source
		}).attr('y1',function(d){
			return d.source.y //y1 of edge to be y of source
		}).attr('x2',function(d){
			return d.target.x;
		}).attr('y2',function(d){
			return d.target.y;
		});

		nodes.attr('cx',function(d){
			return d.x;
		}).attr('cy',function(d){
			return d.y;
		})
	})












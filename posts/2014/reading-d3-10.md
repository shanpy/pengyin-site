.. title: Reading Notes for D3.js Part VI (Chapter 10)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-10
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part VI (Chapter 10)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's importa

#Chapter 10 : Interactive Design

code example for this chapter is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-VI.html">**here**</a>. This part involves lots of code practice.

To add transition to element using `css`:

	:::css
	rect:hover {
		transition: all 0.3s;
		-moz-transition: all 0.3s;
		-o-transition: all 0.3s;
		-webkit-transition: all 0.3s;
	}

We can do same thing using `javascript`: `.on('mouseover',function(){...}`; In function, we can use `d3.select(this).attr()` to adjust attribute of elements. Using `.on('mouseout',function(){...}` to make sure when moving mouse out, the effect disappears.

Note: It is the best to set *hover* effect in `css`, and set other complex effect to `javascript`.

`pointer-events: none;` can be used to let css *ingore* mouse event for certain element. `.style('pointer-events','none')` can achieve same effect.

##Sort Bar

	:::javascript
	var sortBars = function(){
		svg.selectAll('rect')
			.sort(function(a,b){
				return d3.ascending(a,b); //can also do decending
			})
			.transition()
			.attr('x',function(d,i){
				return xScale(i);
			})
	}

In the code above, `sort` needs to know which is front, which is next, so we need to pass it two parameters, and using `ascending()` to give a order. Now each element in dataset will be compared and sorted.

##Tool Tip

If you want to use *default* tooltip setting by browser, just add `.append('title').text(function(d){...});` after appending elements.

You can also set *SVG* tooltip. First, re-set `x` and `y`, then append `text` to element:

	:::javascript
	.on('mouseover',function(d){
		var xPosition = parseFloat(d3.select(this).attr('x')) + xScale.randBand()/2;
		//make tooltip x position to current x plus half of bar width
		var yPosition = parseFloat(d3.select(this).attr('y')) + 14; //make y go down

		svg.append('text')
			.attr('id','tooltip') //Assign id for easy remove
			.attr('x',xPostion)
			.attr('y',yPosition)
			.attr('text-anchor','middle') //In svg, this is used to align text
			.attr('fill','black')
			.text(d);

		//We can remove tooltip by d3.select('#tooltip').remove();
	});

*HTML* tooltip can make tooltip out of svg, which is better in some case. You can make it using `html` or `javascript`.

	:::html
	<div id="tooltip" class="hidden">  <!--hidden class can hide this element-->
		<p><strong>Label Heading</strong></p>
		<p><strong id="value">100</strong></p>
	</div>

	<style type="text/css">
		#tooltip{
			position: absolute; //This is important
			width: 299px;
			height: auto;
			padding: 10px;
			background-color: white;
			//...
			pointer-events:none;
		}
		#tooltip.hidden{
			display: none;
		}
		#tooltip p{
			margin: 0;
			//...
		}
	</style>

	<script type="text/javascript">
		//re-set xPosition and yPosition as code above

		//on mouse over
		d3.select('#tooltip')
			.style('left', xPosition + "px")
			.style('top', yPosition + 'px')
			.select('#value')
			.text(d);

		d3.select('#tooltip').classed('hidden',false); //show tooltip


		//on mouse out
		d3.select('#tooltip').classed('hidden',true);
	</script>

##Code for This Chapter

You can view interative version <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-VI.html">**here**</a>.

	:::html
	<style type="text/css">
			rect:hover{
				fill:orange;
				-moz-transition: all 0.3s;
				-o-transition: all 0.3s;
				-webkit-transition: all 0.3s;
				transition: all 0.3s;
			}

			#tooltip{
				position: absolute;
				width: 10em;
				height: auto;
				padding: 1em;
				background-color: white;
				-webkit-border-radius: 5px;
				-mox-border-radius: 5px;
				border-radius: 5px;
				-webkit-box-shadow: 3px 3px 3px rgba(0,0,0,0.5);
				-moz-box-shadow: 3px 3px 3px rgba(0,0,0,0.5);
				box-shadow: 3px 3px 3px rgba(0,0,0,0.5);
				pointer-events:none;
			}

			#tooltip.hidden{
				display: none;
			}

			#tooltip p{
				margin: 0;
			}
	</style>

	<script type="text/javascript">
		//create key-value pair dataset
		var dataset = [];
		var base1 = 80;
		var base2 = 50;
		for(var count=0;count<10;count++){
			var pair = {};
			pair.value = Math.round(Math.random()*base1);
			pair.key = Math.round(Math.random()*base2);
			dataset.push(pair);
		}

		//set up svg
		var h = 400;
		var padding = 5;
		var svg = d3.select(document.getElementById('chapter10').getElementsByClassName('1')[0]			).append('svg')
					.attr('width','100%')
					.attr('height',h);
		var w = document.getElementsByTagName('svg')[0].offsetWidth;

		//set up scale
		var xScale = d3.scale.ordinal()
						.domain(d3.range(dataset.length))
						.rangeRoundBands([0,w],0.05);
		var yScale = d3.scale.linear()
						.domain([0,d3.max(dataset,function(d){
							return d.value;
						})])
						.range([h-padding,0]);

		//set up bar chart
		var rect = svg.selectAll('rect').data(dataset).enter().append('rect')
						.attr('x', function(d,i){
							return xScale(i);
						})
						.attr('y', function(d){
							return yScale(d.value) - padding;
						})
						.attr('width',function(d,i){
							return xScale.rangeBand();
						})
						.attr('height',function(d){
							return h-yScale(d.value);
						})
						.attr('fill',function(d){
							return "rgb(120,150," + d.value*5 + ')';
						});
		rect.on('click', function(){
							sortBars(); //add a clickable function to it, sorting
						});

		//set up tags
		var text = svg.selectAll('text').data(dataset).enter().append('text');
		text.text(function(d){
			return d.value;
		});
		text.attr('x',function(d,i){
			return xScale(i) + xScale.rangeBand()/2;
		}).attr('y',function(d){
			return yScale(d.value)+padding*3;
		}).attr('fill','black')
		.attr('class','tags');	//add class for easier sorting


		//set up axis. Note if axis should be added as last step, otherwise it will mess up tags, and be covered by bars
		var xAxis = d3.svg.axis()
						.scale(xScale)
						.orient('top')
						.ticks(10);
		var yAxis = d3.svg.axis()
						.scale(yScale)
						.orient('right')
						.ticks(10);
		svg.append('g').attr('class','axis xaxis').attr('transform','translate(0,'+(h-padding)+')').call(xAxis);
		svg.append('g').attr('class','axis yaxis').attr('transform','translate('+padding/2+')').call(yAxis);


		//sortBar method
		var sortBars = function(){
				//sort rect
			 svg.selectAll('rect')
				.sort(function(a,b){
					//Important: Use a.value here if your dataset is key/value pair!
					return d3.ascending(a.value,b.value); //if pass two parameter a,b, sort them using ascending order
				}) //default is ascending order
				.transition()
				.duration(500)
				.attr('x',function(d,i){
					return xScale(i); //after sort, re-asign x value
				}).attr('fill',function(d){
							return "rgb(200,150," + d.value*5 + ')';
						});

				//sort tags
				svg.selectAll(".tags")//selectAll for class name in D3
					.sort(function(a,b){
						return d3.ascending(a.value,b.value);
					}).transition()
					.duration(500)
					.attr('x',function(d,i){
						return xScale(i) + xScale.rangeBand()/2; //after sort, re-asign x value
					}).attr('fill',function(d){
								return 'blue';
							});
		}


		//Add HTML Reminder
		rect.on('mouseover',function(d){
			//get reminder's x and y value

			//get current current x value and add rangeBand
			var xPosition = parseFloat(d3.select(this).attr('x')) + xScale.rangeBand()/2;
			var yPosition = parseFloat(d3.select(this).attr('y')) + h;
			window.console.log(d3.select(this).attr('x') + " " + d3.select(this).attr('y'));

			//create a div to hold reminder. Style for this div is on top
			var newDiv = document.createElement('div');
			newDiv.setAttribute('id','tooltip');
			newDiv.setAttribute('class','hidden');
			newDiv.innerHTML = '<p><strong>Percentage</strong></p><p><span id="value">100</span>%</p>';
			document.getElementById('chapter10').getElementsByClassName('1')[0].appendChild(newDiv);

			//create new reminder
			d3.select('#tooltip').style('left',xPosition + 'px')
								.style('top', yPosition + 'px')
								.select('#value')
								.text(d.value); //select id as value, then assign d.value to it
			//now show tooltip
			d3.select('#tooltip').classed('hidden',false);
		});

		//If mouse move out, hide tooltip
		rect.on('mouseout',function(){
			d3.select('#tooltip').classed('hidden',true); //re-add class by using classed()
		});

	</script>










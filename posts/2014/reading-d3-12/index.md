.. title: Reading Notes for D3.js Part VIII (Chapter 12)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: JavaScript
.. tags: JavaScript, D3.js
.. slug: reading-d3-12
.. authors: Pengyin Shan
.. description: Reading Notes for D3.js Part VIII (Chapter 12)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a Reading Note for *Interactive Data Visualization for the Web - An Introduction to Designing with D3* by *Scott Murray*, pulished by *O'Reilly, 2013*

This post will contains concepts that I think it's important for me to be familiar with in D3 book.

#Chapter 12 : Map

code example for Chapter 12 is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-VIII.html">**here**</a>.

`GeoJSON` is a special format for `JSON`, which is used specially for geography. A typical `GeoJSON` file is an object with two attributes: `type` and `features`. The `features` attibute is an array of objects. Each objects have geography attributes, such as `type`,`id`,`properties`,`geometry`.

`geometry` is a vary useful attributes. It can include `coordinate` attribue, which inludes `longitude,latitude` pairs. Note `longitude` is *vertical* on map, `latitude` is *horizontal* on map. Here is a sample:
images/posts/sampleGeoJSON.png 

Step 1: transfer `GeoJSON` to `SVG path` code by using `d3.geo.path()`. Then load `GeoJSON` file and apply new path:

	:::javascript
	//set a path generator
	var path = d3.geo.path();

	//load map json file. Since this is a callback function, code outside will run the same time as inside
	d3.json('/js/us-states.json',function(json){
		svg.selectAll('path')
			.data(json.features)
			.enter()
			.append('path')
			.attr('d',path); //This line will create a path generator to get all geography data and generate svg path
	});

Step 2: create `projection` to transfer *3D* to *2D*, then use `d3.geo.path().projection()` to apply projection to path. You can also add `scale()` to make map smaller or larger:

	:::javascript
	//Apply scale and Use projection to let map cover all states in US, using a build-in projector albersUsa()
	var projection = d3.geo.albersUsa()
							.translate([w/2,h/2])//Make projection to the center of svg
							.scale([500])//make map smaller. Default value is 1000.
	var path = d3.geo.path().projection(projection); //Apply new projection to current path;

##Use Color to Quantize Map

We can add color with different combination to map to show data difference in map. For example, the place that has more populatio with dark blue and less population with light green, etc.

Step1: create a *quantize* scale with *color* as output. A combination of color can be found in https://github.com/mbostock/d3/tree/master/lib/colorbrewer, from D3 library. Now we output *discreate* value as color. The number of colors decides how precise the map will be. Less color group will make map has less color combination:

	:::javascript
	var color = d3.scale.quantize()
					.range('['rgb(237,248,251)','rgb(204,236,230)','rgb(153,216,201)','rgb(102,194,164)','rgb(44,162,95)','rgb(0,109,44)']');
		//Here we want to devide data to different bucket.

Step2: use `d3.json()` or `d3.csv()` to load data. In data callback function, set up color input domain:

	:::javascript
	d3.json('sample.json',function(data){ //note we use var data to represent data in json file
		color.range(
		[d3.min(data, function(d){return d.value}), d3.max(data, function(d){return d.value;})]
		);
		//Here we get min and max value from data
	});

Step3: load data. We may need to combine data in two json/csv file. To do this, *wrap* another data callback function in current data callback function, then compare column with same data. if it fits, add an attribute in a dataset with the nessiary data from the other dataset. You can use *nested for loop* to compare data:

	:::javascript
	d3.json('1.json',function(data1){

		d3.csv('2.csv',function(data2){ //load another csv file

		for(var i=0; i<data1.attr1.length; i++){ //First for loop for data in json
			var combine1 = data1.attr1[i].data/value/...;

			for(var j=0; j<data2.attr2.length; j++){ //Second for loop for data in csv
				var combine2 = data2.attr2[i].data/value/...;
				if(combine1 == combine2){ //Check if combine 1 and combine 2 has the same data that can be joined
					combine2.attr2[i].newValue = data1.attr1[i].value;
					//Get the data we need from data1 and put it as a new attribute for data2
					break;
					//After find a proper fit, jump out of current for loop and check another value from data1
				}
			}
		}

		})
	})

Step 4: create path and load data to path. You need to do this *inside* a callback loop since we need to use data variable in loop. We need to check if the value in second json/csv exist or not in first json/csv. If not, we need return a single color:

	:::javascript
	svg.selectAll('path')
		.data(data1.attr1)
		.enter()
		.append('path')
		.attr('d','path')
		.style('fill',function(d){
			var value = d.attr1.value; //value that you want to apply color

			if(value) //check exist
			{
				return color(value);
			}else{
				return "grey";
				//if no value, make this part of map as grey.
			}
		})

Step 5: create and add projection. Note you need to do this step *outside* of callback function so that your result will not be affected.

##Add Circle as Data Point on Map

If we have json/csv file that have city names, value, and cities longitude, latitude data, we can make it on map.

Step1, Step2, Step3, Step4: Same as example above.

Step 5: load new data and add circle to map. You need create projection function *before* this step, buy don't apply it to all map. Also, you need to put this part *inside* callback function, so that your circle will not be covered by map since map will be loaded later than outside functions:

	:::javascript
	svg.csv('3.csv',function(data3){
		svg.selectAll('circle')
			.data(data3)
			.enter()
			.append('circle')
			.attr('cx', function(d){
			return projector([d.lon,d.lat])[0];
			//Apply your projector function to the array combined by lon and lat, then get first element as new lon

			}).attr('cy', function(d){
			return projector([d.lon,d.lat])[1];
			//Apply your projector function to the array combined by lon and lat, then get first element as new lat

			}).attr('r',functon(d){
				return Math.sqrt(parseInt(d.attrName)*0.00004);
				//Get the value of the attribute value you want to use, then apply Math.sqrt to get r from coverage size.
			}).attr('fill','yellow')
			.attr('opacity',0.75);
			//You can set up opacity if you want
	})

##Code For This Chapter

code example for Chapter 12 is <a href="http://shanpy.github.io/Front-End-Playground/D3/Reading-D3-VIII.html">**here**</a>.

	:::javascript
	//Part I Code
	function part1(){
	//create svg
	var h = 500;
	var padding = 5;
	var svg = d3.select(document.getElementById('chapter12').getElementsByClassName('1')[0]).append('svg').attr('width','100%').attr('height',h);
	var w = document.getElementsByTagName('svg')[0].offsetWidth;

	//set a path generator
	var path = d3.geo.path();

	//load map json file. Since this is a callback function, code outside will run the same time as inside
	d3.json('/data/us-states.json',function(json){
		svg.selectAll('path')
			.data(json.features)
			.enter()
			.append('path')
			.attr('d',path); //This line will create a path generator to get all geography data and generate svg path
	});

	//Apply scale and Use projection to let map cover all states in US, using a build-in projector albersUsa()
	var projection = d3.geo.albersUsa()
							.translate([w/2,h/2])//Make projection to the center of svg
							.scale([500])//make map smaller. Default value is 1000.
	var path = d3.geo.path().projection(projection); //Apply new projection to current path;
	}


	//Part II Code
	function part2(){
	//Create svg
	var h = 500;
	var padding = 5;
	var svg = d3.select(document.getElementById('chapter12').getElementsByClassName('2')[0]).append('svg').attr('width','100%').attr('height',h);
	var w = document.getElementsByTagName('svg')[0].offsetWidth;


	//Create a scale with different color for quantize map. Here we devide color to 6 groups. You can set your own.
	//Color reference: https://github.com/mbostock/d3/tree/master/lib/colorbrewer
	var colorBrew = ['rgb(237,248,251)','rgb(204,236,230)','rgb(153,216,201)','rgb(102,194,164)','rgb(44,162,95)','rgb(0,109,44)'];
	var color = d3.scale.quantize()
					.range(colorBrew); //We need to wait till data finish loading to add input domain


	//Set up path generator
	var path = d3.geo.path();


	//Load data
	d3.csv('/data/us-ag-productivity-2004.csv',function(data){
		color.domain([
				//set up input domain after data has been loaded
				d3.min(data,function(d){return d.value;}),
				d3.max(data,function(d){return d.value;})
			]);

		//Add csv data to json because we can only bind one group of data to elements.
		//Note you need to do this in d3.csv() because this step rely on csv data
		d3.json('/data/us-states.json',function(json){

			//Mix data in csv file
			for(var i=0; i<data.length; i++){
				var dataState = data[i].state; //get state name in csv file
				var dataValue = parseFloat(data[i].value); //get value in csv file. Note the column of csv file is state and value

				for(var j=0; j<json.features.length; j++){
					var jsonState = json.features[j].properties.name; //Find state name in json file

					if(jsonState == dataState){
						//copy csv value to json file, make a key as value
						json.features[j].properties.value = dataValue;
						//go out for loop. we don't need to check more state in json file.
						break;
					}
				}
			}

			//Now create path and apply data
			svg.selectAll('path')
				.data(json.features)
				.enter()
				.append('path')
				.attr('d', path)
				.style('fill',function(d){
					var value = d.properties.value;
					if(value){ //check if value exist or not
						return color(value);
					}else{
						return "grey";
					}
				});
			});
	});

	//Add Projector
	var projection = d3.geo.albersUsa()
							.translate([w/2,h/2])//Make projection to the center of svg
							.scale([500])//make map smaller. Default value is 1000.
	path.projection(projection);
	}


	//Part III Code
	function part3(){
		//create svg
		var h = 500;
		var padding = 5;
		var svg = d3.select(document.getElementById('chapter12').getElementsByClassName('3')[0]).append('svg').attr('width','100%').attr('height',h);
		var w = document.getElementsByTagName('svg')[0].offsetWidth;

		//create projector
		var proj = d3.geo.albersUsa().translate([w/2,h/2]).scale([500]);

		//create path generator
		var path = d3.geo.path();

		//create color brew
		var colorBrew = ["#ffffd4","#fed98e","#fe9929","#d95f0e","#993404"]; //This time use 5 groups. Color effect will be different from example 2
		var color = d3.scale.quantize().range(colorBrew);

		//load population change.csv file
		d3.csv('/data/us-ag-productivity-2004.csv',function(data){

				//set color input domain
				color.domain(
					[d3.min(data, function(d){return d.value;}),
					 d3.max(data, function(d){return d.value;})]
					);

				//Combine data in csv to data in json
				d3.json('/data/us-states.json', function(data2){
					for(var i=0; i<data.length; i++){
						var dataState = data[i].state;
						var dataValue = parseFloat(data[i].value);

						for(var j=0; j<data2.features.length; j++){
						var data2State = data2.features[j].properties.name;
						if(dataState == data2State){
							data2.features[j].properties.value = dataValue;
							break;
						}
						}
					}



					//Draw map and add color,projector
				svg.selectAll('path').data(data2.features).enter().append('path')
					.attr('d',path).style('fill',function(d){
					var value = d.properties.value; //note since we use data2.features as dataset, here d is equal to data2.features single item
					if(value){
						return color(value);
					}else{
						return "black";
					}
				});

				//load csv data from us cities.csv. Make sure you do this in data callback function so that circle is on top of map. Otherwise circle will be covered by map
				d3.csv('/data/us cities.csv',function(data3){
					//create circle that represetns city, then apply projector to it
					svg.selectAll('circle').data(data3).enter()
						.append('circle')
						//ImportantL proj(lon,lat) will return a array of two
						.attr('cx',function(d){
							return proj([d.lon, d.lat])[0]; //0 postion is longitude
						}).attr('cy',function(d){
							return proj([d.lon, d.lat])[1]; //1 position is latitude.
						}).attr('r',function(d){
							return Math.sqrt(parseInt(d.population) * 0.00004); //use sqrt to get r from coverage of population
						}).attr('fill','green')
						.attr('opacity',0.75);
				});
				});
		});

				//apply projector
				path.projection(proj);
				//Important! When you use projection for full map(i.e, all paths), you must do this out side data callback function!


		}








.. title: Reading Note - Asynchronous in jQuery and ECMAScript 6
.. date: 2016-05-17
.. category: JavaScript
.. tags: JavaScript, jQuery
.. slug: reading_note_defer_in_jquery
.. authors: Pengyin Shan
.. description: Recently I encountered a problem in my project: I need to load around 1,500 records from API and fill them in table. I tried to parse data and append them to DOM tree. While desktop browser working well, mobile browser had around 3 seconds freezing effect. To solve this problem, asynchronous in JS/jQuery will be useful. I read a few articles and wrote this blog post for future reference.




#Reference List

This is a **reading note** for following articles/blogs:

- <a href="https://github.com/shanpy/shanpy.github.io.git"></a>, written by Julian Aubourg and Addy Osmani.

- <a href="https://api.jquery.com/category/deferred-object/">jQuery API</a> and <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise">Promise in MSDN</a>

- (Chinese) <a href="http://es6.ruanyifeng.com/#docs/generator">Entry of ECMA6</a>, from Yifeng Ran

- (Chinese) blog of <a href="http://www.cnblogs.com/dojo-lzz/p/5495671.html">dojo-lzz</a>

#Promises

`Promises`: a **container** which contains everything that has been deferred.

> If you are creating a Deferred, keep a reference to the Deferred so that it can be resolved or rejected at some point. Return only the Promise object via deferred.promise() so other code can register callbacks or inspect the current state. - jQuery API

A function which returns a promise **will be run** if the condition in this function is satisfied, no matter if it is a successfully satisfied case or a failure case. i.e. a **fulfilled** promise can be two states: `resolved`(successfully passing data) or `rejected` (something is wrong).

##promise.then

`them` method is used to handle the case the future result is available (resolved or rejected). It accepts two parameters, which can be functions. One for successful case. One for failed case. Following is the example:

	#!javascript
	var promise = someFunction(arg1, arg2, ...);
	promise.then(function(futurevalue){
			/*Handle successfully passed futurevalue*/
		},function(){
			/*Handle cases with error*/
		}
	);

##promise and when method

`$.when` is used to perform action after all promises have been satisfied. For example:

	#!javascript
	when(
		function(){
			/*animation 1*/
			/*return promise 1*/
			},
		function(){
			/*animation 2*/
			/*return promise 2*/
		}
	).then(function(){
			/*Handle events after both promises are satisfied*/
		});

##Promise in ECMAScript 6

*Remember to check browser capability before using promise JS object*

ECMAScript 6 also have `Promise` object, which can be used for deferred operations. Similar as promise in jQuery, Promise object in JS has three states: `pending` (initial), `fulfilled`, `rejected`.


##Generator in ECMAScript 6

ECMAScript 6 has a `Generator` function, which provides possibility of lazy-loading.

Generator is a function which generates a Iterator. The iterator iterates every `yield` statement insider Generator function and **stop** on each `yield` point. After running `.next()` method, iterator will **resume** from last `yield` point.

Generator function has a `*` in function header, which can be put in any position.


`.next()` method will **return** a object with `value` and `done` attributes. `value` has the value which is returned by the last `yield` (breakpoint). `done` has the value which is the status of Generator, `true` means iteration is finished.

**For the last `next()` method, if there is no `return` current function, `value` will be `undefined`. **

A quick example:

	#!javascript
	function* test(){
		yield 'test';
		return 'end';
	}
	var testGenerator = test();
	testGenerator.next(); //Object {value: "test", done:false}
	testGenerator.next(); //Object {value: "end", done:true}
	testGenerator.next(); //Object {value: undefined, done:true}



##Others

I like following problem when I read a Chinese blog article from<a href="http://www.cnblogs.com/dojo-lzz/p/5495671.html">dojo-lzz</a>: if you have red light which is on for every 3 seconds, green light which is on every 1 second and yellow light which is on every 2 seconds, how to make three light switch and on without break? (i.e. red -> green -> yellow -> red -> green -> yellow, etc)


##Deferred in jQuery

`$.Deferred` is used to create new *deferred object*. This deferred object can be used to check if a promise is exist or not, or to accept an optional function which needs to have deferring effect.

> A Deferred object starts in the pending state.  - jQuery API

From jQuery API, the function that is used inside `$.Deferred` is called just before the `$.Deferred` method returns. It accepts the new deferred object as parameter. This parameter represents as both the `this` object and as the first argument to the inner function (the function which needs to be deferred). The function which calling the `$.Deferred` method can attach callbacks using deferred.then(), for example.

I created a <a href="https://jsfiddle.net/shanpy/g7kfqy8o/35/">JSFiddle</a>. The code is following:

	:::javascript
	/*This is a common function, which accepts functions that needs to have deferred effect*/
	$.createCache = function(requestFunction){
	var cache = {};
	  /*
	  callback is optional
	  */
	  return function(key, callback){
	  	callback = function(){
	    	console.log('deferred callback function');
	    }
	  	if(!cache[key]){
	    	cache[key] = $.Deferred(function(defer){
	    	/*
	    	1. As mentioning above, defer is the deferred project
	    	2. requestFunction here is loadImage function below
	    	*/
	      	requestFunction(defer,key);
	      }).promise(); // Return the Promise so caller can't change the Deferred
	    }
	    return cache[key].done(callback);
	  };
	}

	/*Defer is the deferred parameter/object in $.Deferred method above*/
	$.loadImage = $.createCache(function(defer,url){
	  var image = new Image();
	  function cleanup(){
	  	console.log('cleanup in process');
	  	image.onload = image.onerror = null;
	  }
	  /*rejected/resolved/in process*/
	  defer.then(cleanup, cleanup);
	  /*resolved only*/
	  defer.done(function(){
	  	console.log('done');
	  	$('#test').append(image);
	  });
	  image.onload = function(){
	  	/*After image successfully loading, change state to resolve*/
	  	defer.resolve(url);
	  };
	  image.onerror = defer.reject;
	  image.src = url;
	});

	$.loadImage("https://www.gstatic.com/webp/gallery3/1.png").done(function(){
  		console.log('finish loadingImage function');
	  }).fail(function(){
	  	console.log('there is error');
	  })


The output of code above in console is:

	:::javascript
	VM2454:72 cleanup in process
	VM2454:77 done
	VM2454:56 deferred callback function
	VM2522:88 finish loadingImage function

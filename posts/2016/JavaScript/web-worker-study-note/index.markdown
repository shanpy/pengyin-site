.. title: Web Worker Study Note
.. date: 2016-08-17
.. category: JavaScript
.. tags: Web Worker
.. slug: web-worker-study-note
.. authors: Pengyin Shan
.. description: Web worker provides a probabiliy to implement concurrent JavaScript. This is a study note for it.

#Reference List

- <a href="http://www.html5rocks.com/en/tutorials/workers/basics/">The Basics with Web Workers</a> written by *Eric Bidelman*, *www.html5rocks.com*.

- <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers">Using Web Workers</a> by *MDN*

#Basics

Web worker create a extra thread. The JS file running by this work will run through this thread.

There are some special things to be noticed when using web worker:

1. Instead of `window`, the JS file will run in another global context. So make sure using `self` to get current gloabl context in a worker.

2. You cannot directly manipulate DOM inside a web worker. However some items are still available, like `WebSockets` or `IndexedDB`.

The way to communicate between main thread and web worker thread is using `messages`. To send message, use `postMessage()` method. `onmessage` event handler or `message` event listener is used to receive message. Workers may use `XMLHttpRequest` for network I/O.

>During this process, the data passed between main thread and web worker is **copied** instead of shared.

There are two workers: `dedicated worker` and `shared worker`. Dedicated worker is only accessible from the script that first spawned it. Shared worker can be accessed from multiple scripts.

#Dedicated Worker

The best practice is to wrap web worker code in following if loop:

    :::javascript
    if(window.Worker){
        //Add Web Worker Code
    }

Message being sent/received can be a `string/array` or `JSON` object. `JSON` is supported by most modern browers.

##Basics

Basic operations are: **create**, **post and receive message**, **handler errors** and **terminate works**. see code below:

    :::javascript
    //main thread
    var myWorker = new Worker('worker.js'); //Declare new web worker

    myWorker.addEventListener('message', 'onError', function(e){
        console.log(e.data); //main thread response to message from worker.js
    }, false);

    worker.postMessage(['Hello World','hello']); //main thread pass data to worker

    worker.terminate(); //Terminate worker from main thread

    //Error Handle Function. Notice three attributes for error event
    function onError(e){
        console.log(e.message + e.filename + e.lineno);
    }

    :::javascript
    //worker.js
    self.addEventListener('message', function(e){
        self.postMessage(e.data[0]);
        //worker receive data from main thread and return it back. Notice self is used here
    }, false);

    self.close(); //Stop this work from worker thread

Workers can import scripts and use them:

    :::javascript
    importScripts('one.js', 'two.js');

>If execution fails, `NETWORK_ERROR` will be thrown out. However, function declarations after `importScripts()` will still work because they are hoisted.

##Data Passing

When web worker passing data, the data is always serialized on one hand and de-serialized on the other hand.

> Main thread and worker thread **do not share the same instance**, so the end result is **duplicated**.

#Shared Worker

##Basics

Shared worker is accessible by multiple scripts.

Similar to dedicated worker, shared work can be declared by statement like `var myWorker = new SharedWorker("worker.js");`.

##Port

Shared worker communicate via a `port` object. Scripts can communicate with workers in a opened port.

Port can be started by:

1. Use a `onmessage` event handler

2. Instead above if you have a `message` event listener, then use `start()` function to start explicitly.

Example:

    :::javascript
    myWorker.port.start(); //main thread
    port.start();//If a worker thread has port variable, call this line in worker

##Message

For shared worker, `postMessage()` should be used from `port` object:

    :::javascript
    //main.js
    testpart.onchange = function(){
        myWorker.port.postMessage('hello world');
    }
    myWorker.port.onmessage = function(e){
        console.log(e.data);
    }

    //worker.js
    self.addEventListener('connect', function(e){
        var port = e.ports[0]; //Get first port
        port.onmessage = function(e){
            port.postMessage('hello world back');
        }
        //port.start();
        //If onmessage event listener is not used, needs to start port here
    });

#Examples

##Compute in Background

This example is from MDN, counting fibonacii in worker thread:

    :::javascript
    //main.js
    var worker = new Worker("fibonacci.js");

    worker.onmessage = function(event) {
      document.getElementById("result").textContent = event.data;
      dump("Got: " + event.data + "\n");
    };

    worker.onerror = function(error) {
      dump("Worker error: " + error.message + "\n");
      throw error;
    };

    worker.postMessage("5");

    /********************/

    //fobonacii.js
    var results = [];

    function resultReceiver(event) {
      results.push(parseInt(event.data));
      //After result returned, push to results array. This array has two elements: previous result and newly returned item
      if (results.length == 2) {
        postMessage(results[0] + results[1]);
      }
    }

    function errorReceiver(event) {
      throw event.data;
    }

    onmessage = function(event) {
      var n = parseInt(event.data);

      if (n == 0 || n == 1) {
        postMessage(n);
        return;
      }

      /*Recursively create new worker thread and counting 4, 3, 2, 1, then return back to previous worker */
      for (var i = 1; i <= 2; i++) {
        var worker = new Worker("fibonacci.js");
        worker.onmessage = resultReceiver;
        worker.onerror = errorReceiver;

##A very clean/simple example from html5rocks.com

This example cerate clean function to handle difference cases. Functions can be added to attribute of an object to be more organized.

    :::javascript
    //main.js
    function sayHI() {
        worker.postMessage({'cmd': 'start', 'msg': 'Hi'});
      }

      function stop() {
        // Calling worker.terminate() from this script would also stop the worker.
        worker.postMessage({'cmd': 'stop', 'msg': 'Bye'});
      }

      function unknownCmd() {
        worker.postMessage({'cmd': 'foobard', 'msg': '???'});
      }

      var worker = new Worker('doWork2.js');

      worker.addEventListener('message', function(e) {
        document.getElementById('result').textContent = e.data;
      }, false);

      //worker.js
      self.addEventListener('message', function(e) {
          var data = e.data;
          switch (data.cmd) {
            case 'start':
              self.postMessage('WORKER STARTED: ' + data.msg);
              break;
            case 'stop':
              self.postMessage('WORKER STOPPED: ' + data.msg + '. (buttons will no longer work)');
              self.close(); // Terminates the worker.
              break;
            default:
              self.postMessage('Unknown command: ' + data.msg);
          };
        }, false);
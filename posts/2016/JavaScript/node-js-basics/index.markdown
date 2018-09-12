.. title: Node.js Basics
.. date: 2016-05-25
.. category: JavaScript
.. tags: Node.js
.. slug: node-js-basics
.. authors: Pengyin Shan
.. description: Now most JavaScript packages been been integrated to npm. It is time to start exploring node.js and understand the best scansion to apply it.



*This is a reading note for node.js part on <a href="http://www.tutorialspoint.com/nodejs/index.htm">tutorialspoint</a>.*


#Introduction

Node.js (MIT License) is a server-side framework built on Good V8 Engine. From Tutorialpoints.com, it has following features:

- Asynchronous and Event Driven: the server will always move on. Once it gets a notification of a event with returned data, it will trigger this event.

- Single Threaded Model but Highly Scalable: although node.js use a single threaded server, it can response to multiple requests because of its asynchronous feature. It is easy to be scaled.

- Node.js does not buffer any data.

#Components

One node.js application has following three parts:

Import Required Modules: use `require` to import node.js modules. Example: `var http = require("http")`

Create server: user `http.createServer()` to create server instance. This method includes callbacks for response information, such as port number, content-type, etc:

    :::javascript
    var http = require('http');
    http.createServer(function(request, response){
        response.writeHead(200,{'Content-Type': 'text/plain'});
        response.add('Hello World\n'); //add data in response body
    }).listen(8081);//in example use 8081 as port number

Start Server: use `node xxx.js` in terminal to start server. Use name of server js file. Example: `node config.js`.


#NPM

node.js use `npm` (Node Package Manager) to install/control node modules. `npm install package_name [-g] [--save/--save-dev]` can be used to install package (**`--save` or `--save-dev` is used to add dependencies to your package.json file**). There are two way of installation: **Global** and **Local**:

- Local modules are installed inside project, in `node_modules` folder. *Locally deployed packages are accessiable via `require()` method.* Local packages can be listed by `npm ls` command.

- Globally packages are stored in system directory. *It cannot be imported by `require()`*. They can be used in terminal. `npm ls -g` can be used to list global packages.

npm also has following common command:

- `npm uninstall package_name`: uninstall a package

- `npm update package_name`: update a package

- `npm search package_name`: search package name using npm.


##package.json

For project: Run `npm init` at top level of a project can be used to generate `package.json` for **this project**, which is a JSON file defining the property of **this project**.  A few questions will be asked during initialization process.

A `package.json` for project contains `dependencies`, which is for publication pages, and `devDependencies` for dev/test only packages. Following is an example:

    :::javascript
    {
      "name": "test", //name of project
      "version": "1.0.0",
      "description": "",
      "main": "gulpfile.js", //entry point of project
      "scripts": {
        //handle status of project, see https://docs.npmjs.com/misc/scripts for detail
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "author": "test author",
      "license": "ISC",
      //packages and versions for dev/test only
      "devDependencies": {
        "gulp": "^3.9.1"
      },
      //packages and versions for production
      "dependencies": {
        "gulp": "^3.9.1"
      }
    }

For node modules: there is also a package.json file in each node module in `node_modules` folder. Following is the `package.json` file in `gulp-jade` module package:

    :::javascript
    {
      "name": "gulp-jade",
      "version": "1.1.0",
      "description": "Compile Jade templates",
      "keywords": [
        "jade",
        "gulpplugin",
        "stream",
        "compile"
      ],
      "repository": {
        "type": "git",
        "url": "git+https://github.com/phated/gulp-jade.git"
      },
      "author": {
        "name": "Blaine Bublitz",
        "email": "blaine@iceddev.com"
      },
      "dependencies": {
        "gulp-util": "^3.0.2",
        "jade": "1.1 - 1.11",
        "through2": "^2.0.0"
      },
      "files": [
        "index.js",
        "LICENSE"
      ],
      "engines": {
        "node": ">= 0.10"
      },
      "scripts": {
        "test": "gulp jshint && tap ./test"
      },
      "license": "MIT",
      "devDependencies": {
        "gulp": "^3.8.10",
        "tap": "^1.3.1",
        "gulp-jshint": "^1.9.0"
      },
      "gitHead": "671714d09e9ccd291489f22988bbc40fe8db40ec",
      "bugs": {
        "url": "https://github.com/phated/gulp-jade/issues"
      },
      "homepage": "https://github.com/phated/gulp-jade#readme",
      "_id": "gulp-jade@1.1.0",
      "_shasum": "cb2f332ac46824671f36891655c165c591c33bd4",
      "_from": "gulp-jade@latest",
      "_npmVersion": "2.8.3",
      "_nodeVersion": "0.10.36",
      "_npmUser": {
        "name": "phated",
        "email": "blaine@iceddev.com"
      },
      "maintainers": [
        {
          "name": "phated",
          "email": "blaine@iceddev.com"
        }
      ],
      "dist": {
        "shasum": "cb2f332ac46824671f36891655c165c591c33bd4",
        "tarball": "https://registry.npmjs.org/gulp-jade/-/gulp-jade-1.1.0.tgz"
      },
      "directories": {},
      "_resolved": "https://registry.npmjs.org/gulp-jade/-/gulp-jade-1.1.0.tgz",
      "readme": "ERROR: No README data found!"
    }

`npm adduser` to register current user to npm repository, then `npm publish` can be used to publish current module to `repository` address in `package.json`.


#Concurrency: Callback and Events


##Callbacks

JavaScript callback functions are heavily used in node.js to make sure no block exists. Following is an example:

    :::javascript
    //Assume 'input.txt' has one line 'Hello World!'
    var fs = require('fs');
    fs.readFile('input.txt', function(err,data){
        if(err) return console.log(err);
        console.log(data.toString());
    });
    console.log('End Program!');

The code above should output: `End Program! Hello World!`. Program goes till `readFile()` finished, then callback statements will run.

##Events

Node.js use **observer pattern**, which means there exists dependency from one to many. Many observers (i.e. event listeners) will observe one subject (i.e. event). When subjects changes, all observers will be notified and updated based on the update.

> Node thread keeps an event loop and whenever any task get completed, it fires the corresponding event which signals the event listener function to get executed.

Image from tutorialspoint.com:

images/articles/2016/javascript/node_js_events.png 

This is the difference between callbacks and events. The `EventEmitter` is used to bind events and event listeners.

EventEmitter Methods:

- `eventemitter.on('eventName',eventhandler)` is used to bind event name and event handler.

- `eventemitter.once('eventName', eventhandler)` is to add a listener that *only the next time* event is fired, after which it is removed.

- `eventemitter.removeListener`/`eventemitter.removeAllListeners`: remove listener

- `eventemitter.emit('eventName')` is used to fire an event.

*'eventName' above is just a identifier for an event concept, it's not a real object.* See example below:

    :::javascript
    // Import events module
    var events = require('events');
    // Create an eventEmitter object
    var eventEmitter = new events.EventEmitter();

    // Create an event handler as follows
    var connectHandler = function connected() {
     console.log('connection succesful.');

     // Fire the data_received event
     eventEmitter.emit('data_received');
    }

    // Bind the connection event with the handler
    eventEmitter.on('connection', connectHandler);

    // Bind the data_received event with the anonymous function (callback)
    eventEmitter.on('data_received', function(err, data){
        if(err)
            console.log('err');
        else{
            setTimeout(function(){
                console.log('data received');
            },2000);
        }
    });

    // Fire the connection event
    eventEmitter.emit('connection');

    console.log("Program Ended.");

Since I purposely added a `setTimeout` function to test callback, code above will generate output:

    :::
    connection succesful.
    Program Ended.
    data received

*If no `setTimeout` (i.e. `data_received` event finish immediately), 'data received' will output before 'Program Ended'.*

In Node Application, any async function accepts a callback as a **last** parameter and the callback function accepts error as a **first** parameter.

#Streams

Reading/Writing files needs `require('fs')` module.

Streams is used to read/write data. In node.js, there are four type of streams:

1. Readable: stream for read operation. Common operation: `fs.createReadStream(file)`

2. Writable: stream for write operation. Common operation: `fs.createWriteStream(file)`, `stream.write(data)`, `stream.end()`

3. Duplex: stream for both read and write operation.

4. Transform: a duplex stream which output is based on input

Each type of stream is an `EventEmitter` instance. This means it is used the same way as EventEmitter above. Some common events that are bind to these EventEmitters are:

- data: fired when data is available to read

- end: fired when no more data to be read

- error: fired when getting error while receiving/writing data

- finish: fired when transferring data process is finished

`Piping` is a mechanism where the output of one stream is the input of another stream.  Piping stream in node.js looks like following:

    :::javascript
    var fs = require('fs');
    var readerStream = fs.createReadStream('input.txt');
    var writeStream = fs.createWriteStream('output.txt');
    //Pipe Operation. Read input and write to output
    readerStream.pipe(writeStream);

`Chanining` is a mechanism to connect output of one stream to another stream and create a chain of multiple stream operations.

It usually use with Piping stream. Example:

    :::javascript
    var fs = require('fs');
    var zlib = require('zlib');
    fs.createReadStream('input.txt')
      .pipe(zlib.createGzip())
      .pipe(fs.createWriteStream('input.txt.gz'));


#Global Variables and Common Modules in node.js

Following are some global variables in node.js, which can be used directly, instead of requiring it first:

- `_filename`: the filename of the code being executed. Example: `console.log(_filename)`

- `_dirname`: name of the directory that the currently executing script resides in

- `setTimeout(function, milliseconds)`/`clearTimeout(object)`/`setInterval(function, milliseconds)`: timer functions in node.js.

Two global objects: `console` and `process` can be used directly in js file. `console` is used to print information. `process` is used to get information on current process.

Following modules are commonly used in node.js. They needs to be required at the beginning:

- OS Module: `require('os')` module provides a few basic operating system related utility functions

- Path Module: `require('path')` module provides methods to handle file paths.

- Net Module: `require('net')` module is used to create both servers and clients. It provides an asynchronous network wrapper. It has methods such as `net.createServer()`, `net.connect()`, etc. See <a href="http://www.tutorialspoint.com/nodejs/nodejs_net_module.htm">here</a> for details.

- DNS Module: Provides functions to do DNS lookup. Provides functions to use underlying operating system name resolution functions. It provides an asynchronous network wrapper. It has methods such as `dns.lookup()`, `dns.resolve()`, etc. See <a href="http://www.tutorialspoint.com/nodejs/nodejs_dns_module.htm">here</a> for details.

- Domain Module: `require('domain')` module is used to intercept unhandled error:

There are two ways to handle error: `Internal Binding`, meaning error emmitter is executing its code within `run` method of a domain; `External Binding`, meaning error emmitter is added explicitly to a domain using its add method.


##Error Object

Reference to <a href="https://docs.nodejitsu.com/articles/errors/what-is-the-error-object/">this site</a>: in node.js, `error` is a build-in object that provides a standard set of useful information when an error occurs. such as a stack trace and the error message:

    :::javascript
    var error = new Error('The error message');
    console.log(error);

Output will be:

    :::
    { stack: [Getter/Setter],
     arguments: undefined,
     type: undefined,
     message: 'The error message' }

`domain.create()` needs to be used create an instance of domain, then it can be used to listen to error event:

    :::javascript
    var EventEmitter = require('events').EventEmitter;
    var domain = require('domain');

    var emitter1 = new EventEmitter(); //create an instance of eventemitter

    var domain1 = domain.create(); //create a domain
    //Domain handle error
    domain1.on('error',function(err){
      console.log('domain1 error handler');
    });

    domain1.add(emitter1); //Explicit Binding

    //Bind error event and error handler
    emitter1.on('error',function(err){
      console.log('emittter1 error handler');
    });

    //In output, fire emitter handler instead of domain handler
    emitter1.emit('error',new Error('Error to be handled by listener'));

    var domain2 = domain.create();
    domain2.on('error',function(err){
      console.log('domain2 error handler');
    });

    //Implicit Binding. Create EventEmitter inside run method
    domain2.run(function(){
      var emitter2 = new EventEmitter();
      emitter2.emit('error', new Error('Implicit error handler')); //fire an error event with error message
    });

    //Remove explict binding and try again. Remember to remove all listeners and remove eventemitter together!
    emitter1.removeAllListeners('error');
    domain1.remove(emitter1);
    emitter1.emit('error', new Error('Converted to exception. System will crash!'));

Code above will have following output. Noted error message does not show unless there is no error handler for it:

    :::
    emittter1 error handler
    domain2 error handler

    events.js:72
            throw er; // Unhandled 'error' event
                  ^
    Error: Converted to exception. System will crash!
        at Object. (/web/com/1464273829_135671/main.js:36:28)
        at Module._compile (module.js:456:26)
        at Object.Module._extensions..js (module.js:474:10)
        at Module.load (module.js:356:32)
        at Function.Module._load (module.js:312:12)
        at Function.Module.runMain (module.js:497:10)
        at startup (node.js:119:16)
        at node.js:929:3


#Node.js as Web Server/Client

Following is the image to describe web application architecture in tutorialspoint.com:

Following code is to use node.js as web server (`server.js`):

    :::javascript
    var http = require('http');
    var fs = require('fs');
    var url = require('url');

    // Create a server
    http.createServer( function (request, response) {
       // Parse the request containing file name
       var pathname = url.parse(request.url).pathname; // /index.htm here

       // Print the name of the file for which request is made.
       console.log("Request for " + pathname + " received.");

       /*
        Read the requested file content from file system.
        Here file is index.htm, so content type is text/html. Notice the usage of file system here.
       */
       fs.readFile(pathname.substr(1), function (err, data) {
          if (err) {
             console.log(err);
             // HTTP Status: 404 : NOT FOUND
             // Content Type: text/plain
             response.writeHead(404, {'Content-Type': 'text/html'});
          }else{
             //Page found
             // HTTP Status: 200 : OK
             // Content Type: text/plain
             response.writeHead(200, {'Content-Type': 'text/html'});

             // Write the content of the file to response body
             response.write(data.toString());
          }
          // Send the response body
          response.end();
       });
    }).listen(8081);

    // Console will print the message
    console.log('Server running at http://127.0.0.1:8081/');

Following code is to use node.js as web client (`client.js`). `http` module is also used in this part:

    :::javascript
    var http = require('http');

    //Options to used by request
    var options = {
      host: 'localhost',
      port: '8081',
      path: '/index.htm'
    };

    //Deal with response from web server
    var callback = function(response){
      var body = '';
      //While data is being received by client, update body variable
      response.on('data', function(data){
        body += data;
      });
      //Finish data receiving process
      response.on('end', function(){
        console.log(body);
      });
    }

    //Make request to web server
    var req = http.request(options, callback);
    req.end();//Close request after finishing

Following is a base `index.htm`:

    :::html
    <html>
      <head>
        <title>Sample Page</title>
      </head>
      <body>
        Hello World!
      </body>
    </html>

To run code above, create these three files:

1. Then open one terminal and type `node server.js`. Terminal will show 'Server running at http://127.0.0.1:8081/' and you can open 'http://127.0.0.1:8081/' in web browser.

2. Now browse 'http://127.0.0.1:8081/index.htm'. Browser should have html available and terminal will give message 'Request for /index.htm received.'.

3. Then open another terminal and type `node client.js`. New terminal should show html code (i.e. body variable). Old terminal should show 'Request for /index.htm received.'

4. If you don't have `index.htm` file available, on step 2 terminal will give out error message, which is the code handled in server.js (404 part)


#Express

Express is a popular Node.js framework. It has following features:

- Set up **middleware** to respond to HTTP requests

- Define the **route table** to perform different action based on HTTP method and url

- Dynamically render HTML based on **passing arguments** to templates

Express is normally being installed with following modules (using `npm install xxx --save)`:

1. body-parser: the middle-ware for handling JSON, Raw, Text and URL encoded form data.

2. cookie-parser: Parse cookie header and populate `req.cookies` with an object keyed by the cookie names

3. multer - the middle-ware for handling multipart/form-data.


##Routing

Express uses `request` and `response` objects in a *callback* function. Basic usage is following:

    :::javascript
    app.get('/', function(req,res){
      //deal with request and response objects
    });

Basic way to routing (web application response to different url end point to perform operations like get, post) is following:

    :::javascript
    var express = require('express');
    var app = express();

    //GET for abcd, abcxd, ab123cd and so on, using Regular Expression
    app.get('/abc*d', function(req,res){
      console.log('GET');
      res.send('Hello GET'); //send response back
    });

    //POST
    app.post('/',function(req,res){
      console.log('POST from homepage');
      res.send('Hello POST');
    });

    //PUT
    app.put('/put',function(req,res){
      res.send('PUT from /put page');
    });

    //DELETE
    app.delete('/delete', function(req, res){
      console.log('DELETE from /delete page');
      res.send('Hello DELETE');
    });

    var server = app.listen(8081, function(){
      console.log(server.address());
    });

The console information for `server.address` may return `address` attribute as `::`. This is because if the host name is omitted, the IPv6 address will show `::` and IPv4 address will return `0.0.0.0`. See <a href="http://stackoverflow.com/questions/33853695/node-js-server-address-address-returns">this Stack Overflow post</a> for detail.


##Static Files in Express

`express.static` middleware is used to serve static files, such as images, stylesheets or JS files. An example is following:

    :::javascript
    /*
    now files in public folder (based on root) can be detected in browser
    */
    app.use(express.static('public'));
    app.get('/',function(req,res){
      //continue with other operations
    });

After running code above, URL such as `http://localhost:8081/images/test.png` can be typed and viewed in browser, as long as `image/test.png` is under `public` folder and `public` folder is in root.

##Cookie

Use `cookie-parser` middleware to print out cookie information. Example:

    :::javascript
    var express = require('express');
    var cookieParser = require('cookie-parser');

    var app = express();
    app.use(cookieParser());

    app.get('/', function(req, res) {
      console.log("Cookies: ", req.cookies);
    })

    app.listen(8081);
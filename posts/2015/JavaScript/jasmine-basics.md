.. title: Jasmine Basics
.. date: 2015-08-25
.. modified: 2015-08-28
.. category: JavaScript
.. tags: JavaScript, Software Testing, Jasmine, jQuery
.. slug: jasmine-basics
.. authors: Pengyin Shan
.. description: To automated the testing process of my JavaScript code, I decided to learn Jasmine, a behavior-driven development framework for testing JavaScript code. This post includes basic usage and my learning experience in Jasmine.

You can find Jasmine <a href="http://jasmine.github.io/2.3/introduction.html">here</a>. I choose it because:

1. It's a JavaScript framework which does not depend on any other JavaScript frameworks, and it does not require a DOM. So I can apply it on different web apps and platforms.

2. Jasmine (and its syntax) is really popular. In the future, I can also use Jasmine to test AngularJS code and other JavaScript frameworks.

3. Jasmine has good object-oriented support, making code being modular.

##Describe

`describe` keyword represents the beginning of a **test suite**.

It takes two parameters: a `string` and a `function`.

The content of string represents the content of the test suite.

There can be nested test suites/nested specs exist.

##Specs

`it` keyword represents the beginning of a spec.

It takes two parameters: a `string` and a `function`.

The content of string represents that title/introduction of the spec.

A spec contains one or more `expectation`s that test the state of the code.

A spec with all true expectations is a `passing spec`. A spec with one or more false expectations is a `failing spec`.

###Fail a Spec

You can use `fail` function to manually fail a spec. This function takes a failure message or a Error object as a parameter:

    #!javascript
      describe("A spec using the fail function", function() {
      var foo = function(x, callBack) {
        if (x) {
          callBack();
        }
      };
      it("should not call the callBack", function() {
        foo(false, function() {
          fail("Callback has been called");
        });
      });
    });

###Setups

`beforeEach`, `afterEach`, `beforeAll`, `afterAll` can be used to setup environment before/after test suites/specs.

`beforeEach` function is called once before **each** spec run in test suite.

`afterEach` function is called once after **each** spec run.

>i.e. For each spec in a test suite, `beforeEach` function run first, then the spec function, then `afterEach` function. So if a test suite has multiple specs, `beforeEach` function and `afterEach` function should be run multiple times.

`beforeAll` function is called **only once* before all the specs run.

`afterAll` function is called **only once** after all the specs run.

>Remember if you have a variable which is share between `beforeAll` function, spec function and `afterAll` function, this variable will be continuously modified until all specs are done.

Example:

    #!javascript
     describe("A spec using beforeEach and afterEach", function() {
      var foo = 0;
      beforeEach(function() {
        foo += 1;
      });
      afterEach(function() {
        foo = 0;
      });
      //Here foo will be reset to 0 everytime after a spec running, because of afterEach()
      it("is just a function, so it can contain any code", function() {
        expect(foo).toEqual(1);
      });
      it("can have more than one expectation", function() {
        expect(foo).toEqual(1);
        expect(true).toEqual(true);
      });
    });

>For nested `describe` blocks, before one spec running, `beforeEach` function **for all describes** will be run. Similarly, after one spec running, `afterEach` function **for all describes** will be run.

####Use `this` in Setup

`this` variable can be shared between `beforeEach`, `it` and `afterEach` function.

`this` will be **reset** every time a spec run.

Example:

    #!javascript
      describe("A spec", function() {
      beforeEach(function() {
        this.foo = 0;
      });
      it("can use the `this` to share state", function() {
        expect(this.foo).toEqual(0);
        this.bar = "test pollution?";
      });
      it("prevents test pollution by having an empty `this` created for the next spec", function() {
        expect(this.foo).toEqual(0);
        expect(this.bar).toBe(undefined);
      });
    });


###Disable Suites and Specs

Instead of `describe` and `it`, you can use `xdescribe` and `xit` to skip this test suite or spec.

##Expectations

An expectation in Jasmine is an **assertion** that is either `true` or `false`.

Syntax Example:

    :::javascript
    expect(a).toBe(true);

`expect` takes a value, called `actual`.

`expect` take a `matcher function` on second part, which takes the **expected value**.

###Matcher

You can always add a `not` in front of any matcher to turn it to a negative assertion.

Example:

    :::javascript
    expect(a).toEqual(9);
    expect(a).not.toEqual(9);

###List of Matcher

- `toBe`

- `toEqual`

- `toBeDefined`

- `toBeUndefined`

- `toBeNull`

- `toBeTruthy`

- `toBeFalsy`

- `toContain`

- `toBeLessThan`

- `toBeGreaterThan`

- `toBeCloseTo`

- `toThrow`

- `toThrowError`

###Custom Matchers

A custom matcher at its root is a **comparison function** that takes an **actual value** and **expected value**.

####Structure of Custom Matcher

Create a object, which contains one to many custom matchers.

Each custom matcher is a function, which takes `util` and `customEqualityTesters` as parameters.

`util`: contains a set of **utility functions** for matchers to use. For example:

    :::javascript
    //this utility function test hyuk property of actual object
    result.pass = util.equals(actual.hyuk, "gawrsh" + expected, customEqualityTesters);

>Check <a href="https://github.com/jasmine/jasmine/blob/master/src/core/matchers/matchersUtil.js">matchersUtil.js</a> for all utility functions.

- `customEqualityTesters`: You may or maynot need customEqualityTester, depending on your choice of utility function.

*You custom matcher method must return an object with a `compare` function.* The `compare` function takes `actual` and `expected` as parameter.

In following code, a `result` object is returned. *This `result` object must have a `pass` property, which is `true` or `false`*:

    :::javascript
    var customMatchers = {
        sample_custom_method: function(util, customEqualityTesters){
            return{
                compare: function(actual,expected){
                    //You may or maynot use expected variable. If not, you can skip parameter when you call this method
                    var result = {};
                    result.pass = util.utility_function(); //see code above
                    if(result.pass){
                        result.message = "custom your pass message";
                    }else{
                        result.message = "custom your fail message";
                    }
                    return result;
                }
            }
        }
    }

>You can add `.not` in utility function for result.pass

>You can skip defining result.message. jasmine will try to craft one for your custom matcher.

>If you have too many negative comparison (`.not`), you can add `negativeCompare` function alongside `compare`, using similar structure to include all `.not` methods.

####How to Use Custom Matcher

You should register you custom matchers in `beforeEach` block, using a function `jasmine.addMatchers`:

    :::javascript
    beforeEach(function() {
        //You can get all matcher methods in customMatchers
        jasmine.addMatchers(customMatchers);
    });

To use it, just call matcher method in expectations:

    :::javascript
    it("test custom matcher", function(){
        expect(your_varaible).sample_custom_method(expected_varaible_in_custom_method);
        })

##Spy

A `spy` can stub any function and tracks calls to it and all arguments.

A spy only exists in the `describe` or `it` block it is defined, and will be **removed** after each spec.

>When you put spy `spyOn()` in `beforeEach()` block, based on how `beforeEach()` work, your spy call will be called before each spec function run.

###toHaveBeenCalled and toHaveBeenCalledWith

`toHaveBeenCalled` will return `true` if the spy was called.

`toHaveBeenCalledWith` will return `true` if the argument list matches any of the **recorded calls** to the spy.

Example:

    :::javascript
      describe("A spy", function() {
      var foo, bar = null;
      beforeEach(function() {
        foo = {
          setBar: function(value) {
            bar = value;
          }
        };
        spyOn(foo, 'setBar');
        foo.setBar(123);
        foo.setBar(456, 'another param');
      });
      it("tracks that the spy was called", function() {
        expect(foo.setBar).toHaveBeenCalled(); //this spec will call spy function
      });
      it("tracks all the arguments of its calls", function() {
        expect(foo.setBar).toHaveBeenCalledWith(123);
        expect(foo.setBar).toHaveBeenCalledWith(456, 'another param');
        //this spec detect if spy function has worked. i.e. if the variables which were spied have been modified
      });
      it("stops all execution on a function", function() {
        expect(bar).toBeNull();
        //this spec make sure spy should be removed after each spec function
      });
    });

###callThrough

You can add `and.callThrough()` after spy function to make sure spy will **track all spec calls**, instead of being removed after each spec call:

    :::javascript
    spyOn(foo, 'getBar').and.callThrough();

###returnValue

You can add `and.returnValue(value)` after spy function to make sure your desired call in spy function will return a value:

    :::javascript
    spyOn(foo, "getBar").and.returnValue(745); //getBar method for foo object will return value `745`

###callFake

You can add `and.callFake(function(){})` to create a fake function which can replace the content of your spied function:

    ::javascript
      describe("A spy, when configured with an alternate implementation", function() {
      var foo, bar, fetchedBar;
      beforeEach(function() {
        foo = {
          setBar: function(value) {
            bar = value;
          },
          getBar: function() {
            return bar;
          }
        };
        //force `getBar` to return 1001, but notice `bar` variable is not affected by this fake call
        spyOn(foo, "getBar").and.callFake(function() {
          return 1001;
        });
        foo.setBar(123);
        fetchedBar = foo.getBar();
      });
      it("tracks that the spy was called", function() {
        expect(foo.getBar).toHaveBeenCalled();
      });
      it("should not effect other functions", function() {
        //fake function does not impact other real function
        expect(bar).toEqual(123);
      });
      it("when called returns the requested value", function() {
        //fake function should work
        expect(fetchedBar).toEqual(1001);
      });
    });

###stub

To remember the state of any spy calling method above, use `and.stub()` to get the original stubbing behavior:

    :::javascript
    describe("A spy", function() {
      var foo, bar = null;
      beforeEach(function() {
        foo = {
          setBar: function(value) {
            bar = value;
          }
        };
        spyOn(foo, 'setBar').and.callThrough();
      });
      it("can call through and then stub in the same spec", function() {
        foo.setBar(123);
        expect(bar).toEqual(123);
        //use .and.stub() for the spied method
        foo.setBar.and.stub();
        bar = null;
        //Now bar should always be null
        foo.setBar(123);
        expect(bar).toBe(null);
      });
    });

###Tracking Properties

After you having `spayOn(obj, spied_method)`, following tracking properties can be used when you call the spied method in `expect`:

- `.calls.any()`: return `false` if spy has not been called at all. return `true` once **at least** one call happens.

- `.calls.count()`: returns the number of times the spy was called.

- `.calls.argsFor(index)`: assume you call a method a few times. Use `index` to get different `expect` function results:

>Example:

    :::javascript
    it("tracks the arguments of each call", function() {
        foo.setBar(123);
        foo.setBar(456, "baz");
        expect(foo.setBar.calls.argsFor(0)).toEqual([123]);
        expect(foo.setBar.calls.argsFor(1)).toEqual([456, "baz"]);
    });

- `.calls.allArgs()`: assume you call a method a few times, and return all results from these calls in `expect` functions:

>Example:

    :::javascript
        it("tracks the arguments of all calls", function() {
            foo.setBar(123);
            foo.setBar(456, "baz");
            expect(foo.setBar.calls.allArgs()).toEqual([[123],[456, "baz"]]);
        });

- `calls.all()`: use this to check all context and argument(i.e. `this` variable) in `expect` function: `expect(foo.setBar.calls.all()).toEqual([{object: foo, args: [123], returnValue: undefined}]);`

- `.calls.mostRecent()`: similar as above, but just return context and arguments for **the most recent call**.

- `.calls.first()`: similar as above, but just return context and arguments for **the first call**.

- `.calls.reset()`: clears all tracking for a spy

###jasmine method

####createSpy

`jasmine.createSpy()` is a function with **no implementation**. It acts as other spies:

    :::javascript
    var whatAmI;
    beforeEach(function() {
        whatAmI = jasmine.createSpy('whatAmI');
        whatAmI("I", "am", "a", "spy"); //it does not have implementation. Only with arguments
      });
      //expect(whatAmI).toHaveBeenCalledWith("I", "am", "a", "spy");
      //expect(whatAmI.calls.mostRecent().args[0]).toEqual("I");

####createSpyObj

Similar as above, `jasmine.createSpyObj` accept an **array of strings**, and return a object that has a **property** for each string of the spy:

    :::javascript
    var tape;
     beforeEach(function() {
        tape = jasmine.createSpyObj('tape', ['play', 'pause', 'stop', 'rewind']);
        tape.play();
        tape.pause();
        tape.rewind(0);
    });

####anything

`jasmine.anything` returns `true` if the actual value is **not** `null` or `undefined`: `expect(1).toEqual(jasmine.anything());`

####objectContaining

`jasmine.objectContaining` tests objects with **key-value** pairs:

    :::javascript
      describe("jasmine.objectContaining", function() {
      var foo;
      beforeEach(function() {
        foo = {
          a: 1,
          b: 2,
          bar: "baz"
        };
      });
      it("matches objects with the expect key/value pairs", function() {
        expect(foo).toEqual(jasmine.objectContaining({
          bar: "baz"
        }));
        expect(foo).not.toEqual(jasmine.objectContaining({
          c: 37
        }));
      });

####arrayContaining

`jasmine.arrayContaining` test objects with **values in array**:

    :::javascript
      beforeEach(function() {
        foo = [1, 2, 3, 4];
      });
      it("matches arrays with some of the values", function() {
        expect(foo).toEqual(jasmine.arrayContaining([3, 1]));
        expect(foo).not.toEqual(jasmine.arrayContaining([6]));
      });

####stringMatching

`jasmine.stringMatching()` test if you want match **a string in a object** or **regular expression** pattern:

    :::javascript
    describe('jasmine.stringMatching', function() {
      it("matches as a regexp", function() {
        expect({foo: 'bar'}).toEqual({foo: jasmine.stringMatching(/^bar$/)});
        expect({foo: 'foobarbaz'}).toEqual({foo: jasmine.stringMatching('bar')});
    });

###Custom Equality Tester

You can create your own equality tester for your test criteria, using `asymmetricMatch` function name:

    :::javascript
      var tester = {
        //Use asymmetricMatch as function. No returns
        asymmetricMatch: function(actual) {
          var secondValue = actual.split(',')[1];
          return secondValue === 'bar';
        }
      };
      it("dives in deep", function() {
        expect("foo,bar,baz,quux").toEqual(tester);
      });

##Clock

`jasmine.clock().install()` can be used to setup time dependent testing. To do this, you can put `jasmine.clock().install` in `beforeEach()` block and `jasmine.clock().uninstall()` in `afterEach()` block.

###Timeout

Use `jasmine.clock().tick(milliseconds)` function to simulate timeout in JavaScript: `jasmine.clock().tick(1000)`;

###Date

You can create a `Date` object in JavaScript, then use `jasmine.clock().mockDate(date_object)` to simulate date:

    :::javascript
    var baseTime = new Date(2014, 9, 23);
    jasmine.clock().mockDate(baseTime);

>If you don't provide a time object, jasmine will use current Date.

##Ajax

You need to include `mock-ajax.js` from <a href="https://github.com/jasmine/jasmine-ajax">here</a> to test Ajax using jasmine.

Make sure you have `jasmine.Ajax.install()` in `beforeEach()` block and `jasmine.Ajax.uninstall()` in `afterEach()` to install and uninstall jasmine-ajax.

###Define Mock Response

You may want to define a mock response to test your Ajax call response. A good place to define this is in `spec/javascripts/helpers/test_responses`.

Example:

    :::javascript
    var TestResponses = {
      search: {
        success: {
          status: 200,
          //Make responseText to be your response data
          responseText: '{"response":{"groups":[{"type":"nearby","name":"Nearby","items":[{"id":"4bb9fd9f3db7b7138dbd229a","name":"Pivotal Labs","contact":{"twitter":"pivotalboulder"}'}]}]}}
        }
      }
    };

###Trigger Request

You need to trigger request before you test your Ajax response. You can set a function call, such as:

    :::javascript
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function(args) {
        if (this.readyState == this.DONE) {
          doneFn(this.responseText);
        }
      };
      xhr.open("GET", "/some/cool/url");
      xhr.send();

Or:

    :::javascript
    beforeEach(function() {
    jasmine.Ajax.install();
    onSuccess = jasmine.createSpy('onSuccess');
    onFailure = jasmine.createSpy('onFailure');
    foursquare = new FoursquareVenueSearch();
    foursquare.search('40.019461,-105.273296', {
      onSuccess: onSuccess,
      onFailure: onFailure
    });
    request = jasmine.Ajax.requests.mostRecent();
    //create a request object. This request will not be triggered until you set response
    expect(request.url).toBe('venues/search');
    expect(request.method).toBe('POST');
    expect(request.data()).toEqual({latLng: ['40.019461, -105.273296']});
    });

###Set Response

Use `.respondWith()` to set response. You need to tell jasmine which response you want to test. For example, based on the code in **Define Mock Response** part, you can test `success` response:

    :::javascript
      describe("on success", function() {
      beforeEach(function() {
        request.respondWith(TestResponses.search.success);
      });
    });

You can also set the object that you want to have as response:

    :::javascript
    jasmine.Ajax.requests.mostRecend().respondWith({
        "status": 200,
        "contentType",'text/plain',
        "responseText": 'test response'
        });

###Full Steps

After these step, you can create `it` blocks to test your Ajax call. Here is a full example for `post` from jasmine-ajax Github repo:

    :::javascript
      describe("FoursquareVenueSearch", function() {
      var foursquare, request;
      var onSuccess, onFailure;
      beforeEach(function() {
        jasmine.Ajax.install();
        onSuccess = jasmine.createSpy('onSuccess');
        onFailure = jasmine.createSpy('onFailure');
        foursquare = new FoursquareVenueSearch();
        foursquare.search('40.019461,-105.273296', {
          onSuccess: onSuccess,
          onFailure: onFailure
        });
        request = jasmine.Ajax.requests.mostRecent();
        expect(request.url).toBe('venues/search');
        expect(request.method).toBe('POST');
        expect(request.data()).toEqual({latLng: ['40.019461, -105.273296']});
      });
      describe("on success", function() {
        beforeEach(function() {
          request.respondWith(TestResponses.search.success);
        });
        it("calls onSuccess with an array of Locations", function() {
          expect(onSuccess).toHaveBeenCalled();
          var successArgs = onSuccess.calls.mostRecent().args[0];
          expect(successArgs.length).toEqual(1);
          expect(successArgs[0]).toEqual(jasmine.any(Venue));
        });
      });
    });

Other `get` Ajax call examples can be found on <a href="http://jasmine.github.io/2.3/ajax.html">jasmine website</a>.

##Jasmine-jQuery

<a href="https://github.com/velesin/jasmine-jquery">jasmine-jquery</a> is great to combine Jasmine with jQuery. It provides:

- a set of **custom matchers** for jQuery framework

- an API for handling HTML, CSS, and JSON fixtures in your specs

###Custom Matcher

You can find a list of useful custom matchers, such as `toBeCheck()` or `toBeSelected()` <a href="https://github.com/velesin/jasmine-jquery">here</a>.

###HTML Fixture

I'm still trying to figure out the best practice to apply HTML Fixture for my working project. HTML Fixture can be used to load HTML content to be used by your tests.

You can find more detailed information about HTML Fixture <a href="https://github.com/velesin/jasmine-jquery">here</a>. For most of my working projects, I need to limit the complexity of all my JavaScript test. Also, instead of `html`, my work is more involved in `jsp`, which is really hard to be transferred to pure HTML code for fixture content. Personally I prefer not to write too many fixtures for to simplify my test.

I'll continue to research for the best practice of using HTML Fixture.

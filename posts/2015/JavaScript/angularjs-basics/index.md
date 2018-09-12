.. title: AngularJS Basics
.. date: 2015-08-11
.. category: JavaScript
.. tags: AngularJS, JavaScript
.. slug: angularjs-basics
.. authors: Pengyin Shan
.. description: My job may requires me to use AngularJS in future projects, so I write this post to review some useful information about AngularJS.

##Resouce List

- <a href="http://www.tutorialspoint.com/angularjs">AngularJS Tutorial on tutorialspoint.com</a>

- <a href="https://docs.angularjs.org">AngularJS Official API Doc</a>

##Core Features

- `Data-binding`: Two-way data-binding between model and view components.

- `Scope`: Objects that refer to the model

- `Controller`: The controller for a specific scope

- `Services`: Built-in services for functions such as `XMLHttpRequests`.

- `Filters`: Generate a new array from a subset of items in an old array.

- `Directives`: Create custom HTML tags as new widgets.

- `Templates`: The "View" part in MV* structure

- `Routing`: Switching between different views

- `MVVM`: Instead of purse MVC structure, AngularJS is a `MVVM` (Model-View-ViewModel) structure.

- `Deep Linking`: Bookmark current state of application in URL so that this state can be restored later.

- `Dependency Injection`: The DI system in AngularJS

A description graph from tutorialspoint.com:

../images/articles/2015/javascript/angularjs_concepts.jpg 

##Three Major Parts

- `ng-app`: Link a AngularJS application to HTML.

- `ng-model`: Bind the value of AngularJS application data to HTML input controls

- `ng-bind`: Bind angularJS application to HTML tags.

##Controller

HTML:

    :::html
    <div ng-app="" ng-controller="testController">
        Test Name 1: {{names.name1}}
        Test Name 2: {{names.name2}}
        Test Name 3: {{names.name3()}}
    </div>

JS:

    :::javascript
    function testController($scope){
        $scope.names = {
            name1: 'a',
            name2: 'b',
            name3: function(){
                return $scope.name1;
            }
        }
    }

##Type of Filters

- `uppercase`

- `lowercase`

- `currency`

- `filter`: example `ng-repeat='name in names | filter: firstname'`

- `orderby`

##HTML DOM Control

- `ng-disabled`: disable a given control.

- `ng-show`: show a given control.

- `ng-hide`: hide a give control.

- `ng-click`: a AngularJS click event.

Example:

    :::html
    <input type="checkbox" ng-model="checkboxmodel"/>
    <button ng-disabled='checkboxmodel'>Disable/Enable this Button</button>

##Module

- `Application Module`: Initialize application with controller

    - Example: `var myApp = angular.module('myApp, []);`

- `Controller Module`: Define the controller. Example is in "Controller" section

##ng-events

- `ng-click`

- `ng-dbl-click`

- `ng-mousedown`

- `ng-mouseup`

- `ng-mousenter`

- `ng-mouseleave`

- `ng-mousemove`

- `ng-mouseover`

- `ng-keydown`

- `ng-keyup`

- `ng-keypress`

- `ng-change`

##Forms

###Data Validation

- `$dirty`: Notify when a value is changed

- `$invalid`: Notify when a value is invalided

- `$error`: Point out the error

Example from tutorspoint:

    :::html
    <tr>
        <td>Enter last name: </td>
        <td>
            <input name="lastname"  type="text" ng-model="lastName" required>
            <span style="color:red" ng-show="studentForm.lastname.$dirty && studentForm.lastname.$invalid">
                <span ng-show="studentForm.lastname.$error.required">Last Name is required.</span>
           </span>
        </td>
    </tr>


##ng-includes

`ng-includes` is used to include partial views, which is similar to
`<jsp:include page = "../../test.jsp"/>` in JSP page.

Example from tutorialspoint.com:

    :::html
    <div ng-app="" ng-controller="studentController">
       <div ng-include="'main.htm'"></div>
       <div ng-include="'subjects.htm'"></div>
    </div>


##AJAX in AngularJS

Similar as jQuery, the format of AJAX is following:

    :::javascript
    $http.get('/someUrl').
      then(function(response) {
        // this callback will be called asynchronously
        // when the response is available
      }, function(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
      });

    :::javascript
    // Simple POST request example (passing data) :
    $http.post('/someUrl', {msg:'hello word!'}).
      then(function(response) {
        // this callback will be called asynchronously
        // when the response is available
      }, function(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
      });

Since AngularJS Ajax involves in some other knowledge, I will write extra post about this.

##Views

###ng-view

Just create a placeholder for easier configuration:

    :::html
    <div ng-view></div>

###ng-template

Create a view with `id`. This view will be map to a controller using `$routeProvider`.

Example from tutorialspoint.com:

    :::html
    <div ng-app="mainApp">
       <script type="text/ng-template" id="addStudent.htm">
          <h2> Add Student </h2>
             {{message}}
       </script>
    </div>

###$routeProvider

`$routeProvider` configure urls and map to corresponding views. The controller for that corresponding view will also be attached. It works similar to `@RequestMapping(value='...')` function in Spring MVC framework.

Example from tutorialspoint.com:

    :::javascript
    //You need to add ngRoute to application controller
    var mainApp = angular.module("mainApp", ['ngRoute']);
    //templateUrl maps the id defined in ng-template
    mainApp.config(['$routeProvider',
         function($routeProvider) {
            $routeProvider.
               when('/addStudent', {
                  templateUrl: 'addStudent.htm',
                  //addStudent.htm should be the same path as main.htm
                  controller: 'AddStudentController'
               }).
               when('/viewStudents', {
                  templateUrl: 'viewStudents.htm',
                  controller: 'ViewStudentsController'
               }).
               otherwise({
                  //Default View
                  redirectTo: '/addStudent'
               });
    }]);

##Scope

`$scope` is passed as first argument to controller during its constructor definition.

- **Scope is controller specific.**

- **Child controller can inherit scope from parent controller.**

- **Scope in parent controller can be overwritten by child controller**.

Example from tutorialspoint.com:

    :::javascript
    <script>
      var mainApp = angular.module("mainApp", []);
      mainApp.controller("shapeController", function($scope) {
         $scope.message = "In shape controller";
         $scope.type = "Shape";
      });
      mainApp.controller("circleController", function($scope) {
         $scope.message = "In circle controller";  //Overwritten
      });
    </script>

##Service

Services are JavaScript functions and are responsible to do a **specific tasks** **only.

Services are normally injected using **dependency injection** mechanism of AngularJS.

There are two types of service.

###Factory

Define a factory then assign method to it.

Example from tutorialspoint.com:

    :::javascript
     var mainApp = angular.module("mainApp", []);
      //Define a MathService factory
      mainApp.factory('MathService', function() {
         var factory = {};
         factory.multiply = function(a, b) {
            return a * b
         }
         //return factory object
         return factory;
      });

###Service

Call Factory and perform methods defined in Factory:

    :::javascript
    //take MathService factory as a parameter
    mainApp.service('CalcService', function(MathService){
            //CalService define a squre method
            this.square = function(a) {
            return MathService.multiply(a,a);
            //call MathService factory 'multiply' method
         }
      });

Finally, you can call service in your controller method:

    :::javascript
    //take CalcService service as a parameter
    mainApp.controller('CalcController', function($scope, CalcService) {
            $scope.square = function() {
            $scope.result = CalcService.square($scope.number);
            //Call square method from CalcService
         }
      });

##Dependency Injection

Following component of AngulaJS can be injected into other components:

- `value`

- `factory`: Example above injecting MathService factory to CalcService service

- `service`

- `provider`: `Provider` is a special factory method with a method `get()`which is used to return the `value`/`service`/`factory`.

- `constant`

Example for value/constnat from tutorialspoint.com:

    :::javascript
    mainApp.value("defaultInput", 5);
    mainApp.constant("configParam", "constant value");
    mainApp.controller('CalcController', function($scope, defaultInput, configParam) {
        //...
    }

Example for provider from tutorialspoint.com:

    :::javascript
    //create a service using provider which defines a method square to return square of a number.
    mainApp.config(function($provide) {
       $provide.provider('MathService', function() {
          //This provider gets MathService factory
          this.$get = function() {
             var factory = {};
             factory.multiply = function(a, b) {
                return a * b;
             }
             return factory;
          };
       });
    });

##Custom Directives

Custom directives are defined using `directive` function. **A custom directive simply replaces the element for which it is activated**.

AngularJS use its `compile()` method of the custom directive then process the element using `link()` method of the custom directive based on the scope of the directive.

You can create custom directives for following type of elements:

- `Element directives`: Directive activates when a **matching element** is encountered.

- `Attribute`: Directive activates when a **matching attribute** is encountered.

- `CSS`: Directive activates when a **matching css** style is encountered.

- `Comment`: Directive activates when a **matching comment** is encountered.

Example custom HTML tags from tutorialspoint.com:

View:

    :::html
    <!-- This controller includes custom directive necessary information -->
     <div ng-app="mainApp" ng-controller="StudentController">
        <student name="Mahesh"></student><br/>
        <student name="Piyush"></student>
   </div>

Controller:

    :::javascript
    mainApp.controller('StudentController', function($scope) {
            $scope.Mahesh = {};
            $scope.Mahesh.name = "Mahesh Parashar";
            $scope.Mahesh.rollno  = 1;
            $scope.Piyush = {};
            $scope.Piyush.name = "Piyush Parashar";
            $scope.Piyush.rollno  = 2;
      });

Create Directive:

    :::javascript
    /Create a directive, first parameter is the html element to be attached.
    //This directive will be activated as soon as any student element is encountered in html
    mainApp.directive('student', function() {
       //define the directive object
       var directive = {};
       //restrict = E, signifies that directive is Element directive
       directive.restrict = 'E';
       //template replaces the complete element with its text.
       directive.template = "Student: <b>{{student.name}}</b> , Roll No: <b>{{student.rollno}}</b>";
       //scope is used to distinguish each student element based on criteria.
       directive.scope = {
           student : "=name"
       }

Compile:

    :::javascript
       //compile is called during application initialization. AngularJS calls it once when html page is loaded.
       directive.compile = function(element, attributes) {
          element.css("border", "1px solid #cccccc");
          //linkFunction is linked with each element with scope to get the element specific data.
          var linkFunction = function($scope, element, attributes) {
              element.html("Student: <b>"+$scope.student.name +"</b> , Roll No: <b>"+$scope.student.rollno+"</b><br/>");
              //You are using the scope from controller. Note StudentController replace 'student' to a specific student name
              element.css("background-color", "#ff00ff");
          }
          return linkFunction;
       }
       return directive;
    });

In the example above, you need to create a directive, then create a corresponding compile attribute for it.
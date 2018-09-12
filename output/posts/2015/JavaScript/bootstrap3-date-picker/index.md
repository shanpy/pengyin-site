.. title: Boostrap3 Date Picker
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: JavaScript
.. tags: JavaScript
.. slug: bootstrap3-date-picker
.. authors: Pengyin Shan
.. description: This is a brief introduction about <a href="https://github.com/eternicode/bootstrap-datepicker">bootstrap-datepicker</a>, a date-picker that is built for Bootstrap including different functions. It is created by <a href="https://github.com/eternicode">eternicode</a>.



##Usage

You can try a sandbox <a href="http://eternicode.github.io/bootstrap-datepicker/?markup=input&format=&weekStart=&startDate=&endDate=&startView=0&minViewMode=0&todayBtn=false&clearBtn=false&language=en&orientation=auto&multidate=&multidateSeparator=&keyboardNavigation=on&forceParse=on#sandbox">here</a> to expore more about bootstrap-datepicker.

###General Usage

Generally everything is easy. After you refer source file (stylesheet and js) in code, create a `<input type="input">` element. Then write following JavaScript code:

	:::javascript
	$("#your_container input").datepicker();

Now when you click input box, a calendar will appear.

###Embeded Full Calander

You may want a full calender instead of a input box. First you make a `<div>` with id/className, The do same JavaScript code as above:

	:::javascript
	$("#your_div").datepicker();

###Disable Special Dates

One of the function I use very often is to disable some dates (Or only make a few dates available). You need `beforeShowDay` option to do this:

	:::javascript
	var avialableDates= [1,18,20];
	$("#date_picker").datepicker({
	    beforeShowDay: function(date){
	        if(date.getMonth() == (new Date()).getMonth())
	        //This means date apply to any month, you can also set specific month if you need

	        switch(true){
	            case(availableDates.indexOf(date.getDate())==-1):
	                //Do something to unavailable date
	                return false;

	                //You can also set opearation to available date
	        }
	    }
	});

###Do Something after User Choose Date

You may want to perform something after user click on a date. Use `.change()` and `.on` to detect user's selection and assign function to it:

	:::javascript
	$("#your_div").datepicker({
	  //assign options, such as beforeShowDay
	}).change(changeEvent)
	  .on('changeDate',changeEvent);


	function changeEvent(ev){
	    var nowDate = new Date(ev.Date).getDate();
	    //This is the date that user choose. You are free to use .getFullYear(), .getMonth(), etc

	    //Do whatever you want to do
	}

##Problems and Solutions

###P1: "cannot call method 'split' of undefined" error

S1: I find following steps to solve this problem:

- First, check if there is any repeat id/class name as the one that you are calling

- Second, try to add "format: 'dd.mm.yyyy'" in option list

- Third, check if your version is right: you can download a zip with both production version and full version <a href="http://eternicode.github.io/bootstrap-datepicker/?markup=input&format=&weekStart=&startDate=&endDate=&startView=0&minViewMode=0&todayBtn=false&clearBtn=false&language=en&orientation=auto&multidate=&multidateSeparator=&keyboardNavigation=on&forceParse=on#sandbox">here</a>. Try to replace your javascript file with another version, and check if problem disappears.
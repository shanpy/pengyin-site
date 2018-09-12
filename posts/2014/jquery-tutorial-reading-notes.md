.. title: jQuery Tutorial Reading Notes
.. date: 2014-12-10
.. modified: 2015-06-01
.. category: JavaScript
.. tags: JavaScript, jQuery
.. slug: jquery-tutorial-reading-notes
.. authors: Pengyin Shan
.. description: This is an old blog I created when I wanted to be more familiar with jQuery library, in late 2014. This is a reading note for <a href="http://www.tutorialspoint.com/jquery">jQuery Tutorial on TutorialsPoint.com</a>, including useful functions/concepts for web development using jQuery. Please note I only pick parts of core concept which I will use most often.

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

If you want to find specific topic, feel free to use `ctrl + F` to search for keyword.

This is a reading note for <a href="http://www.tutorialspoint.com/jquery">jQuery Tutorial on TutorialsPoint.com</a>, including useful functions/concepts for web development using jQuery. Please note I only pick parts of core concept which I will use most often.

This reading note is based on `jQuery 1.3.2`.

#Part I : Selectors, Attributes, Traversing

##Selectors

###$()/jQuery() function

`$()` or `jQuery()` is the format for all selectors in jQuery. It can be applied to:

- *Tag*: `$('p')` selects all paragraphs in document

- *#ID*: `$('#test')` select element with ID as test

- *.Class*: `$('.test')` select element with ClassName as test

- *\**: star means universal. This means all DOM elements have been selected

- *Mutiple Selectors*: results from mutiple selectors can be selected at the same time. For example, `$('a#IDs.Classes')` means an element with `<a>` *and* `ID` as id *and* `Classes` as class name.

###Important Notes

- `$(XX:not(YY))`: select XX elements without YY elements

- `$(XX YY)`: this means select YY elements which are *descendants* of XX elements. i.e, inside XX elements

- `$(XX YY:first)`: select first YY elements which is inside XX

- `$(XX > YY)`: select YY elements which are children of XX elements

- `$(XX + YY)`: select YY elements that is the *connected* following sibling of XX elements.

- `$(XX ~ YY)`: select YY elements that is the following siblings of XX elements

- `$(XX,YY)`: select elements that match XX *or* YY

- `$(':empty')`:select elements that have no child elements

- `$('XX:empty')`:select all XX elements that have no child elements

- `$('XX[YY]')`: select all XX elements that *contains* an element with attribute YY

- `$('XX[@YY]')`: select all XX elements that has a YY attribute

- `$('XX[@YY=ZZ]')`: select all XX elements that has a YY attribute, and attribute value is ZZ

- `$('XX[@YY^=ZZ]')`: select all XX elements that has a YY attribute, and attribute value *begin with* ZZ

- `$('XX[@YY$=ZZ]')`: select all XX elements that has a YY attribute, and attribute value *end with* ZZ

- `$('XX[@YY*=ZZ]')`: select all XX elements that has a YY attribute, and attribute value *containing* ZZ

- `$("XX:YY")`: YY here can be: `even`, `odd`, `first`, `last`, `visible`, `hidden`, `radio`, `checked`, `input`, `text`, `eq(n)` (This mean nth element), `li(n)` (This means the first nth element), `ge(n)` (This means after n+1 element), `first-child`, `last-child`, `contains(YY)` (This means contain text YY)

- `$(XX/YY)`: select YY elements that are child of an element XX

- `$(XX//YY)` or `$(//XX//YY)`: select YY elements that are descendants of an element XX

- `$(:parent)`:all elements that are *parents* of another element, including `text`

##DOM Attributes

Some of most import DOM attributes are: `className`, `tagName`, `id`, `href`, `title`, `rel`, `src`

*Get Attribute Value*: `.attr()`. For example: `var title = $(#testId).attr('title');`. Element testId should be `<XX titile="..."/>`

*Set Attribute Value*: `.attr(name,value)`. For example, `$("#testId").attr('src','/image.jpg');`

*Set Mutiple Attribute Value*: `.attr({key:value, key:value})`:

    :::javascript
    $('#testId').attr({
        src: `/image.png`,
        alt: 'images',
        style: `display:auto;`
    });

*Set Attribbute with Function*: `.attr(key, function(){...});`

*Remove Attribute*: `.removeAttr(Attr_Name);`

*Set Class*: `.addClass()`. You may want to define the style for this class first in style sheet. For example, `$(#testId).addClass('main');`

*Remove Class*: `.removeClass(Class_Name);`

*Judge if Exists Class*: `XX.hasClass(Class_Name)`. Return true if as least one of XX element has this specific class

*Add/Remove Class*: *.toggleClass(Class_name)*. Add class if not exist. Remove class if it exists.

*Get Content*: `.html()`. Get html content of the *first* matched element. Equals to `xx.getInnerHTML();`

*Set Context*: `.html(val)`. For example: `var test = "<p>Test</p>. $('#testId').html(test)"` means assign content in test to element testId.

*Get All Text Content*: `.text()`. Get the *combined* text contents of all matched elements.

*Set Text Contents to All*: `.text(val)`. Set the text contents of all matched elements.

*Get Value*: `.val()` get the input value of the first matched element

*Set Value*: `val(val)`. If applied to `input`, set the value of all input field. If applied to `select` and passign `option` value, that option is selected. If applied to `checkbox` or `radiobutton`, all match checkbox or radiobutton are selected.

##DOM Traversing

###For Table Lists

`.eq(index)`: find the *index+1*th element, since we count staring from 0.

`.filter(selector)`: remove all elements which not match to selector

`.filter(function)`: remove all elements which not match to function

`XX.is(selector)`: return true if at least one element of XX fits the selector

`XX.map(callback)`: transfer XX to a jQuery array, following callback

`.not(selector)`: remove all elements which match to the selector

`.slice(start, [end])`: select a subset of matched elements. Starting for *0*.

*End is exclusive*. If using nagative number, it means starting from the end of selection.

###Others

`XX.add(selector)`: add more elements to XX, which matches the selector.

`XX.selector.andSelf().Do-something`: Do something to elements in selector, and XX itself:

    :::javascript
    $('div').find(p).andSelf().addClass("border");
    //Add border to all paragraphs, and all divs themselves

`XX.children(selector)`: select *sons* of XX which matches selector

`XX.closest(selector)`: First check if XX matches selector, if so return XX. Otherwise find XX's cloest *parent* element which matches the selector, and return this element.

`.contents()`: Applies to `iframe`. Get all contents (i.e. child nodes) of iframe.

`XX.end()`: revert XX to its previous state.

`.find(selector)`: find all *descedent* elements that match selector

`.next(selector)`: find first *sibling* which match the selector

`.nextAll()/.nextAll(selector)`: find all *siblings*. Can add selector as parameter

`XX.offsetParent()`: return the *first* parent of XX elements.

`parent()/parent(selector)`: reutrn the direct parent of element. Can add selector as parameter

`prev()/prev(selector)`: return *closest* previous sibling (which matches the selector).

`prevAll()/prevAll(selector)`: return previous siblings (which matches the selector).

`siblings()/siblings(selector)`: return siblings (which matches the selector).

#Part II : CSS, DOM, Events

##CSS Methods

*Apply CSS Properties*: `XX.css(PropertyName, PropertyValue);`. For example, `$("#testId").css("display","none");`

*Apply Multiple CSS Properties*: `.css({key:value, key:value...})`:

    :::javascript
    $('#testId').css({
        "color" : "red",
        "background-color": "blue"
    });

*Apply Width and Height*: `.width(Number)` and `.height(Number)` can be used directly

##DOM Manipulation Methods

*Content Manipulation*: `.html()`. Please refer <a href="/jquery-reading-note-I">Reading Note I</a> for usage.

*DOM Element Replacement*: `XXX.replaceWith(content)`. XXX DOM element is replaced by content.

*DOM Remove*: `XXX.empty()` remove all child elements from XXX elements. `XXX.remove(selector)` remove all matched elemetns from DOM.

*DOM Insert*: `XXX.before(content)` or `XXX.after(content)`.

##Event Handling

###Binding Event Handlers

`selector.bind(eventType, handler)` or `selector.bind(eventTpe, eventData, handler)`

`eventType` is the action, such as `click` or `submit`

`eventData` is *optional*.

`handler` is the function trriger for this event.

###Remove Event Handlers

`selector.unbind(eventType, handler)` or `selector.unbind(eventType)`

`eventType`: same as above

`handler`: the handler that you want to remove

###Event Object and Attributes

`event` can be used as a parameter in handler callback function. There are several attributes that can be retrived by using `event.attributeName`. These attribute name returns useful values.

Example:

    :::javascript
    $('#testId').bind('click',function(event){
        alert(event.type); //here event parameter means the 'click' object
        alert(event.pageX); //type and pageX are attributes for event object
    });

List of Attributes:
images/posts/event-attributes.png 

###Event Methods

`event` parameter can also run some methods to perform specific function. To use it, just do `event.XXX();` in callback function. Here is a list of event methods:
images/posts/event-methods.png 

Please note `preventDefault()` is to prevent current function function working on current element, but `stopPropagation()` is to prevent *parent element's function* working on current element.

###Event Helper Methods

To trigger an event function YY on XX element, just use `XX.YY();`

There are some already defined methods that you can use `XX.YY()` format to add event to XX element. For example, `$("#testId").click(function(){ ... });`. Here is a list:
images/posts/binding-methods.png 

#Part III : Ajax, Effects

##Ajax

AJAX means *Asynchromous JavaScript and XML*. It can help load data from server without having to refresh whole page.

`XX.load(URL, Optional:data, Optional:callback)` is used to load data:

- URL: can be `CGI`, `ASP`, `JSP` or `PHP` script which generate data from database.

- data: *Optional*. if this is ommitted, `GET` method is used. If specified, `POST` method is used.

- callback: callback function to deal with data after loading. The first parameter passed to this function is the *response text* received from the server and second parameter is *status code*.

###Get JSON Data

`XXX.getJSON(URL, Optional:data, Optional:callback)` is used to get JSON string:

- URL: the server-side source which can be reach via `GET` method.

- data: *Optional*. You can pass `name/value` pair to do sring query.

- callback: *Optional*. Call back function to deal with data after loading. The first parameter is the *JSON string* which is passed back based on request. The second parameter is the *status code*.

###Pass Data to Server

You can use `data` parameter to pass data to server via any ajax call. For example:

    :::javascript
    var name = $('#name').val();
    $('#stage').load('/jquery/result.php', {'name':name});

###jQuery Ajax Methods and Events

images/posts/ajax_methods_events.png 

##Events

###Show or Hiding or Toggle Elements

`XXX.show(speed,Optional:callback)` is used to show the elements. `speed` can be `slow`, `normal`, `fast` or any milliseconds. `callback` is optional. You run this function after the animation completes.

`XXX.hide(speed,Optional:callback)` is the same as above:

    :::javascript
    $('#testDIV').hide(10000);

`XXX.toggle(Optional:speed, Optional: callback)` is used to toggel elements.

###Other jQuery Events

images/posts/jquery_events.png 




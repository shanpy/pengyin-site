.. title: JavaScript Tips
.. date: 2015-08-17
.. modified: 2015-08-26
.. category: JavaScript
.. tags: JavaScript, jQuery
.. slug: javascript-tips
.. authors: Pengyin Shan
.. description: This post includes useful JavaScript tips I encourted in daily job, may also contain knowledge in jQuery.

##JavaScript String

###Substring

There are two ways in JavaScript to get substring:

####`substr(StartIndex, Length)`:

Takes two parameter: **StartIndex** and **Length of Substring (Optional)**

####`substring(StartIndex, EndIndex)`

Takes two parameter: **StartIndex (inclusive)** and **EndIndex (exclusive)**. EndIndex is optional.

If "start" is greater than "end", this method will swap the two arguments, meaning str.substring(1,4) == str.substring(4,1).

If either "start" or "stop" is less than 0, it is treated as if it were 0.

> Note: Both methods do not change the original string.

####Special Cases

The two methods above have difference usage for following spceial cases:

**Negative Value**

`substr()` and `substring()` can both take negative value parameters as `StartIndex`, which means starting to count from end of string.

`substr()` can take `Length` parameter as negative number, but it will return a **empty String**.

`substring()` can take `EndIndex` as negative value, but **this value will be ignored, and substring will start from position 0, has same length as Start Index**.
>If you only have one negative index, whole string will be returned, If you have a negative Start Index, nothing will be returned

So, if you want to **take substring from the end of string**, using `substr()`. Start from where your substring start, and length is what you need, or `str.length - startIndex` if you want rest of string.
>Remember you substring has same sequence as original string. It's not reversed.

##JavaScript KeyCode and Related Information

###Two Way of Event Binding

    :::javascript
    $('#inputbox_id').bind('input', function(event){
        //event.keyCode...
    }
    //Second way: you may want keydown/keypress event also
    $('#inputbox_id').on('keyup', function (event) {
    /*
    *When you use copy and paster instead of key input, this way may cause double event trigger, so I prefer the way above
    */
    }

###Common KeyCode

- `Delete`:46

- `Backspace`: 8

- `Enter`: 13

- `Tab`: 9

You can refer this <a href="http://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes">cheatsheet</a> for more keycode information.

###Special Cases

From <a href="http://stackoverflow.com/questions/4084715/javascript-e-keycode-doesnt-catch-backspace-del-in-ie">this stackflow post</a>, IE doesn't fire **keypress** event for delete, end, enter, escape, function keys, home, insert, pageUp/Down and tab. So use **keydown** or **keyup** instead.
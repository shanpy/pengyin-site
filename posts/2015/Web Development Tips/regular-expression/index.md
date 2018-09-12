.. title: Regular Expression
.. date: 2015-08-20
.. category: Web Development Tips
.. tags: JavaScript
.. slug: regular-expression
.. authors: Pengyin Shan
.. description: This post includes information about regular expression. This post will be update when I learn anything new about it.

A JavaScript Regex Cheatsheet <a href="https://www.debuggex.com/cheatsheet/regex/javascript">online</a>.

##JavaScript Regular Expression

###Method

####search

`search()` uses an expression to search for a match, and returns the position of the match. Return `-1` if regular expression not match:

    :::javascript
    var str = "test";
    var n = str.search(/^(test)+$/i); //n=0

####replace

`replace`: search pattern and replace it

    :::javascript
    var str = "test";
    var res = str.replace(/test/i, "new-test");

####test

`test()` searches a string for a pattern, and returns `true` or `false`, depending on the result.

Example code from w3cschool:

    :::javascript
    var patt = /e/;
    patt.test("The best things in life are free!"); //true

####exec

`exec()` searches a string for a specified pattern, and returns **the found text**. If nothing is founded, return `null`.

Example code from w3cschool:

    :::javascript
    /e/.exec("The best things in life are free!"); //e

###Modifiers

- `i`: Perform case-insensitive matching

- `g`: Perform a global match (find all matches rather than stopping after the first match)

- `m`: Perform a mutiline matching

###Escape

Use `\` to **escape** to following items in regular expression: `^`, `$`, `.`, `*`, `+`, `?`, `=`, `!`, `:`, `|`, `\`, `/`, `(`, `)`, `[`, `]`, `{`, `}`

###OR

`[]`: `/[abc]/` means `a` or `b` or `c`

###Except

`[^]`: `/[^abc]/` anything except `a` or `b` or `c`

###Character

`.`: any single character *except next-line and white-space*. i.e. `[^\n\r]`

`\w`: any ASCII single character. i.e. `[a-zA-Z0-9]`

`\W`: any non-ASCII single character. i.e. `[^a-zA-Z0-9]`

`\d`: any digital singe character. i.e. `[0-9]`

`\D`: any non-digital single character. i.e.e `[^0-9]`

`\s`: white-space

`\S`: non-white-space

###Meta Character

`\r`: Assume you hit `Enter` key

`\t`: Tab

`\n`: change new line

`\f`: change page

`\0`: empty character

###Repeat

`{min, max}`: Repeat from min times to max times. Example: `/[test]{4,6}/` means 't' or `e` or `s` or `t` should be repeated at least 4 times and as most 6 times.

`{min,}` or `{,max}`: Repeat at least `min` or at most `max` times. Example: `/[test]{4,}` means 't' or `e` or `s` or `t` should be repeated at least 4 times. No maximum times.

`{n}`: Repeat exactly n times.

`?`: Repeat 0 or 1 times

`+`: Repeat 1 or more times

`*`: Repeat 0 or more times

>when we use `{min,max}`, we may fine more than one corresponding pattern in string. By default result string should be as long as possible. If you want result to be shortest case, add `?` after `{min,max}`

Example from: http://www.cnblogs.com/dolphinX/p/3486214.html:

    :::javascript
    '123456789'.match(/\d{3,5}/g); //["12345", "6789"]
    '123456789'.match(/\d{3,5}?/g); //["123", "456", "789"]

###Group and Border

`^`: Mark start point

`$`: Mark end point

`\b`: all characters except `[a-zA-Z0-9]`

Example from http://www.cnblogs.com/dolphinX/p/3486214.html:

    :::javascript
    (/\w+\b Byron/).test('Hi Byron'); //true
    (/\w+\b Byron/).test('Welcome Byron'); //true
    (/\w+\b Byron/).test('HiByron'); //false

`\B`: opposite from above

`()`: AND. Example: `/(abc)+/` means `abc` or `abcabc` or more.

`|`: OR. Example: `/a|b/` means `a` or `b`

###Frequently Used Regular Expressions

Examples below are taken from <a href="http://kb.cnblogs.com/page/80965/">this post</a>:

- Non-negative Integer: `^\d+$`

- Positive Integer: `^[0-9]*[1-9][0-9]*$`

- Non-positive Integer: `^((-\d+)|(0+))$`

- Negative Integer: `^-[0-9]*[1-9][0-9]*$`

- Integer: `^-?\d+$`

- Non-negative Float: `^\d+(\.\d+)?$`

- Positive Float: `^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$`

- Non-positive Float: `^((-\d+(\.\d+)?)|(0+(\.0+)?))$`

- Negative Float: `^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$`

- Float: `^(-?\d+)(\.\d+)?$`

- String with all letters: `^[A-Za-z]+$`

- String with all upper case letters: `^[A-Z]+$`

- String with all lower case letters: `^[a-z]+$`

- String with number and letters: `^[A-Za-z0-9]+$`

- String with number, letters and underline: `^\w+$`

- **Email Address** validation: `^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$`

- **URL** Validation: `^[a-zA-z]+://` `(\w+(-\w+)*)(\.(\w+(-\w+)*))*(\?\S*)?$`

- **HTML Tag**: `<\s*(\S+)(\s[^>]*)?>(.*?)<\s*\/\1\s*>`

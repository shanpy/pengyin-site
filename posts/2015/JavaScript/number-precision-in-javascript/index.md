.. title: Number Precision in JavaScript
.. date: 2015-09-22
.. category: JavaScript
.. tags: JavaScript
.. slug: number-precision-in-javascript
.. authors: Pengyin Shan
.. description: The post includes the methods to precise numbers in JavaScript.

Following methods is referenced from developer.mozilla.org.

###Number.prototype.toPrecision()

The `toPrecision()` method returns a string representing the Number object to the specified precision.

Example:

    :::javascript
    var test = 1.999
    test.toPrecision() //1.999

    var test2 = 1.511
    test2.toPrecision(1) //2
    test2.toPrecision(2) //1.5

    var test3 = 1.001
    test3.toPrecision(1) //1
    test3.toPrecision(2) //1.0

    var test4 = 0.999
    test4.toPrecision(1) //1
    test4.toPrecision(2) //1.0

###Number.prototype.toFixed()

The `toFixed(parameter)` method formats a number using **fixed-point notation**.

*The parameter may be a value between 0 and 20, inclusive. If no parameter, it is treated as 0.*

This function returns a string representation of the number that **does not use exponential notation and has exactly digits digits after the decimal place**. The number is **rounded** if necessary, and the fractional part is **padded with zeros** if necessary so that it has the specified length.

Example:

    :::javascript
    test = 2.059
    test.toFixed() //2
    test.toFixed(1) //2.1
    test.toFixed(2) //2.06

    test2 = 2e+10
    test2.toFixed(1) //20000000000.0

>toPrecision() is to count the total length. toFixed() is to count length after decimal point.

###Number.prototype.toExponential()

The `toExponential(parameter)` method returns a string representing the Number object in **exponential notation**.

*The parameter specifying the number of digits after the decimal point.*

*If you use the `toExponential()`` method for a numeric literal and the numeric literal has no exponent and no decimal point, **leave a space before the dot** that precedes the method call to prevent the dot from being interpreted as a decimal point.*

Example:

    :::javascript
    test = 2.019
    test.toExponential() //'2.019e+0'
    test.toExponential(1) //'2.0e+0'
    test.toExponential(2) //'2.02e+0'
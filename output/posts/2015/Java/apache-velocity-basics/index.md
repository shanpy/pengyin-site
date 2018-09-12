.. title: Apache Velocity Language Basics
.. date: 2015-11-11
.. category: Java
.. tags: Java, Velocity
.. slug: apache-velocity-basics
.. authors: Pengyin Shan
.. description: This post is a reading notes for <a href="http://velocity.apache.org/engine/releases/velocity-1.7/user-guide.html">Apache Velocity User Guide</a>, with basic information about Apache Velocity's Template Language(**VTL**) information.

##Syntax Basics

All VTL statements, begins with the `#` character. For rendering process: the **Velocity Templating Engine** will:

1. **search** through your web page to find all `#` characters

2. Then **determine** which mark the beginning of VTL statements, and which of the `#` characters that have nothing to do with VTL.

>It is recommended to start each VTL statement on a **new line**.

###References

There are **three** types of references in the VTL: `variables`, `properties` and `methods`.

>In VTL, References begin with $ and are used to **get** something. Directives begin with # and are used to **do** something.

####Variables

All variables/references in VTL begins with the `$` character,followed by a **VTL Identifier**.

- A **VTL Identifier** must start with an alphabetic character (i.e. a to z case insensitive). The rest of the characters are limited to the following types of characters: alphabetic, numeric, `-` or `_`.

In VTL, the variable can get its value from either a **set directive** in the template, or from the **Java code**. Example: for `#set( $foo = "bar" )`, `"bar"` will replace all `$foo` variables in VTL.

Once a value has been assigned to a variable, you can reference the variable **anywhere** in your HTML document. Example:

    :::html
    <html>
    <body>
        #set( $foo = "Velocity" )
        Hello $foo World!
    </body>
    <html>

#####String

String values are always enclosed in *quotes*, either *single* or *double* quotes:

- Single quotes will ensure that the quoted value will be **assigned** to the reference as is.

- Double quotes allow you to use **velocity references and directives** to interpolate

- Example: for `"Hello $name"`, the `$name` will be replaced by the referenced value.

####Properties

Properties have a distinctive format.

The shorthand notation consists of a leading `$` character followed a **VTL Identifier**, followed by a dot character `.` and another **VTL Identifier**

Example: `$customer.Address` has **two meanings**:

1. VTL should look in the **hashtable** named as `customer`, then return the value associated with the **key** `Address`.

2. VTL should find a referring to a **method** called `$customer.getAddress()`.

####Methods

Methods are references that consist of a leading `$` character followed a **VTL Identifier**, followed by a **VTL Method Body**.

A **VTL Method Body** consists of a **VTL Identifier** followed by an left parenthesis character `(`, followed by an **optional parameter list**, followed by right parenthesis character `)`.

Example:

    :::velocity
    $customer.getAddress()
    $purchase.getTotal()
    $page.setTitle( "My Home Page" )
    $person.setAttributes( ["Strange", "Weird", "Excited"] )

#####a *shorthand notation* for **VTL Methods**

In the example above, The **property** `$customer.Address` has the exact same effect as using the **method** `$customer.getAddress()`.

*It is generally **preferable** to use a **Property** when available.*

>The main difference between Properties and Methods is that you can specify a **parameter list** to a Method.

#####Array as Lists

As of Velocity 1.6, all **array** references are treated as **fixed-length lists**. User can call `java.util.List` methods on array references. Example:

    :::velocity
    $myarray.isEmpty()
    $myarray.size()
    $myarray.get(2)
    $myarray.set(1, 'test')

#####vararg methods

From Velocity 1.6, **setter** methods can have different parameter list:

    :::velocity
    $sun.setPlanets('Earth', 'Mars', 'Neptune')
    $sun.setPlanets('Mercury')
    $sun.setPlanets()
    ##  Will just pass in an empty, zero-length array

###Other Syntax Information

####Comments

In VTL, A single line comment begins with `##` and finishes at the end of the line. Example: `## This is a single line comment.`

**Multi-line** comments, which begin with `#*` and end with `*#`, are available to handle this scenario.

    :::velocity
    This is text that is outside the multi-line comment.
    Online visitors can see it.
    *#
     Thus begins a multi-line comment. Online visitors won't
     see this text because the Velocity Templating Engine will
     ignore it.
    *#
    Here is text outside the multi-line comment; it is visible.

User can also set **javadoc-style** annotation in VTL comment block:

    :::velocity
    #**
    This is a VTL comment block and
    may be used to store such information
    as the document author and versioning
    information:
    @author
    @version 5
    *#
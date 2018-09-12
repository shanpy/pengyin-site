.. title: Manning OCA Java SE 7 Reading Note: Chapter 2
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-2
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 2



This is a post that I moved from <a href="blogpengyin.herokuapp.com"> my old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

#Chapter 2: Working with Java Data Types

This chapter main covers:

- **Primitive data** types in Java

- **Literal values** of primitive Java data types

- **Object reference** variables in Java

- Valid and invalid **identifiers**

- Usage of Java **operators**

- Modification of default operator precedence via parentheses

##2.1 Primitivate Variables

A variable defined as one of the primitive data types is a **primary variable**.

Primitive data types is the **simplest data types** in a programming language.

Java has **eight** primitive data types:

- **char**

- **byte**

- **short**

- **int**

- **long**

- **float**

- **double**

- **boolean**

>**String** is not primitive type in Java.

>**char** and **int** are the only short-name primitive data types, with low case as begining, others are all full-name.

>**Integer** or **Character** or **Boolean** is not primitive data type in Java.

Primitive Date Type can be devided to three **categories**:

- Boolean: boolean

- Character: char

- Numeric:

- 1. Integers: int, byte, short, long

- 2. Floating-point/**decimals**: float, double

###boolean

A **literal** is a **fixed** value that does not need further calculations in order for it to be assigned to any varible.

**true** and **false** are the *only* boolean literal variables.

###Numeric

Range of **byte**: `-128` to `127`, inclusive. `8` bits.

The **default type** of a nondecimal number is `int`.

To designate an integer value as a **long** value, just add suffix `L` or `l`: `23333000000L`.

Integer literal values comes in four categories: **binary**, **decimal**, **octal**, and **hexoadecimal**:

- Binary: A **base-2** system. Use prefix `0B` or `0b` to define it: `int b = 0B1110011;`

- Decimal: A **base-10** system. **This is the default setting for `System.out.println()`**.

- Octal: A **base-8** system, which means in octal , `10` has decimal value `9`. Use prefix `0` to define it: `int o = 036620;`

- Hex: A **base-16** system, `A`->`F` means `10->16`. Use `0X` or `0x` to define it.Example: `int h = 0X23232FA;`

In Java7, you can use **underscores**. Underscore has no effect on values: `long oc = 045_13;`

**Rules to Remember**

- You can not **start** or **end** a literal value with an underscore, such as `_100_`

- You can not place an underscore **right after** the prefixes `0b` for binary, `0` for octal and `0x` for hex.

- You can not place an underscre **prior** the an `L` suffix for `long` value

- You can not use an underscore in positions where a **string of digits** is expected, such as `int i = Integer.parseInt("45_98");`. Note this will *compile successfully* but *fail in run time*.

In Java, you use **float** and **double** to store decimal numbers. **float** is smaller and takes less space. **float has less precision**.

The **default type** of a decial litercal is `double` in Java. You can place a **suffix** `f/F` to transfer to to `float` in compile time. a `D/d` suffix can also be used to transfer to `double`, but this can be skipped since `double` is default.

You can also assign **scientific notation** as a literal decimal value:
`double test = 1.4444e4;`

In Java7, you can use **underscore** for floating-points. Rules:

- All rules for *numberic* literals above

- You can not place an underscore **prior** to a `D/d` or `F/f` suffix

- You can not place an underscore **adjacent(i.e. attched before or attched after)** to a `decimal point`: `100_.21` or `89._45`

###char

A char can store a single **16-bit Unicode** character.

Range of char: from `\`u0000` or `0` to `\`ufff` or `65,535`, inclusive.

Use **single quote** for characters. Double quote will fail compile.

Since Java store characters internally as **unsigned integer value (i.e. positivate integer)**, so it's fine to **assign positive integer** to a char. *Negative number will fail to compile, but you can cast*.

>For example: `char a = 122;`, character is transferred to `\`u0122`. The format is first a number based on `10`, then a number that is based on `16`.

>You must use quotes to assign Unicode values to char variables: `char c = '\u0122';`

You can **cast** only capatible data types.

If you cast a negative number for char, the sign will be recognize as a part of numberic value becuase Java does not store sign of an integer.

##2.2 Identifiers

**Indentifiers** are names of packages, classes, interfaces, methods and variables.

**Hyphens (-)** are not allowed in identifier. **Underscotres** are allowed.

###Valid Identifiers

Unlimited length

Starts with a letter ( a–z, upper- or lowercase), a **currency sign**, or an underscore Uses special characters: `!` , `@` , `#` , `%` , `^` , `&` , `*` , `( `, `)` ,`' `, `:` ,`;` , `[` , `/` , `\`` , `}`

Can use a digit (not at the starting position)

Can use an underscore (in **any** position)

Can use a currency sign (in any position): `$` , `£` , `¢` ,`¥` and others

###Invalid Indentifier

Same spelling as a Java reserved word or keyword

Starts with a Java digit ( 0 – 9 )

##2.3 Object Reference Variables

The variables in Java can be categorized into two types: **primitive variables** and **reference variables**.

**Reference variables** are also known as **object reference variables** or **object references**.

**Objects are instances of classes**.

An object reference is a **memory address** that points to a memory area where an object’s data is located.

When an object is instantiated with the new operator, a **heap-memory address** value to that object is returned. That address is usually assigned to the reference variable.

Code Example:

	:::java
	Person person = new Person();

	//Step 1: A new Person object is created
	//Step 2: A variable named person is created in the stack with an empty ( null ) value.
	//Step 3: The variable person is assigned the memory address value where the object is located.

The **literal value** of all types of object reference variables is `null`. You can also assign a `null` value to a reference variable explicitly.

The basic difference is that primitive variables store the **actual values**, whereas reference variables store the **addresses** of the objects they refer to.

##2.4 Operators

###Assignment Operators

The `+=` , `-=` , `*=` , and `/=` operators are short forms of addition, subtraction, multiplication and division with assignment.

You cannot assign larger range of values to smaller range of values. For example: `long num = 188883544333334L; int val = numl` will give complie error. However, opposite and **casting** is allowed.

You cannot assisn `boolean` to other primitive data types.

You can also assign **multiple values** on the **same line** using the
assignment operator and comma: `int a=7, b=5, c=3;`

####Arithmetic Operators

**Unary operators (++/--)** can also be used in **prefix** and **postfix** notation.

>In prefix notation, the unary calculation run first, then closest expression run.

>In postfix notation, closest expression run first, then the unary calcuation run.

>**cloest expression** means the one expression that this variable needs to attend now.

Code example for unaray operators:

	:::java
	int a  = 10;
	a = a++ + a + a-- - a-- + ++a;
	System.out.println(a)

For the code above:

- `a++` means `a=10`, after expression `a=11`. However, there is no expression before this step. **so now totally we have `a=10` as whole function, but the single `a` value on right for next step is `11`**;

- Then `+ a` now means `+ 11`, so now `a = 10 + 11`;

- Then `a--` means first do `+`, then do `--`. So now `a = 10 + 11 + 11`, but single `a` on right side now is `10`.

- Then `a--` means first do `-`, then do `--`. So now `a = 10 + 11 + 11 - 10`, but single `a` on right side now is `9`.

- Then `++a` means first make single `a = 10`, then do `+`. So now `a = 10 + 11 + 11 -10 + 10`

- Now we can hava `a=32` for final printout.

During steps above, the variable assignment is the last step. It needs to waiting for all expressions on right finish.

###Relational Operators

**Relational operators** are used to check one condition, with two categories:

- Comparing greater ( `>` , `>=` ) and lesser values ( `<` , `<=` )

- Comparing values for equality ( `==` ) and nonequality ( `!=` )

The result of the relational operation is always a **boolean** value

The operators `==` (equal to) and `!=`(not equal to) can be used to compare **all types of primitives**: `char` , `byte` , `short` , `int` , `long` , `float` , `double`, and `boolean`.

>Remember that you can’t apply these operators to incomparable types.

###Logical Operators

These expressions should return a **boolean** value.

You can use the logical operators `AND (&&)` , `OR (||)` , and `NOT (!)` to check multiple conditions and proceed accordingly.

>**If there is any false, `&&` always return false;**

>**If there is any true, `||` always return true;**

`&&` and `||` is called **short-circuit operators**, because as long as there is any expression that can decide the result of whole expression (Using the rule above), they will stop evaluating and give out result.

####Operator Precedence

the operator on top has the **highest** precedence, and operators within the same group have the same precedence and are evaluated from
**left to right**:

- `Exp++`,`Exp--`

- `++Exp`, `--Exp`, `+Exp`, `-Exp`, `!`

- `*`, `/`, `%`

- `+`, `-`

- `<`, `>`, `<=`, `>=`

- `==`, `!=`

- `&&`

- `||`  Note OR has lower precedence than AND

- `=`, `+=`, `-=`, `*=`, `/=`, `%=`

- You can use `()` i.e. parentheses to override the default operator precedence.
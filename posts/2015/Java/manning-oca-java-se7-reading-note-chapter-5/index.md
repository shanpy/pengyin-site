.. title: Manning OCA Java SE 7 Reading Note: Chapter 5
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-5
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 5



This is a post that I moved from my <a href="blogpengyin.herokuapp.com">old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

# Chapter 5 Flow Control

This chapter has following content:

- Creating and using `if`, `if-else`, and `switch` constructs to execute statements selectively

- Creating and using `loops—while`, `do-while`, `for`, and `enhanced for`

- Creating `nested construct`s for selection and iteration statements

- Comparing the `do-while`, `while`, `for`, and `enhanced for` loop constructs

- Using `break` and `continue` statements

##If and If-Else

In Java, **`then` isn’t a keyword**, so it shouldn’t be used with the `if` statement.

It’s acceptable to define one course of action for an if construct:

	:::java
	boolean testValue = false;
	if (testValue == true)
	System.out.println("value is true");

	//you can’t define the `else` part for an `if` construct, **skipping the `if` code block**:

	boolean testValue = false;
	if (testValue == true)
	//Won't compile, no content for 'if' but has content for 'else'
	else
	    System.out.println("value is false");
	/**********/
	int score = 100;
	if((score=score+10) > 110);
	//Compile fine. Since no content for `else`, it is fine to skip content for 'if'

Using `if(testValue==true)` is the same as using `if(testValue)`. Similarly, `if(testValue==false)` is the same as using `if(!testValue)`.

An `if` block is marked by enclosing one or more statements within a pair of `curly braces`, `{}`.

An `if` block will execute **a single line of code if there are no braces**, but will execute **an unlimited number of lines** if they’re con- tained within a block (defined using `{}`)

>i.e. In the **absence of a defined code block** (marked with a pair of {}), **only the statement following the if construct** will be considered to be part of it.

	:::java
	String name = "Lion";
	int score = 100;
	if (name.equals("Lion"))
	score = 200;
	    name = "Larry";
	else  //Won't compile. Compiler can't get a if for this else
	score = 129;

The **result** of a variable or an expression used in an `if` construct must evaluate to `true` or `false`.

>i.e. `if(exp)` must have a `boolean` expression.

However, **if you use `=` as assignment in `if` construct, no compile error.** It will become a simple assignment operation.

##Switch Statement

A `switch` statement can define multiple case labels within its switch block, but **only a single `default` label**.
- The default label executes when no matching value is found in
the case labels.

A `break` statement is used to exit a switch statement, after the code completes its execution for a matching case .

When the code control enters the label matching one case in the switch construct, it’ll **execute all of the code until it encounters a `break` statement or it reaches the end of the switch statement.**

You can’t use the `switch` statement to compare all types of values, such as all types of `object`s and `primitive`s. A switch statement accepts arguments of type:

- `char`

- `byte`

- `short`

- `int`

- `String`

- `enum`

- `Character`

- `Byte`

- `Integer`

- `Short`

The `witch` statement **doesn’t accept** arguments of type:

- `long`

- `float`

- `double`

- any `object` besides `String`

Apart from passing a variable to a `switch` statement, you can also pass an `expression` to the `switch` statement **as long as it returns one of the allowed types**:
	:::java
	int score =10, num = 20;
	switch (score+num) {
	// ..code
	}

The value of a `case` label must be a **compile-time constant value**; that is, the value should be known at the time of code compilation:

	:::java
	int a=10, b=20, c=30;
	switch (a) {
	    case b+c: System.out.println(b+c); break; //Not Allowed
	    case 10*7: System.out.println(10*7512+10); break;  //Allowed
	}

You can use **variables in an expression** if they’re marked `final` because the value of final variables can’t change once they’re initialized:

	:::java
	final int a = 10;
	final int b = 20;
	final int c = 30;
	switch (a) {
	    case b+c: System.out.println(b+c); break; //Works fine
	}

	//if you don’t *assign* a value to a `final` variable
	with its declaration, it isn’t considered a compile-time constant**:

	final int a = 10;
	final int b = 20;
	final int c;
	c = 30; //c is not assigned value after initialized, so compile error
	switch (a) {
	    case b+c: System.out.println(b+c); break;
	}

	byte myByte = 10;
	switch (myByte) {
	    //Not compile. Floating-point can't be used for case variable
	    case 1.2: System.out.println(1); break;
	}

Code that tries to compare the variable passed to the `switch` statement with `null` **won’t compile**:

	:::java
	String name = "Paul";
	switch (name) {
	    case "Paul": System.out.println(1);
	    break;
	    case null: System.out.println("null");
	    //Not compile, null can't be a case variable
	}

It’s acceptable to define a **single code block for multiple case labels** in a `switch` statement:

	:::java
	int score =10;
	switch (score) {
	    case 100:  //Works fine. Match case will execute till a break;
	    case 50 :
	    case 10 : System.out.println("Average score");
	    break;
	    case 200: System.out.println("Good score");
	}

In the absence of the `break` statement, control will **fall through
the remaining code and execute the code corresponding to all the remaining cases that follow that matching case**.

##For Loop

Code Structure:

	:::java
	for (initialization; condition; update) {
	    statements;
	}

You can consider the `update` clause to be **a last statement in the for loop**.

The `initialization` section, which executes only once, may define **multiple initialization statements**.

The `update` clause may define **multiple statements**. But there can be **only one `termination` condition** for a `for` loop.

Code Example:

	:::java
	public class DemonstrateFor {
	    public static void main(String args[]) {
	    int ctr = 12;
	    //mutiple initialization and mutiple update, only one termination, which is j<=k
	    for ( int j=10, k=14; j <= k; ++j, k=k-1, ctr--)
	        {
	           System.out.println(j+":"+k+":"+ctr);
	        }
	    }
	}

###Block Variables

An `initialization` block executes **only once**.

A `for` loop can declare and initialize multiple variables in its initialization block, but **the variables it declares should be of the same type**:

	:::java
	//Won't compile
	for (int j=10, long longVar = 10; j <= l; ++j) { }

The scope of the variables declared in the `initialization` block is **limited to the `for` block**.

For example, the variable `j` above cannot be used outside of `for` loop.

The `termination` condition is evaluated **once** for each iteration **before executing the statements defined within the body of the loop**.


Code defined in `update` block executes **after all the code defined in the body of the `for` loop**.

**Mutiple** `udpate` statements will execute **in the order in which
they appear**, at the **end** of all the statements defined in the `for` block.

`Update` block can also call **method**s:

	:::java
	for (int i=0; i < line.length(); ++i, printMethod()) //works fine
	    System.out.println(line.charAt(i));
	}

###Nested For Loop

The loop that encloses another loop is called the `outer loop`, and the enclosed loop is called the `inner loop`.

##The Enhanced For Loop

The `enhanced for loop` is also called the `for-each` loop, and it offers some advantages over the regular for loop.

You can read the colon ( `:` ) in a for- each loop as **“in”**.

Code Example:

	:::java
	for (String val : myList)
	    System.out.println(val);

**What happens when you try to modify the value of the loop variable in an `enhanced for loop`?**

>The result depends on whether you’re iterating through a collection of `primitive` values or `objects`.

>If you’re iterating through an array of `primitive` values, manipulation of the loop variable will **never change the value** of the array being iterated because the primitive values are passed by value to the loop variable in an enhanced for loop.

>When you iterate through a collection of `objects`, the value of the collection is **passed by reference** to the loop variable. Therefore, **if the value of the loop variabl is manipulated by executing methods on it, the modified value will be reflected** in the collection of objects being iterated.

>Example:

	:::java
	StringBuilder myArr[] = {
	    new StringBuilder("Java"),
	    new StringBuilder("Loop")
	};
	for (StringBuilder val : myArr)
	    System.out.println(val);
	for (StringBuilder val : myArr)
	    val.append("Oracle"); //append() means you edit var in myArr
	for (StringBuilder val : myArr)
	    System.out.println(val); //JavaOracle LoopOracle

	/*************/
	StringBuilder myArr[] = {
	    new StringBuilder("Java"),
	    new StringBuilder("Loop")
	};
	for (StringBuilder val : myArr)
	    System.out.println (val);
	for (StringBuilder val : myArr)
	    //This just make sure make StringBuild("Oracle") pointing to same address as val
	    //So it is not a manipulating operation !
	    val = new StringBuilder("Oracle");
	for (StringBuilder val : myArr)
	    System.out.println (val); //Java Loop

A `nested loop` executes all its iterations for each single iteration of its immediate outer loop.

####Limitations of the enhanced for loop

Can't be used to **initialize** an `array` and **modify** its elements

Can't be used to **delete** or **remove** the elements in a collection:

>Because the `for` loop **hides the iterator** used to iterate through the elements of a collection, you can’t use it to remove or delete the existing collection values because you **can’t call the remove method**.

>If you assign a `null` value to the loop variable, **it won’t remove the element from a collection**:

	:::java
	for (StringBuilder val : myList)
	    val = null; //Won't remove. Just change variable to null

Can't be used to **iterate over multiple `collection`s or `array`s in the same loop**

You can’t iterate over multiple collections or arrays in the same `for-each` loop because the `for-each` loop allows for the **creation of only one looping variable**.

Unlike the regular for loop, you **can’t define multiple looping variables** in a `for-each` loop.

###The while and do-while loops

The `while` loops checks its condition before evaluating its loop body, and the `do-while` loop checks its condition **after executing the statements** defined in its loop body.

###while Loop

This loop checks the condition **before** it starts the execution of
the statement.

The condition used in the while loop to check whether or not to
execute the loop body again **should evaluate to `false` at some point in time**; otherwise, the loop will **execute indefinitely**.

Example:

	:::java
	//This code works fine
	int num = 9;
	boolean divisibleBy7 = false;
	//if condition values true, which is the case here, get into loop
	while (!divisibleBy7) {
	    System.out.println(num);
	    if (num % 7 == 0) divisibleBy7 = true;
	    --num;
	}
	//Print out: 9 8 7

###do-while loop

This loop checks the condition **after it completes the execution of all the statements in its loop body**.

**Don’t forget to use a semicolon ( `;` ) to end the `do-while` loop after specifying its condition**.

Code Example:

	:::java
	int num = 9;
	boolean divisibleBy7 = false;
	do {
	    System.out.println(num);
	    if (num % 7 == 0) divisibleBy7 = true;
	    num--;
	} while (divisibleBy7 == false);
	//Print out: 9 8 7

You can use the curly braces `{}` with `while` and `do-while` loops to define multiple lines of code to execute for every iteration.

Without the use of curly braces, **only the first line of code will be considered a part of the `while` or `do-while` loop**

##Comparing Loop Constrcuts

The `do-while` loop executes the code **at least once**.

	:::java
	int num=10;
	do {
	    num++; //num = 11
	} while (++num > 20); //num =12, then evaluate
	System.out.println (num);
	//Print out: 12
	/**************/
	int num=10;
	while (++num > 20) { //First, num = 11, then evaluate
	    num++;
	}
	System.out.println(num);
	//Print out: 11

##Loop Statements: break and continue

###break

The `break` statement is used to **exit** — or **break out of** —the `for`, `for-each`, `do` , and `do-while` loops, as well as `switch` constructs.

Alternatively, the `continue` statement can be used to
***skip* the remaining steps in the current iteration and *start* with the next loop iteration**.

When you use the `break` statement with `nested loop`s, **it exits the `inner loop`**.

**`if` is not a loop!**

Code Example:

	:::java
	String[] programmers = {"Paul", "Shreya", "Selvan", "Harry"};
	for (String name : programmers) {
	    if (name.equals("Shreya"))
	        break;
	    System.out.println(name);
	}
	//Print out: Paul

###continue

The `continue` statement is used to **skip** the remaining steps in the current iteration and **start** with the next loop iteration.

As soon as a loop encounters `continue` , it **exits the current iteration** of the loop

Unlike the `break` statement, `continue` doesn’t exit the loop — it **restarts** with the next loop iteration

When you use the `continue` statement with nested loops, it exits the current iteration of the **inner loop.**

Code Example:

	:::java
	String[] programmers = {"Paul", "Shreya", "Selvan", "Harry"};
	for (String name : programmers) {
	    if (name.equals("Shreya"))
	        continue; //Re-start for loop from next programmers
	    System.out.println(name);
	}
	//Print out: Paul Selvan Harry

###Labeled Statements

In Java, you can add `label`s to the following types of statements:

- A code block defined using `{}`

- All looping statements ( `for`,`enhanced for`,`while`,`do-while` )

- Conditional constructs ( `if` and `switch` statements)

- Expressions

- Assignments

- `return` statements

- `try` blocks

- `throws` statements

Code Example:

	:::java
	String[] programmers = {"Outer", "Inner"};
	outer: //This is a label
	for (int i = 0; i < programmers.length; i++) {
	}

You **can’t add labels to `declaration`s**. For example, `outer : int[] myArray = {1,2,3};` won't compile.

**previous declaration** can be defined within a `block` statement:

	:::java
	outer : //Label with a block
	{
		int[] myArray = {1,2,3};
	}

You can use a labeled `break` statement to **exit an outer loop**:

	:::java
	String[] programmers = {"Outer", "Inner"};
	outer:
	for (String outer : programmers) {
	    for (String inner : programmers) {
	        if (inner.equals("Inner"))
	            break outer; //Add label name to exit such loop
	    System.out.print(inner + ":");
	    }
	}

You can use a labeled `continue` statement to **skip an iteration of the outer loop**:

	:::java
	String[] programmers = {"Paul", "Shreya", "Selvan", "Harry"};
	outer:
	    for (String name1 : programmers) {
	        for (String name : programmers) {
	            if (name.equals("Shreya"))
	            continue outer;
	        System.out.println(name);
	        }
	}
	/**Process:
	* name1 = Paul, name= Paul, print Paul;
	* name1 = Paul, name= Shreya, re-start outer
	* name1 = Shreya, name = Paul, print Paul;
	* name1 = Shreya, name = Shreya, re-start outer;
	* ...
	* Total print-out: Paul, Paul, Paul, Paul
	**/
.. title: Manning OCA Java SE 7 Reading Note: Chapter 7
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-7
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 7



This is a post that I moved from <a href="blogpengyin.herokuapp.com"> my old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

#Chapter 7: Exception Handling

This chapter mainly covers:

- Understanding and identifying exceptions arising in code

- Determining how exceptions alter the normal program flow

- Understanding the need to handle exceptions separately in your code

- Using `try-catch-finally` blocks to handle exceptions

- Differentiating among `checked exception`s, `unchecked exception`s, and `error`s

- Invoking methods that may throw exceptions

- Recognizing common exception categories and classes

When JVM reposts exceptions, Stack traces are read **from the bottom**.

##7.2 What happens when an exception is thrown?

As with all other Java objects, **an exception is an object**. All types of exceptions subclass `java.lang.Throwable`.

An operating system (OS) keeps track of the code that it needs to execute using a `stack`. A stack is a type of list in which the items that are added last to it are the first ones to be taken off it—**Last In First Out**. This stack uses a `stack pointer` to point to the instructions that the OS should execute.

When a stack pointer finds an exception should be throwed out in one method, it will check if this methos has a **error handler**. If not, go and find upper level.

For example, if method call a method1 then call a method2, And a `IndexOutOfBounds` error should be throwed out in method2, but method2 doesn't have a error handler, stack pointer will find method1 -> main.

If there are no further methods that handle `ArrayIndexOutOfBoundsException`, execution stops.

###Creating try-catch-finally blocks

Try what?

>First you try to execute your code. If it doesn’t execute as planned, you handle the exceptional conditions using a catch block.

Catch what?

>You catch the **exceptional event** arising from the code enclosed within the try block and handle the event by defining appropriate exception handlers.

What does finally do?

>Finally, you execute a set of code, in all conditions, **regardless of whether the code in the try block throws any exceptions**.

>You can create an exception of your own—a **custom exception**—by extending the class `Exception`.

For a try block, you can define **multiple catch blocks**

But **only a single finally block**.

Multiple catch blocks are used to handle different types of exceptions. - A finally block is used to define cleanup code—code that closes and releases resources, such as file handlers and database or network connections.

###Will a finally block execute even if the catch block defines a return statement?

**Yes**. The `return` statement does not return the control to the main method before execution of the finally block completes.

###What happens if both a catch and a finally block define return statements?

If both catch and finally blocks define return statements, the calling method will receive a value from the `finally` block.

###What happens if a finally block modifies the value returned from a catch block?

If a catch block returns a **primitive data type**, the finally block **can’t modify the value** being returned by it. *Note: in this case, finally block does not return anything*.

Example:

	:::java
	class MultipleReturn {
	    int getInt() {
	        int returnVal = 10;
	            try {
	                	String[] students = {"Harry", "Paul"};
	                System.out.println(students[5]);
	                 }
	        catch (Exception e) {
	                ￼￼￼￼System.out.println("About to return :" + returnVal);
	                	return returnVal;
	                }
	        finally {
	            	returnVal += 10;
	        ￼￼￼￼    System.out.println("Return value is now :" + returnVal);
	        }
	        	return returnVal;
	        }
	        public static void main(String args[]) {
	            MultipleReturn var = new MultipleReturn();
	            System.out.println("In Main:" + var.getInt());
	    } }

	//- Output will be:
	//About to return :10
	//Return value is now :20
	//In Main:10

Even though the **finally** block adds `10` to variable `returnVal`, **this modified value is not returned to the method main** . Control in the catch block **copies** the value of `returnVal` to be returned before it executes the finally block, so **the returned value is not modified when finally executes**.

**Important:** the value **inside finally block changed**. So if you return **inside** finally block, the value passed to `main` will be changed

If a catch block returns a **object**, When the finally block executes, it **can access** the value of the object referred to by the variable and **can modify** it. **The modified value is returned to the method main**.

Remember that **primitives are passed by value and objects are passed by reference**.

###Does the order of the exceptions caught in the catch blocks matter?

Order doesn’t matter for unrelated classes. But it does matter for related classes sharing an `IS-A` relationship.

If you try to catch an exception of the **base class before an excep- tion of the derived class** , the exception handler for the derived class can never be reached, so your code will **fail to compile**.

Code Example:

	:::java
	try {
	    fis = new FileInputStream("file.txt");
	    fis.close();
	}
	catch (IOException ioe) {
	    System.out.println("IOException");
	}
	catch (FileNotFoundException fnfe) {
	    System.out.println("file not found");
	}

In the code above, since `FileNoteFoundException` is a derived class from `IOException`, `FileNoteFoundException` should be catched **before** `IOException`, otherwise code will not compile.

**Rules to Remember**

- A `try` block may be followed by **multiple** `catch` blocks

- the `catch` blocks may be followed by a **single** `finally` block.

- A `try` block may be followed by **either** a `catch` or a `finally` block or **both**. But a `finally` block alone wouldn’t **suffice** if code in the try block throws a checked exception. In this case, you need to catch the checked exception or declare it to be thrown by your method. Otherwise **your code won’t compile**.

- The `try`, `catch`, and `finally` blocks can’t exist **independently**.

- The `finally` block **can’t appear `before` a catch block**.

- A `finally` block **always executes**, regardless of whether the code throws an exception.

###Can I rethrow an exception or the error I catch

You can do whatever you want with an exception.

Rethrow example:

	:::java
	try {
	    soccer = new FileInputStream("soccer.txt");
	}
	catch (FileNotFoundException fnfe) {
	    throw fnfe; //re-throw error without handler. Will not compile
	}

When you rethrow a checked exception, it’s treated like a regular thrown checked exception, meaning that all the rules of handling a checked exception apply to it. **So after you re-throw, you still need a error handler or a `throw` argument to handle error, otherwise your code will not compile.**

However, You can rethrow a `runtime exception`, but **you’re not required to catch it**, nor must you modify your method signature to include the throws clause

###Can I declare my methods to throw a checked exception, instead of handling it?

If a method doesn’t wish to handle the checked exceptions thrown by a method it calls, it can **throw** these exceptions using the `throws` clause in its own method signature.

For example: `public void myMethod() throws IOException{...}`

###I can create nested loops, so can I create nested try-catch blocks too?

**Yes**. you can define a `try-catch-finally` block within another `try-catch-finally` block.

##7.3 Categories of Exceptions

There are **three** categories of Exceptions:

- `Checked exceptions`

- `Runtime exceptions` (`unchecked exceptions`)

- `Errors`

**you shouldn’t try to catch runtime exceptions**, and there are few options you can use for the **errors**, because **they’re thrown by the JVM**.

###Checked exceptions

A `checked exception` is an unacceptable condition **foreseen** by the author of a method but outside the immediate control of the code.

A`checked exception` is a **subclass** of class `java.lang.Exception`, but it’s **not a subclass** of `java.lang.RuntimeException`.

If a method uses another method that may throw a checked exception, one of the two following things should be true:

- The method should be enclosed within a `try-catch` block or

- The method should specify this exception to be thrown in its **method signature**, i.e. `throws XXXException`

###Runtime Exception/Unchecked Exception

A `runtime exception` is a representation of a **programming error**. These occur from **inappropriate use** of another piece of code.

A runtime exception is a **subclass** of `java.lang.RuntimeException`.

A runtime exception **may not be a part of the method signature**, even if a method may throw it. i.e. You may not need a `throws`.

However, you **can** create a error handler for runtime exception.

###Errors

The `error`s are considered to be **serious exceptional condition**s and they **can’t be directly controlled by your code**.

An `error` is a serious exception thrown by the **JVM** as a result of an error in the **environment state** that processes your code.

An error is a **subclass** of class `java.lang.Error`.

An error **need not** be a part of a method signature.

An error **can be** caught by an `exception handler`, but it **shouldn’t** be.

##7.4 Common Exception Classes and Categories

**Common Runtime Exceptions**

- `ArrayIndexOutOfBoundsException`

- `IndexOutOfBoundsException`

- `ClassCastException`

- `IllegalArgumentException`

- `IllegalStateException`

- `NullPointerException`

- `NumberFormatException`

**Common Errors**

- `ExceptionInInitializerError`

- `StackOverflowError`

- `NoClassDefFoundError`

- `OutOfMemoryError`

###ArrayIndexOutOfBoundsException and IndexOutOfBoundsException

`ArrayIndexOutOfBoundsException` and `IndexOutOfBoundsException` are **runtime exceptions**, which share an `IS-A` relationship. `IndexOutOfBoundsException` is **subclassed** by `ArrayIndexOutOfBoundsException`.

`ArrayIndexOutOfBoundsException` is thrown when a piece of code **tries to access an `array` out of its bounds** (either an array is **accessed at a position less than 0 or at a position greater than or equal to its length**).

`IndexOutOfBoundsException` is thrown when a piece of code tries to **access a `list`**, like an ArrayList, using an **illegal index**.

Reason for these two runtime exception is: a variable is used to specify this array or list position, and **its value may not be known until runtime**.

####ClassCastException

`ClassCastException` is thrown when an object fails an `IS-A` test with the class type to which it’s being cast.

Code Example:

	:::java
	ArrayList<ColorInk> inks = new ArrayList<ColorInk>();
	inks.add(new ColorInk());
	Ink ink = (BlackInk)inks.get(0);
	//Can throw ClassCastException error if BlackInk has no relation with ColorInk

You can use the `instanceof` operator to **verify** whether an object can be cast to another class before casting it: `inks.get(0) instanceof BlackInk`

####IllegalArgumentException

`IllegalArgumentException` is thrown to specify that a method has **passed illegal or inappropriate arguments**.

###IllegalStateException

an `IllegalStateException` happens if the Java environment or Java application is **not in an appropriate state for the requested operation**.

You can throw `IllegalStateException` to signal to the calling method that the method being requested for execution **can’t be called** for the current state of an object.

For example, you can set if `int a !=0`, then throw `IllegalStateException`.

###NullPointerException

This exception is thrown by the **JVM** if you try to access a method or a variable with **a null value**

Cases can be the following:

- Accessing members of a reference variable that is **explicitly assigned a `null` value**.

- Accessing members of an **uninitialized** `instance` or `static` reference variable. These are **implicitly assigned a `null` value**.

- Using an **uninitialized** `local variable`, which may seem to throw a `NullPointerException`.

- Attempting to access **nonexistent array positions**. Note the difference between `ArrayOutOfBoundException` and `NullPointerException`

- Using members of an `array` element that are **assigned a `null` value**.

Code Example:

	:::java
    static ArrayList<String> list = null; //No initialization
    public static void main(String[] args) {
        list.add("1"); //NullPointerException
    }

**By default, the `static` and `instance` variables of a class are assigned a `null` value.**

You can prevent a `NullPointerException` from being thrown by checking **whether an object is null** before trying to access its member.

**Important:** If you attempt to use an **uninitialized** `local variable`, your code will fail to compile.

For example, following code will not compile:

	:::java
    ArrayList<String> list;
    if (list!=null)
    list.add("1");

**Important**: for `array`, `NullPointerException` only throws if you want to **do something** with a null array space or **access** a non-exisit positon (For example, a **non-initialized** `static/instance` array).

Example:

	:::java
	class ThrowAnotherNullPointerException {
	    static String[] oldLaptops;
	    public static void main(String[] args) {
	        System.out.println(oldLaptops[1]); //NullPointerException

	        String[] newLaptops = new String[2];
	        //Note if there is no initialization, code will not compile

	        System.out.println(newLaptops[1]); //Print null
	        System.out.println(newLaptops[1].toString());
	        //NullPointerException
	    }
	}

###NumberFormatException

`NumberFormatException` is a runtime exception. It’s thrown to indicate that the application has tried to **convert a string (with an inappropriate format) to one of the numeric types**.

For example: Starting in Java 7, you can use underscores`_` in numeric literal values. But you can’t use them in String values passed to the method `parseInt()`. So if you do `Integer.parseInt("123_45")`, you will get `NumberFormatException`.

Note: `Integer.parseInt("123ABCD", 16)` is valid, since this is the way to parse hex number. If you remove `16`, a `NumberFormatException` will throw since you cannot covert it to **base 10**.

###ExceptionInInitializerError

The `ExceptionInInitializerError` error is typically thrown by the **JVM** when a `static initializer` in your code throws any type of `RuntimeException`.

This error always goes with `runtime exception`. It can’t occur as the result of an `error` or `checked exception` thrown by the `static` initialization block.

`Runtime exception`s arising from any of the following will throw this error:

- Execution of an **anonymous `static` block**

- **Initialization** of a `static` variable

- Execution of a `static` method (called from either of the previous two items)

For example, following code will throw this error, with `NumberFormatInitializerError`:

	:::java
	public class DemoExceptionInInitializerError {
	            static {
	                int num = Integer.parseInt("sd", 16);
	                //anoymous static block with runtime exception
	            }

	            public class DemoExceptionInInitializerError1 {
	                static String name = null;
	                static int nameLength = name.length();
	           //Initialization of a static variable with NullPointerException
	            }
	}

###StackOverflowError

This error is thrown by the **JVM** when a Java program **calls itself** so many times that the memory stack allocated to execute the Java program “overflows.”

For example, a infinate loop can cause this error

###NoClassDefFoundError

`NoClassDefFoundError` can throw if:

- If you **failed to set your classpath** and, as a result, the JVM was unable to load the class that you wanted to access or execute.

- If you try to run your application before compiling it.

Note, `Class.forName()` methods, which is used to load class, throws `ClassNotFoundException` instead of this error.

####OutOfMemoryError

the JVM may **run out of memory on the heap**, and the garbage collector may **not be able to free more memory for the JVM**. In this case, the JVM is unable to create any more objects on the heap. An `OutOfMemoryError` will be thrown.
.. title: Important Q&A for OCA Java SE7 Certification Guide
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: key-qas-for-oca-book
.. authors: Pengyin Shan
.. description: This post records all Q&As which are important and be easy to make mistake for me. Most of Q&As are taken from OCA Java SE 7 Certification Guide from Manning.



##Q&As from Chapter 1, OCA Guide from Manning

###Q1: which code(s) can be complied as `main` method?

a.

	:::java
	class EJava {
	public static void main(String sun[]) {
	    System.out.println(sun[0] + " " + sun[2]);
	}
	}

b.

	:::java
	class EJava {
	static public void main(String phone[]) {
	    System.out.println(phone[0] + " " + phone[1]);
	}
	}

c.

	:::java
	class EJava {
	static public void main(String[] arguments[]) {
	    System.out.println(arguments[0] + " " + arguments[1]);
	}
	}

d.

	:::java
	class EJava {
	static void public main(String args[]) {
	    System.out.println(args[0] + " " + args[1]);
	}
	}


A1: a,b

>The problem of c is `main` method only accept one-dimention String array.

>The problem of d is **only `public` and `static` can change position. `void` must be the last modifier for `main` method*.*

###Q2: Which of the following examples define the correct Java class structure?

a.

	:::java
	#connect java compiler;
	#connect java virtual machine;
	class EJavaGuru {}

b.

	:::java
	package java compiler;
	import java virtual machine;
	class EJavaGuru {}

c.

	:::java
	import javavirtualmachine.`*`;
	package javacompiler;
	class EJavaGuru {
	    void method1() {}
	    int count;
	}

d.

	:::java
	package javacompiler;
	import javavirtualmachine.*; class EJavaGuru {
	          void method1() {}
	            int count;
	}

e.

	:::java
	#package javacompiler; $import javavirtualmachine; class EJavaGuru {
	          void method1() {}
	int count;
	}

f.

	:::java
	package javacompiler; import javavirtualmachine; Class EJavaGuru {
	          void method1() {}
	int count;
	}


A2: d

>Problem of f is : **Java is case-sensitive**.

###Q3. Which of the following options, when inserted at //INSERT CODE HERE, will print out EJavaGuru?

	:::java
	public class EJavaGuru {
	    // INSERT CODE HERE
	    {
	        System.out.println("EJavaGuru");
	    }
	}

- a. `public void main (String[] args)`

- b. `public void main(String args[])`

- c. `static public void main (String[] array)`

- d. `public static void main (String args)`

- e. `static public main (String args[])`

A3: c

>**Extra space is ignored by java compiler**.

###Q4: Given the following code, select the correct options:

	:::java
	package com.ejavaguru.courses;
	class Course {
	    public String courseName;
	    public void setCourseName(private String name) {
	        courseName = name;
	    }
	}

- a. You can’t define a method argument as a private variable.

- b. A method argument should be defined with either public or default accessibility.

- c. For overridden methods, method arguments should be defined with protected accessibility.

- d. None of the above.

A4: a

>**Method argument cannot have any access modifier**.

##Q&As from Chapter 2, OCA Guide from Manning

###Q1. Let’s use the primitive variables baseDecimal, octVal, hexVal, and binVal defined earlier in this section and introduce additional code for printing the values of all these variables. Determine the output of the following code:

	:::java
	class TwistInTaleNumberSystems {
	public static void main (String args[]) {
	        int baseDecimal = 267;
	        int octVal = 0413;
	        int hexVal = 0x10B;
	        int binVal = 0b100001011;
	        System.out.println (baseDecimal + octVal);
	        System.out.println (hexVal + binVal);
		}
	}


A1: 267, 267

>`System.out.println()` always print out decimal value so all oct, hex and binaray needs to be changed to decimal value. Note the way to calculate binary is use the n square of 2.

###Q2. Select all incorrect statements:

a. A programmer can’t define a new primitive data type.

b. A programmer can define a new primitive data type.

c. Once assigned, the value of a primitive can’t be modified.

d. A value can’t be assigned to a primitive variable.

A2: b,c,d

>Note you **can modify value of primary type after it is assigned**.

###Q3. Which of the operations are correct for the following code?

	:::java
	public class Prim { //line1
	  public static void main(String[] args) { //line 2
	  char a = 'a'; //3
	  char b = -10; //4
	  char c = '1'; //5
	  integer d = 1000; //6
	  System.out.println(++a + b++ * c - d); //7
	  }
	  }

a. Code at line 4 fails to compile.

b. Code at line 5 fails to compile.

c. Code at line 6 fails to compile.

d. Code at line 7 fails to compile.

A3: a,c,d

>Note `Integer` is *not* a valid java primary data type!

###Q4. Which of the following options contain correct code to declare and initialize variables to store whole numbers?

a. bit a=0;

b. integer a2 = 7;

c. long a3 = 0x10C;

d. short a4 = 0512;

e. double a5 = 10;

f. byte a7 = -0;

g. long a8 = 123456789;

A4: c,d,f,g

>Note `double` can *only* store **decimal** value. Also `byte a7 = 0` is valid.

>`bit` and `integer` are not primary data type for java.

###Q5.  If the functionality of the operators = and > were to be swapped in Java (for the code on line numbers 4, 5, and 6), what would be the result of the following code?

	:::java
	boolean myBool = false;
	int yourInt = 10;
	float hisFloat = 19.54f;
	System.out.println(hisFloat > yourInt);
	System.out.println(yourInt = 10);
	System.out.println(myBool > false);

a. true true false

b. 10.0 false false

c. false false false

d. Compilation error

A5: b

>`swapped` means change the function of `=` and `>`. Note `System.out.println(assignment expression)` is acceptable in Java.

###Q&As from Chapter 3, OCA Guide from Manning

###Q1: Which of the following methods correctly accepts three whole numbers as method arguments and returns their sum as a decimal number?

a.

	:::java
	public void addNumbers(byte arg1, int arg2, int arg3) {
	double sum = arg1 + arg2 + arg3;
	}

b.

	:::java
	public double subtractNumbers(byte arg1, int arg2, int arg3) {
	double sum = arg1 + arg2 + arg3;
	return sum;
	}

c.

	:::java
	public double numbers(long arg1, byte arg2, double arg3) {
	return arg1 + arg2 + arg3;
	}

d.

	:::java
	public float wakaWakaAfrica(long a1, long a2, short a977) {
	double sum = a1 + a2 + a977;
	return (float)sum;
	}


A1: b,d

>On option d, note that `double` can accept `long` and `short` assignment. There is no data size problem.

###Q2: Which of the following statements are true?

a. If the return type of a method is `int` , the method can return a value of type `byte` .

b. A method may or may not return a value.

c. If the return type of a method is void , it can define a return statement without a value, as follows: `return;`

d. A method may or may not accept any method arguments.

e. A method must accept at least one method argument or define its return type.

f. A method whose return type is String can’t return `null`.


A2: a, b, c, d

>Note for opation a, since `byte` can be transferred succesfully to `int` without casting, it is safe to return `byte`.

###Q3: Given the following code,

	:::java
	class Course {
	    void enroll(long duration) {
	    System.out.println("long");
	    }
	    void enroll(int duration) {
	    System.out.println("int");
	    }
	    void enroll(String s) {
	    System.out.println("String");
	    }
	    void enroll(Object o) {
	    System.out.println("Object");
	    }
	}

what is the output of the following code?

	:::java
	class EJavaGuru {
	    public static void main(String args[]) {
	    Course course = new Course();
	    char c = 10;
	    course.enroll(c);
	    course.enroll("Object");
	    }
	}

a. Compilation error

b. Runtime exception

c. "int" "String"

d. "long" "Object"

A3: c

>About using `Object` parameter here: although `Object` is a generally type of other type, since there exist other methods that take more **sepecified parameter**, there will be not runtime error.

>The way to get c option is:
- Java found `char` can use methods that have parameter type `int` and `long`.
- Java found **closest** type for char is `int`, so Java call method which takes `int`.

###Q4: Select the incorrect options:

a. If a user defines a private constructor for a public class, Java creates a public default constructor for the class.

b. A class that gets a default constructor doesn’t have overloaded constructors.
c. A user can overload the default constructor of a class.

d. The following class is eligible for a default constructor:

	:::java
	class EJava {}
	```
	- e. The following class is also eligible for a default constructor:
	```
	class EJava {
	void EJava() {}
	}

A4: a,c

>**Note we need incorrect options here!**

>- b is right, **Default controller can not exist as the same time as user-defined controller**, so it doesn't have overloaded constructors.

>- c is not right, similarly, we can not overload default controller becuase if we do, the default controller will disappear.

##Q&As from Chapter 7, OCA Guide from Manning

###Q1: Examine the following code and select the correct option(s):

	:::java
	class EJavaGuruExcep2 {
	public static void main(String args[]) {
	EJavaGuruExcep2 var = new EJavaGuruExcep2();
	var.printArrValues(args);
	}
	void printArrValues(String[] arr) {
	try {
	System.out.println(arr[0] + ":" + arr[1]);
	}
	catch (NullPointerException e) {
	System.out.println("NullPointerException");
	}
	catch (IndexOutOfBoundsException e) {
	System.out.println("IndexOutOfBoundsException");
	}
	catch (ArrayIndexOutOfBoundsException e) {
	System.out.println("ArrayIndexOutOfBoundsException");
	}
	}
	}

a. If the class EJavaGuruExcep2 is executed using the following command, it prints `NullPointerException` : javaEJavaGuruExcep2

b. If the class EJavaGuruExcep2 is executed using the following command, it prints `IndexOutOfBoundsException` : javaEJavaGuruExcep2

c. If the class EJavaGuruExcep2 is executed using the following command, it prints `ArrayIndexOutOfBoundsException`: javaEJavaGuruExcep2one
d. The code will fail to compile.

A1: d

>**If you try to catch an exception from its dervied class after the exception of base class, the code will note compile.**

>Here `ArrayIndexOutOfBoundsException` is a derived class of `IndexOutOfBoundsException`, so it should be throwed out first. The code will fail to compile otherwise.

###Q2: What is the output of the following code?

	:::java
	class EJava {
	void method() {
	try {
	guru();
	return;
	}
	finally {
	System.out.println("finally 1");
	}
	}
	void guru() {
	System.out.println("guru");
	throw new StackOverflowError();
	}
	public static void main(String args[]) {
	EJava var = new EJava();
	var.method();
	}
	}

a. guru finally 1

b. guru finally 1 Exception in thread "main" java.lang.
StackOverflowError

c. guru Exception in thread "main" java.lang.StackOverflowError

d. guru

e. The code fails to compile.

A2: b

>`throw` in code means **an exception must be throwed out**

###Q3: What is the output of the following code?

	:::java
	class TryFinally {
	int tryAgain() {
	int a = 10;
	try {
	++a;
	}
	finally {
	a++;
	}
	return a;
	}
	public static void main(String args[]) {
	System.out.println(new TryFinally().tryAgain());
	}
	}

a. 10

b. 11

c. 12

d. Compile Error

e. Runtime Error

A3. c

>- It is OK to have `try` block **without** a `catch` block.
>- "Primary Number Passing Problem" only happens if there is any `return` in `try/catch` block. Here since the only `return` is at the end of method, both `try` and `finally` are able to modify value.
>- Note if there is a `return` at the end of method block, `try` and `catch` cannot have `return` at the same time.

###Q4: Which of the following statements are true?

a. A user-defined class may not throw an `IllegalStateException` . It must be thrown only by Java API classes.

b. `System.out.println` will throw `NullPointerException` if an uninitialized instance variable of type String is passed to it to print its value.

c. `NumberFormatException` is thrown by multiple methods from the Java API when invalid numbers are passed on as String s to be converted to the specified number format.

d. `ExceptionInInitializerError` may be thrown by the JVM when a static initializer in your code throws a `NullPointerException`.

A4. c,d

>Note the problem of `b` is `System.out.println` will print `null` in option b. When a string is not initialized, it has default value `null`. It will throw `NullPointerException` error when you try to access a method using the `null` variable.

###Q5. Given that `file.txt` doesn’t exist on your system, what is the output of the following code?

	:::java
	import java.io.*;
	public class MultipleExceptions {
	public static void main(String args[]) {
	FileInputStream fis = null;
	try {
		fis = new FileInputStream("file.txt");
		System.out.println("File Opened");
		fis.read();
		System.out.println("Read File");
	}
	finally {
		System.out.println("finally");
	}
	catch (FileNotFoundException fnfe) {
		System.out.println("File not found");
	}
	catch (IOException ioe) {
		System.out.println("File Closing Exception");
	}
	System.out.println("Next task..");
	}
	}

a. The code prints:

	:::java
	File not found
	finally
	Next task..

b. The code prints:

	:::java
	File Opened
	File Closing Exception
	finally
	Next task..

c. The code prints `File not found`

d. The code fails to compile

A5. d

>The code cannot compile because **finally block cannot be put before catch block**.

###Q6. Given that `players.txt` exists on your system and that the assignment of players, shown in bold, doesn’t throw any exceptions, what is the output of the following code?

	:::java
	import java.io.*;
	public class TwistInTaleNestedTryCatch {
	static FileInputStream players, coach;
	public static void main(String args[]) {
	try {
	players = new FileInputStream("players.txt");
	System.out.println("players.txt found");
	try {
	coach.close();
	}
	catch (IOException e) {
	System.out.println("coach.txt not found");
	}
	}
	catch (FileNotFoundException fnfe) {
	System.out.println("players.txt not found");
	}
	catch (NullPointerException ne) {
	System.out.println("NullPointerException");
	}
	}
	}

a. The code prints:

	:::java
	players.txt found
	NullPointerException

b. The code prints:

	:::java
	players.txt found
	coach.txt not found

c. The code throws a runtime exception.

d. The code fail to compile.

A6. a

>Since `coach` is a `static` variable **which hasn't been initialized**, a call to use **a method** of `coach` will throw `NullPointerException`.

##Q&As from Chapter 4, OCA Guide from Manning

###Q1: Which of the following are valid lines of code to define a `multidimensional int array`?

a. `int[][] array1 = {{1, 2, 3}, {}, {1, 2,3, 4, 5}};`

b. `int[][] array2 = new array() {{1, 2, 3}, {}, {1, 2,3, 4, 5}}`

c. `int[][] array3 = {1, 2, 3}, {0}, {1, 2,3, 4, 5};`

d. `int[][] array5 = new int[2][];`

A1. a,d

>The option b is wrong. `new array()` is not valid

###Q2. Which of the following statements are correct?

a. By default, an ArrayList creates an array with an initial size of 16 to store its elements.

b. Because ArrayList stores
only objects, you can’t pass an element of an ArrayList to a switch construct.

c. Calling `clear()` and `remove()` on an ArrayList will remove all its elements.

d. If you frequently add elements to an ArrayList , specifying a larger capacity will improve the code efficiency.

e. Calling the method `clone()` on an ArrayList creates its shallow copy; that is, it doesn’t clone the individual list elements.

A2. d,e

>Option a is not right. `ArrayList` has size `10`. `StringBuilder` has size `16`.
>Option c is right. You can specify a larger capacity of `ArrayList`

###Q3. What is the output of the following code?

	:::java
	import java.util.*; //Line 1
	class EJavaGuruArrayList { //Line2
	public static void main(String args[]) { //Line 3
		ArrayList<String> ejg = new ArrayList<>(); //Line 4
		ejg.add("One"); //Line 5
		ejg.add("Two"); //Line 6
		System.out.println(ejg.contains(new String("One"))); //Line 7
		System.out.println(ejg.indexOf("Two")); //Line 8
		ejg.clear(); //Line 9
		System.out.println(ejg); //Line 10
		System.out.println(ejg.get(1)); //Line 11
	}
	}

a. Line 7 prints true

b. Line 7 prints false

c. Line 8 prints -1

d. Line 8 prints 1

e. Line 9 removes all elements of the list ejg

f. Line 9 sets the list ejg to null

g. Line 10 prints null

h. Line 10 prints []

i. ine 10 prints a value similar to ArrayList@16356

j. Line 11 throws an exception

k. Line 11 prints null

A3: a,d,e,h,k

>Option a is right. When `contains()` is used for String, it call `equals()` first, which for String, if using `new()`, means same reference.

>Option h is right. When calling `System.out.println()`, `toString()` method is automatically called. For `ArrayList`, `toString()` method will print out String value. Since ejg has been cleared, `null` value will be print out.

###Q4. What is the output of the following code?

	:::java
	class EJavaGuruString {
		public static void main(String args[]) {
			String ejg1 = new String("E Java");
			String ejg2 = new String("E Java");
			String ejg3 = "E Java";
			String ejg4 = "E Java";
			do
			    System.out.println(ejg1.equals(ejg2));
			while (ejg3 == ejg4);
		}
	}

a. true printed once

b. false printed once

c. true printed in an infinite loop

d. false printed in an infinite loop

A4. c

>String `ejg3` and `ejg4` are not created with `new()`, so Java will find them same in String pool, which gives out a infinite loop.

###Q5. What is the output of the following code?

	:::java
	class EJavaGuruStringBuilder {
		public static void main(String args[]) {
			StringBuilder ejg = new StringBuilder(10 + 2 + "SUN" + 4 + 5);
			ejg.append(ejg.delete(3, 6));
			System.out.println(ejg);
		}
	}

a. 12S512S5

b. 12S12S

c. 1025102S

d. Runtime exception

A5. a

>`ejg.delete(3, 6)` means `ejg` is now `12S5`. **last index is exclusive.**

###Q6. What is the output of the following code?

	:::java
	class EJavaGuruString2 {
		public static void main(String args[]) {
			String ejg = "game";
			ejg.replace('a', 'Z').trim().concat("Aa");
			ejg.substring(0, 2);
			System.out.println(ejg);
		}
	}

a. gZmeAZ

b. gZmeAa

c. gZm

d. gZ

e. game

A6. e

>String is **immmutable**. Since `ejg` has been initialized, no operation can modify its value.

###Q7. Let’s modify some of the code used in the previous section. Execute this code on your system. Which answer

	:::java
	String letters = "ABCAB";
	System.out.println(letters.substring(0, 2).startsWith('A'));

a. true

b. false

c. AB

d. ABC

e. Compilation error

A7. e

>`startsWith()` only accept `String` as argument

###Q8. Modify some of the code used in the previous example as follows:

	:::java
	//Line1
		String multiStrArr[][] = new String[][]{
	//Line2
			{"A", "B"},
	//Line3
			null,
	//Line4
			{"Jan", "Feb", null},
	//Line5
		};

Which of the following individual options are true for the previous code?
a. Code on line 4 is the same as `{"Jan", "Feb", null, null}`,

b. No value is stored at `multiStrArr[2][2]`

c. No value is stored at `multiStrArr[1][1]`

d. Array `multiStrArr` is asymmetric.

A8. a,d

>The probem if option c is, `multiStrArr[1][1]` does not exist, so we cannot say "no value is stored"

###Q9. What is the output of the following code?

	:::java
	ArrayList<String> myArrList = new ArrayList<String>();
	String one = "One";
	String two = new String("Two");
	myArrList.add(one);
	myArrList.add(two);
	ArrayList<String> yourArrList = myArrList;
	one.replace("O", "B");
	\***********\
	for (String val : myArrList)
	    System.out.print(val + ":");
	for (String val : yourArrList)
	    System.out.print(val + ":");

a. `One:Two:One:Two:`

b. `Bne:Two:Bne:Two:`

c. `One:Two:Bne:Two:`

d. `Bne:Two:One:Two:`

A9. a

>We cannot change the value of String after it has been initialized.

##Q&As from Chapter 6, OCA Guide from Manning

###Q1. Let’s modify the code used in the previous example as follows. Which of the options is correct for this modified code?

	:::java
	class Employee {
	    private String name;
	    String address;
	    protected String phoneNumber;
	    public float experience;
	}
	class Programmer extends Employee {
	    Programmer (String val) {
	        name = val;
	}
	String getName() {
	        return name;
	}
	}
	class Office {
	    public static void main(String args[]) {
	        new Programmer ("Harry").getName();
	    }
	}

a. The class `Office` prints `Harry` .

b. The derived class `Programmer` can’t define a getter method for a variable defined in its base class `Employee`.

c. The derived class `Programmer` can’t access variables of its base class in its constructors.

d. `new Programmer ("Harry").getName();` isn’t the right way to create an object of class `Programmer` .

e. Compilation error.

A1. e. `name` is `private`.

###Q2. Let’s modify the definition of the `Employee` and `Programmer` classes as follows. What is the output of class `TwistInTale3` ?

	:::java
	class Employee {
	    String name = "Emp";
	    String address = "EmpAddress";
	}
	class Programmer extends Employee{
	    String name = "Prog";
	    void printValues() {
	        System.out.print(this.name + ":");
	        System.out.print(this.address + ":");
	        System.out.print(super.name + ":");
	        System.out.print(super.address);
	    }
	}
	class TwistInTale3 {
	    public static void main(String args[]) {
	        new Programmer().printValues();
	    }
	}

a. `Prog:null:Emp:EmpAddress`

b. `Prog:EmpAddress:Emp:EmpAddress`

c. `Prog::Emp:EmpAddress`

d. Compilation error

A2. b. If a `this` in derviced class cannot find variable, it will go back to its base class for the value.

###Q3. Examine the following code and select the correct method declaration to be inserted at `//INSERT CODE HERE`:

	:::java
	interface Movable {
	    void move();
	}
	class Person implements Movable {
	    public void move() { System.out.println("Person move"); }
	}
	class Vehicle implements Movable {
	    public void move() { System.out.println("Vehicle move"); }
	}
	class Test {
	    // INSERT CODE HERE
	    movable.move();
	}
	}


a. `void walk(Movable movable) {`

b. `void walk(Person movable) {`

c. `void walk(Vehicle movable) {`

d. `void walk() {`

A3. a. b. c.

>Note option a is available. Although you cannot create instance for a `interface`, it's ok to put it as a **type of method parameter**.

###Q4. Examine the following code:

	:::java
	class Programmer {
	    void print() {
	        System.out.println("Programmer - Mala Gupta");
	    }
	}
	class Author extends Programmer {
	    void print() {
	        System.out.println("Author - Mala Gupta");
	    }
	}
	class TestEJava {
	    Programmer a = new Programmer();
	    // INSERT CODE HERE
	    a.print();
	    b.print();
	}

Which of the following lines of code can be individually inserted at `//INSERT CODE`? HERE so that the output of the code is as follows:

	:::java
	Programmer - Mala Gupta
	Author - Mala Gupta

a. `Programmer b = new Programmer();`

b. `Programmer b = new Author();`

c. `Author b = new Author();`

d. `Author b = new Programmer();`

e. `Programmer b = ((Author)new Programmer());`

f. `Author b = ((Author)new Programmer());`

A4. b.c

>Problem of option e: Will compile but has `classCastException` error. **Base class cannot be cast to derived class. Opposite is fine**

>Problem of opetion f: same reason as option e.

###Q5. Given the following code, which of the options, when applied individually, will make it compile successfully?

	:::java
	Line1> interface Employee {}
	Line2> interface Printable extends Employee {
	Line3>    String print();
	Line4> }
	Line5> class Programmer {
	Line6>    String print() { return("Programmer - Mala Gupta"); }
	Line7> }
	Line8> class Author extends Programmer implements Printable, Employee {
	Line9>    String print() { return("Author - Mala Gupta"); }
	Line10> }

a. Modify code on line `2` to: `interface Printable{`

b. Modify code on line `3` to: `public String print();`

c. Define the accessibility of the print methods to `public` on lines `6` and `9`.

d. Modify code on line `8` so that it implements only the interface `Printable`

A5. c

>Option a, b, d won't cause compile error, but also won't fix compile error.

>Option c: Since all interface method are implictly `public` and `abstract`, the problem of the code is `print()` has to be `public`

##Q&As from Chapter 5, OCA Guide from Manning

###Q1. Let’s modify the code used in the previous example as follows. What is the output of this code?

	:::java
	String day = new String("SUN");
	switch (day) {
	    case "MON":
	    case "TUE":
	    case "WED":
	    case "THU": System.out.println("Time to work");
	    break;
	    case "FRI": System.out.println("Nearing weekend");
	    break;
	    case "SAT":
	    case "SUN": System.out.println("Weekend!");
	    break;
	    default: System.out.println("Invalid day?");
	}

a. Time to work

b. Nearing weekend

c. Weekend!

d. Invalid day?

A1. c

>String is special for `switch` case parameter. `switch` only compare **value of String** when it use String as case parameter.

###Q2. What’s the output of the following code?

	:::java
	class Loop2 {
	    public static void main(String[] args) {
	        int i = 10;
	        do
	            while (i++ < 15)
	            i = i + 20;
	        while (i < 2);
	        System.out.println(i);
	    }
	}

a. 10

b. 30

c. 31

d. 32

A2. d

>Process:
- `i=10` -> `10<15` -> `i++` -> `i=i+20`
- `i=31` -> `31>15` -> `i++`
- Print out `i=32`
- **Note** for i++, alough going out of loop, you still need `++` operation.

###Q3. What’s the output of the following code?

	:::java
	int a = 10;
	if (a++ > 10) {
	    System.out.println("true");
	}
	{
	    System.out.println("false");
	}
	System.out.println("ABC");

a. true false ABC

b. false ABC

c. true ABC

d. compile error

A3: b

>Just need to know only `{}` will not cause compile error.

###Q4. Given the following code, which of the following lines of code can individually replace the `//INSERT CODE HERE` line so that the code compiles successfully?

	:::java
	class EJavaGuru {
	    public static int getVal() {
	        return 100;
	    }
	    public static void main(String args[]) {
	        int num = 10;
	        final int num2 = 20;
	        switch (num) {
	            // INSERT CODE HERE
	            break;
	            default: System.out.println("default");
	        }
	    }
	}

a. `case 10*3: System.out.println(2);`

b. `case num: System.out.println(3);`

c. `case 10/3: System.out.println(4);`

d. `case num2: System.out.println(5);`

A4. a, c, d

>If you use `/` for `case` parameter, Java will **disard** decimal parts, only leave integer.

###Q5. What’s the output of the following code?

	:::java
	class EJavaGuru {
	    public static void main(String args[]) {
	    int num = 120;
	    switch (num) {
	        default: System.out.println("default");
	        case 0: System.out.println("case1");
	        case 10*2-20: System.out.println("case2");
	        break;
	    }
	    }
	}

a. default case1 case2

b. case1 case2

c. case2

d. compile error

A5. d.

>Note. last `case` equasl to `case 0`. **Duplicate case will get compile error.**

###Q6. What’s the output of the following code?

	:::java
	class EJavaGuru5 {
	    public static void main(String args[]) {
	    int i = 0;
	    for (; i < 2; i=i+5) {
	        if (i < 5) continue;
	        System.out.println(i);
	    }
	    System.out.println(i);
	    }
	}

a. Compilation error

b. 0 5

c. 0 5 10

d. 10

e. 0 1 5

f. 5

A6. f

>It is fine to **skip start value in `for` loop**, as long as you initailize start value before.
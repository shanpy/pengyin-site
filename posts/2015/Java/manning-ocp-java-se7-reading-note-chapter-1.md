.. title: Manning OCP Java SE 7 Reading Note: Chapter 1
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-ocp-java-se7-reading-note-chapter-1
.. authors: Pengyin Shan
.. description: This is a post that I moved from <a href="blogpengyin.herokuapp.com"> my old blog site</a>. This is the reading note for **OCP Java SE 7 Certification Guide** from **Manning**. I created this post in late 2014.

This is the reading note for **OCP Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

#Chapter 1: Java Class Design*

##1.1 Java access modifiers

Java has four access modifiers:

- `public`: least restrictive

- `protected`

- `default`

- `private`: most restrictive

Access modifier can be applied to classes, interfaces and their varibles and methods. *Can not* be applied to local variables and method parameters.

Members of an interface are public in default. If you set it to `protected` or `private`, the interface *will not compile*.

`public` is the least restrictive access modifier. Classes and interfaces defined using the public modifier are accessisble across *all packages*, from *derived* to *unrelated* classes.

`protected` classes and interfaces are accessiable if *in same package*. Also, *All derived class* is accessable even in *different package* (i.e. `extends` is used in this class).

A derived class can inherite and access protected memebers of its base class, regardless of the package it's defined. A derived class in a separate package can't access protected memebers of its base class using `reference variables`.

	:::java
	package library;

	public class Book{
		protected String author;
		protected void modifyTemplate(){};
	}
	/*********************/
	package building;
	import library.book;

	public class StoryBook extends Book{
		public StoryBook{
			author="ABC"; //Works Fine
			modifyTemplate(); //Works Fine

			//If you want to access memebers in book, a new instance of Book needs to be declared first to access inside.
			Book book = new Book();
			String v = book.author;
			book.modifyTemplate();
		}
	}

A class that has no access modifier marked always has `default access`, also called `package-private access`. Only memebers in same package can access it.

	:::java
	package library;
	public class Book{
		int issueCount;
		void issueHistory(){};
	}

	package building;
	import library.Book;
	public class House{
		public House(){
			Book b = new Book(); //Works Fine
			int c = b.issueCount(); //Compile Error
			b.issueHistory(); //Compile Error
		}
	}

	package library;
	class Book{
		int issueCount;
		void issueHistory(){};
	}

	package building;
	import library.Book; //Compile Error. library.Book can not be accessed
	public class House{
		public House(){
		}
	}

`private` means this member can only be accessed in its own class.

`private` and `protected` can not be applied to top level class/interface. Method parameter and local varaibels can only use `default access`. In these cases java will not compile.

##1.2 Overloaded methods and constructors

Overloaded methods are mothods with the same name but different method parameter lists. Also, a derived class can overload its base class's methods

	:::java
	class Paper();
	class Laptop();

	class Lecture{
		void takeNotes(Paper paper);
		void takeNotes(Laptop laptop);
	}

	class Pen();
	class newLecture extends Lecture{
		void takeNotes(Pen pen);
	}

Overloaded method can accept:

Different number of parameters

*Or* different type of parameters

	:::java
	public Test{

	double Case(double test1, int test2){
		return 0.5;
	}
	double Case(int test1, double test2){
		return 0.6;
	}
	public static void main(String.. args){
		Test test = new Test();
		test.Case(2,3);
		/*
		This will get compile error.
		Java compiler is unable to determine which overloaded method should be called.
		*/
	}

	//Following will solve the problem
	double Case(int test1, int test2){
		return 0.7;
		}
	}

*Or* different positions of parameter, based on parameter type

Overloaded method can not accept:

- Only differ in return types becuase java compiler does not differentiates turn types.

- Only differ in access modifiers

- Only different in non-access modifiers such as `final`.

The overloaded methods are bound are *compile time* and not run time. To resolve the call to the overloaded methods, the complier consider the type of the variable that is used to *refer* to an object.

	:::java
	class Result{
		String getValue(Object obj){
			return "Object";
		}
		String getValue(String str){
			return "String";
		}
	}

	class TestResult{
		public static void main(String... args){
			Object obj = new String("Harry");
			System.out.println(new Result().getValue(obj));

			/*
			"Object" will be print out.
			String is just a reference, pointing to the object obj.
			So getValue will find type of the reference object obj, which is a object.
			Note that obj here is a reference variable becuase we use obj to refer an instance of String, "Harry".
			*/

		}
	}

Overloaded constructors can be defined by using a different argument list, but no a change of its access or nonaccess modifiers.

	:::java
	class Employee{
		String name;
		int age;

		Employee(String newName){
		name = newName;
		age = 12;
		}

		Employee(String newName, int newAge){
			name = newName;
			age = newAge;
		}
	}

Overloaded constructor can be called from another overloaded constructor. `this` keyword should be used to do this. Also, the class to another constructor must be the *first* statement in a constructor.
	:::java
	class Employee{
		String name;
		int age;

		Employee(){
		/*
		Note: if I add a "System.println.out..." here, there will be compile error.
		Because this() must be the first statment here
		*/
		this(null,0); //Invoke a constructor that takes two parameters
		}

		Employee(String newName, int newAge){
			name = newName;
			age = newAge;
		}
	}
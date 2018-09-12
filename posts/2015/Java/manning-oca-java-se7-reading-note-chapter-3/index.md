.. title: Manning OCA Java SE 7 Reading Note: Chapter 3
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-3
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 3



This is a post that I moved from <a href="blogpengyin.herokuapp.com"> my old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

# Chapter 3: Methods and Encapsulation

This chapter mainly covers:

- Defining the **scope** of variables

- Explaining an object’s **life cycle**

- Creating methods with primitive and object arguments and return values

- Creating **overloaded** methods and constructors

- Reading and writing to object fields

- Calling methods on objects

- Applying **encapsulation** principles to a class

##3.1 Scope of Variables

Valid scope of variable:

- `Local` variable (also known as method-local variables)

- `Method parameter` (also known as method arguments)

- `Instance variable` (also known as attributes, fields, and nonstatic variables)

- `Class variable` (also known as static variables)

The **life span** of a variable is determined by its **scope**.

###Local Variable, Method Parameter

Local variables are defined **within method**, with the **shortest scope (life span)**.

The variables that accept values in a method are called **method parameters**. They’re accessible **only in the method** that defines them.

The scope of methods parameters can never be shorter than scope of local variables.

###Instance Variables, Class Variables

**Instance is another name for an object.**

>Hence, an **instance variable** is available for the **life of an object**. An instance variable is declared **within a class, outside of all of the methods**. It’s accessible to **all the nonstatic methods** defined in a class.

A **class variable** is defined by using the keyword `static` . A class variable **belongs to a class**, not to individual objects of the class. A class variable is shared across **all objects**.

You don’t even need an object to access a class variable. It can be accessed by **using the name of the class** in which it’s defined:

	:::java
	class Person{
	    public int age; //Instance Variable
	    static String name; //Class Variable
	}

	class Test{
	    public static void main(String args...){
	        Person.name = "Bob"; //Use of Class Variable
	        Person p = new Person();
	        p.age = 12; //Use of Instance Variable

	        Person p2 = new Person();
	        System.out.println(p2.name); //Still Bob, because class variable is independent of instance
	        System.our.println(p2.age); //Null. New instance hasn't define the value of this instance variable

	        //You can change class variable once, then all instances will have the changed class variable
	    }
	}

The scope of an instance variable is longer than that of a local vari-
able or a method parameter.

###Compare Scopes, Overlapping Scopes


`Local variables` are defined **within** a method and are normally used to store the intermediate results of a calculation.

`Method parameters` are used to pass values to a method. These values can be manipulated and may also be stored as the state of an object by assigning them to instance variables.

`Instance variables` are used to store the **state** of an object. These are the values that need to be accessed by multiple methods.

`Class variables` are used to store values that should be shared by all the objects of a class.

**Same Name Problem**

- you can’t define a `static variable` and an `instance variable` with the same name in a class

- `local variable`s and `method parameter`s can’t be defined with the same name.

- A class can define `local variable`s with the same name as the `instance or class variable`s.

##3.2 Object's Life Cycle

Java doesn’t allow you to allocate or deallocate memory yourself when you create or destroy objects. Java manages memory for **allocating** objects and reclaiming the memory occupied by unused objects, using Java's **garbage collector**.

Java also provides a method called `finalize`, which is accessible to all of the classes.

All Java classes can **override** the method `finalize`, which executes just before an object is garbage collected;

An object’s life cycle starts when it’s **created** and lasts until it **goes out of its scope** or is **no longer referenced** by a variable.

###Create Object

An object is **created** when you use the keyword `new`. You need to **declare** and **initialize** it.

If you just do `ClassName myclass;`, no objects of class `ClassName` are created in the class Object Life Cycle; it **declares** only a **variable** of type `ClassName`; Only **declaration** step is done.

Since **String**s can also be initialized using the `=` operator, you can just do `String a = "a";` to create a String object.

>If you just do `new ClassName()`, you only finish **initialize** step.

>Creating an object in this manner will execute the relevant **constructor**s of the class.

###Access Object

Once an object is created, it can be **accessed **using its **reference variable**.

It become **inaccessible/eligible to be garbage collected** when it:

- **goes out of scope**

- its reference variable is explicitly set to `null`

- **reassign** another object to this variable (i.e. **reinitialized**)

You can determine only which objects are **eligible** to be garbage collected.

You can never determine **when** a particular object will be garbage collected.

>i.e. "which objects are sure to be col- lected during the next GC cycle" is **unknown**.

##3.3 Create Methods with Arguments and Return Values

Methods are used to define the **behavior** of an object.

###Return

A method may or may not return a value.

>One that doesn’t return a value has a return type of `void`.

>If you don’t assign the returned value from a method, it’s neither a compilation error nor a runtime exception

A method can return a **primitive value** or an **object** of any class.

The returned value from a method may or may not be assigned to a variable.

>If you do assignment operation with a method that is `void`, the code will not compile.

>If you just run a method with return type, without any assignment, this line of code will do nothing.

The variable you use to accept the returned value from a method must be compatible with the returned value. For example, you can not return a `int` when method needs a `double`.

For methds that define a return type, the `return` statement must be immediately followed by a return value;

You can use the `return` statement in a method even if it doesn’t return a value.

Usually this statement is used to define an **early exit** from a method

However, the return statement must be the **last statement to execute** in a method, if present. Othewise code will failt to compile.

The return statement need not be the last statement in a method. i.e. You can `return` in a leaf of if loop.

###Method Parameters

- **Method parameter**s are the variables that appear in the definition of a method.

- **Method argument**s are the actual values that are passed to a method while executing it.

The ellipsis (`...`) that follows the data type indicates that the method parameter may be passed an **array** or **multiple comma-separated values**

You can define only **one** ellipsis variable argument in a parameter list

And it should be the **last variable** in the parameter list

>For example, `public void test(String... a, String... b)` and `public void test(String... a, int b)` will not compile.

**Rules to Remember**

- You can define **multiple parameters** for a method.

- The method parameter can be a primitive type or objects referenced by a class or referenced by an interface.

- The method’s parameters are separated by **commas**.

- Each method parameter is preceded by the name of its type. Each method
parameter must have an **explicit type declared with its name**.

- You can’t declare the type once and then list them separated by commas, as you can for variables.

- A method can be an **instance method** (`nonstatic`) or a **class method** (`static`).

- A method can take zero or more parameters but can **return only zero or one values**.

##3.4 Create an Overloaded Method

**Overloaded methods** are methods with the **same name** but **different method parameter lists**.

**Rules to Remember**

- Overloaded methods must have **different method parameters** from one another.

- Overloaded methods may or may not define a different return type.

- Overloaded methods may or may not define different access modifiers.

- Overloaded methods **can’t be defined by only changing their return type or access modifiers**.

###Argument List

The argument lists can differ in terms of any of the following:

- Change in the **number of parameters** that are accepted

- Change in the **types of parameters** that are accepted

- Change in the **positions of the parameters** that are accepted (based on **parameter type**, not variable names)

when you try to execute this method using values that can be passed to both versions of the overloaded methods. In this case, the code will fail to compile:

	:::java
	class MyClass {
	    double calcAverage(double marks1, int marks2) {
	            return (marks1 + marks2)/2.0;
	    }
	    double calcAverage(int marks1, double marks2) {
	            return (marks1 + marks2)/2.0;
	    }
	    public static void main(String args[]) {
	            MyClass myClass = new MyClass();
	            myClass.calcAverage(2, 3); //Two method are same here
	} }

##3.5 Contructor of a Class

Constructors are special methods that create and return an object of the class in which they’redefined.

Constructors have the **same name as the name of the class** in which they’re defined, and they **don’t specify a return type—not even `void`** .

>i.e. A constructor **must not** define any return type.

Constructor is called when a object is **initialized**, for example `new ClassName();`

A constructor can accomplish the following tasks:

- Call the **base class**’s constructor; this can be an **implicit** or **explicit** call.

- **Initialize** all of the **instance variables** of a class with their default values.

###User-Defined Constructors

An author may or may not define a constructor in a class. If the author does define a constructor in a class, it’s known as a **user-defined constructor**.

Because a constructor is called as soon as an object is created, you can use it to **assign default values** to the instance variable of your class:

	:::java
	class Employee {
	    String name;
	    int age;

	    Employee() {
	    age = 20;
	    System.out.println("Constructor");
	    }
	}

Because a constructor is a method, you can also **pass method parameters** to it:

	:::java
	class Employee {
	    String name;
	    int age;

	    Employee(int newAge, String newName) {
	    name = newName;
	    age = newAge;
	    System.out.println("Constructor");
	    }
	}
	//You can use it via new Employee(12,"Lisa");


A constructor does have an **implicit return type**, which is the class in which it’s defined.

It creates and returns an object of its class, which is **why you can’t define a return type for a constructor**.

You can define constructors using **any of the four access modifiers**.

If you define a return tyoe for a contructor, Java will treat it as **another method**, not a **constructor**, which also implies that it won’t be called implicitly when you create an object of its class.

**Initialize Block**

An **initializer block** is defined **within a class**, not as a part of a method. It executes for every object that’s created for a class.

If you define both an **initializer** and a **constructor** for a class, **both of these will execute**. The initializer block will execute **prior** to the constructor:

	:::java
	class Employee {
	    Employee() {
	    System.out.println("Employee:constructor"); //Constructor
	    }
	    {
	    System.out.println("Employee:initializer"); //Initialize Block
	    }
	}
	class TestEmp {
	    public static void main(String args[]) {
	    Employee e = new Employee();
	    //Employee: initializer
	    //Employee:constructor
	    }
	}

Initializer blocks are used to initialize the variables of **anonymous classes**.

An anonymous class is a type of **inner class**. In the absence of a name, anonymous classes can’t define a constructor and rely on an initializer block to initialize their variables upon the creation of an object of their class.

###Default Constructor

In the absence of a user-defined constructor, Java inserts a **default constructor**.

This constructor **doesn’t accept any method arguments**.

>It calls the constructor of the **super (parent)** class and assigns default values to all the instance variables.

>Code Example of a default constructor:

	:::java
	Employee() {
	    super(); //Use super to call parent class constructor
	    name = null; //Assign defalt value to instance variables
	    age = 0;
	    }

if you modify the class later by adding a constructor to it, the Java compiler will **remove the default, no-argument constructor** that it initially added to the class.

>i.e. **Java defines a default constructor if and only if you don’t define a constructor.**

So if you defined a constructor which takes parameters, but when you create instance you just do `new ClassName()`, the code will fail to compile.

###Overloaded Constructors

Similar as overloaded methods, overloaded constructor must:

- be defined using **different argument lists**.

- can’t be defined by just a change in the access **modifiers**.

- Because constructors don’t define a return type, there’s no point to defining invalid overloaded constructors with different return types.


Overloaded constructors are invoked by using the keyword `this` —
an implicit reference that’s accessible to all objects that **refer to an object itself**:

	:::java
	class Employee {
	    String name;
	    int age;
	    Employee() {
	    this(null, 0);
	    //this is used to call anther constructor which takes two parameters
	    }
	    Employee(String newName, int newAge) {
	    name = newName;
	    age = newAge;
	    }
	}

However, when you invoke an overloaded constructor using the keyword `this` , it must be the **first statement** in your constructor. i.e. `Employee(){ int a = 0; this(null,0); }` cannot compile.
- Also, you can’t invoke a constructor within a class by **using the class’s name**. i.e. `Employee(){ Employee(null,0); }` will not compile.
- `Employee(){ this() }` will create infinate loop. Code will not compile.

**Rules to Remember**

- Overloaded constructors must be defined using different argument lists.

- Overloaded constructors can’t be defined by just a change in the access modifiers.

- Overloaded constructors may be defined using different access modifiers.

- A constructor can call another overloaded constructor by using the keyword `this` .

- A constructor can’t invoke a constructor by using its class’s name.

##3.6 Accessing Object Fields

An **object field** is another name for an **instance variable** defined in a class.

A **setter method** is used to set the value of a variable.

A **getter method** is used to retrieve the value of a variable.

**The name of an object field is not determined by the name of its getter or setter methods.** i.e. Setter and Getter can have different name comparing to variable name.


**The default value of an object is `null`**

**The default value of an int is `0`**

If you set an instance variable `private`, then you cannot use `object.instanceName` to assign value. Will not compile.


Java uses the dot notation ( `.` ) to execute a method on a reference variable. For example: `person.setName()`;

When you call a method, you must pass to it the **exact number of method parameters** that are defined by it.

If a method has parameter as `...`, you can pass multiple parameters to it, with same type:

	:::java
	public int daysOffWork(int... days){
	    //...
	}
	public static void main(String... args){
	    System.out.println(e.daysOffWork(1, 2, 3, 4));
	    System.out.println(e.daysOffWork(1, 2, 3));
	    //All code above work fine
	}

##3.7 Apply Encapsulation Principles to a Class

**A well-encapsulated object doesn’t expose its internal parts to the outside world.**

the object fields of a class that **isn’t well encapsulated are exposed outside of the class**. This approach enables the users of the class to **assign arbitrary values** to the object fields.

**Information Hiding**

**Encapsulation** is the concept of defining variables and the methods
together in a class. Information hiding originated from the application and purpose of the concept of encapsulation.

The terms encapsulation and information hiding are used inter-
changeably.

By exposing object functionality only through methods, you can
**prevent your private variables from being assigned any values** that don’t fit your requirements.

One of the best ways to **create a well-encapsulated class** is
to **define its instance variables as private variables** and **allow access to these variables using public methods**.

##3.8 Passing Objects and Primitives to Methods

###Passing Primitives to Methods
The value of a primitive data type is **copied** and **passed** on to a method. Hence, **the variable whose value was copied doesn’t change**.

>i.e. When you pass a primitive variable to a method, its value remains the same after the execution of the method.

Example:

	:::java
	class Employee {
	    int age;
	    void modifyVal(int a) {
	    a = a + 1;
	    System.out.println(a);
	    }
	}
	class Office {
	    public static void main(String args[]) {
	    Employee e = new Employee();
	    System.out.println(e.age); //Prints 0
	    e.modifyVal(e.age); //Prints 1. This method never access the object field age
	    System.out.println(e.age); //Prints 0
	    }
	}

It’s okay to define a method parameter with **the same name as an instance variable** (or object field).

Within a method, **a method parameter takes precedence over an object field**.

On the code above, when the method `modifyVal` refers to the variable `age` , it refers to the **method parameter** `age` , not the **instance variable** `age` .

To access the instance variable `age` within the method `modifyVal` , the variable name `age` needs to be **prefixed with the keyword `this`** ( `this` is a keyword that refers to the object itself).

###Passing Object References to Methods

When you pass an **object reference** to a method, **the method can assign it to another variable**.

In this case, the **state** of the object, which was passed on to the method, remains intact/complete.

Code Example:

	:::java
	class Person {
	    private String name;
	    Person(String newName) {
	    name = newName;
	    }
	    public String getName() {
	    return name;
	    }
	    public void setName(String val) {
	    name = val;
	    }
	}
	class Test {
	    public static void swap(Person p1, Person p2) {
	    //Method to swap two
	    Person temp = p1;
	    object references
	    p1 = p2;
	    p2 = temp;
	    }

	    public static void main(String args[]) {
	    Person person1 = new Person("John");
	    Person person2 = new Person("Paul");

	    System.out.println(person1.getName() + ":" + person2.getName());
	    //Prints John:Paul
	    swap(person1, person2);
	    System.out.println(person1.getName()+ ":" + person2.getName());
	    //Prints John:Paul
	    }
	}

Explaination of `swap` method (Make sure you won't mix order!):

- `Person temp = p1`: make `temp` refer to the object referred to by `p1`.

- `p1 = p2`: makes `p1` refer to the object referred to by `p2` .

- `p2 = temp;` makes `p2` refer to the object referred to by `temp`.

>On the code above, however, **the reference variables `person1` and `person2` are still referring to the objects that they passed to the method `swap`**.

>We can change the value by using `setter` for person_name.
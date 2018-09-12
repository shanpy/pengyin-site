.. title: Manning OCA Java SE 7 Reading Note: Chapter 6
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-6
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 6



This is a post that I moved from <a href="blogpengyin.herokuapp.com">my old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

#Chapter 6 Working with Inheritance

This chapter main talks about:

- Understanding and implementing `inheritance`

- Developing code that demonstrates the use of `polymorphism`

- Differentiating between the type of a `reference` and an `object`

- Determining when `casting` is required

- Using `super` and `this` to access objects and constructors

- Using `abstract classe`s and `interface`s

##Inheritance with Classes

a class can **inherit** the `propertie`s and `behavior` of another class. The class that inherits from another class can also define additional properties and behaviors.

**A class uses the keyword `extends` to inherit a class**:

	:::java
	class Employee {
		String name;
		String address;
		String phoneNumber;
		float experience;
	}
	class Programmer extends Employee {
		String[] programmingLanguages;
		void writeCode() {}
	}
	class Manager extends Employee {
		int teamSize;
		void reportProjectStatus() {}
	}

Inheriting a class is also referred to as **subclassing**.

Inherited class `Employee` is also referred to as the **superclass**, **base class**, or **parent class**.

The classes `Programmer` and `Manager` that inherit the class `Employee` are called **subclasses**, **derived classes**, **extended classes**, or **child classes**.

Code that works with the base class in a **hierarchy tree** can work with all classes that are added using inheritance later.

When multiple classes inherit a base class, it creates a **logical group**.

Inheritance enables you to **reuse** code that has already been
defined by a class. Inheritance can be implemented by extending a class.

###Derived Class

	:::java
	class Employee {
		String name;
		String address;
		String phoneNumber;
		float experience;
	}
	class Manager extends Employee {
		int teamSize;
		void reportProjectStatus() {}
	}
	class Programmer extends Employee {
		String[] programmingLanguages;
		void writeCode() {}
		void accessBaseClassMembers() {
			name = "Programmer";
			//Derived class Programmer can directly access members of its base class.
		}
	}

When a class inherits another class, it encloses within it an object of the inherited class.

For example, for the code above, the `Programer` is a large circle, enclosing a small circle of `Employee`

###A derived class can't inherit all the members of its base class

Based on **access modifiers**:

- `default`— Members with `default` access can be accessed in a derived class only if base and derived classes reside **in the same package**.

- `protected` — Members with protected access are accessible to **all the derived classes, regardless of the packages** in which the base and derived classes are defined.

- `public` — Members with public access are **visible to all** the other classes.

A derived class **can't inherite** following members:

- `private` members of the base class.

- Base class members with `default access`, if the base class and derived classes exist in **separate packages**.

- **`Constructor`s of the base class**. A derived class **can call a base class’s constructors, but it doesn’t inherit them**.

Derived classes **can define** additional properties and behaviors.

Derived classes can also **define their own `constructor`s and `static` methods and variables**.

A derived class can also **hide or override its `base` class’s members**.

When a derived class defines an `instance` or `class variable` with **the same name** as one defined from its base class, **only these new variables and methods are visible to code using the derived class**.

When a derived class defines different code for a `method` inherited from a base class by defining the method again, **this method is treated as a special method—an `overridden` method**.

You can implement inheritance by using either a `concrete` class or an `abstract` class as a `base` class

###Abstract Base Class v.s Concreate Base Class

**Abstract Class**

It groups the common properties and behavior of its derived classes, but it **prevents itself from being instantiated**.

An `abstract class` can **force** all its derived classes to **define their own implementations** for a behavior by defining it as an `abstract method` (**a method without a body**)

A `abstract class` **may or may not define any `abstract methods`**. - If an abstract base class **defines one or more `abstract method`s, the class must be marked as `abstract` and the abstract methods must be implemented in all its derived classes**.

If a `derived class` **doesn’t implement** all the abstract methods defined by its base class, then **it also needs to be an `abstract class`**.

**Important Notes about Abstract Class**

- You can **never create objects** of an `abstract class`.

- **A base class can be defined as an abstract class, even if it doesn’t define any abstract methods**.

- A derived class should **implement all the abstract methods of its base class. If it doesn’t, it must be defined as an abstract derived class**.

- You can use variables of an abstract base class to refer to objects of its derived class.

###Important Term and Defination

- `Base class`— A class inherited by another class. The class `Employee` is a base class for the classes `Programmer` and `Manager` in the previous examples.

- `Superclass` — A base class is also known as a superclass.

- `Parent class` — A base class is also known as a parent class.

- `Derived class` — A class that inherits from another class. The classes Programmer and Manager are derived classes in the previous example.

- `Subclass` — A derived class is also known as a subclass.

- `Extended class` — A derived class is also known as an extended class.

##Inteface

An `interface` can define **only `abstract methods` and `constants`**.

All the members of an interface are **implicitly `public`** .

`interface` **can't have `constructor`**.

**Java doesn't allow a class to inherit multiple classes**.

However, it **allows a class to implement multiple interfaces**.

A class uses the keyword `implements` to implement an interface.

Each class can implement these methods in **its own particular manner**.

If the **signature** of a method is changed in an interface, all classes that implement the interface will fail to compile.

**An interface can only define `constant`s.**

Once it’s assigned, you can’t change the value of a constant.

**The variables of an interface are implicitly `public` , `final` , and `static` .**

>i.e.:

	:::java
	interface MyInterface {
		public static final int AGE = 10; //equal to int AGE = 10; No compile error here
	}

When you implement an interface, you **must implement all its methods** by using the access modifier `public` .

A class that implements an interface **can’t make the interface’s methods more restrictive**.

>i.e.

	:::java
	interface Relocatable {
		void move(); //implicitly public
	}
	class CEO implements Relocatable {
		void move() {} //Won't compile
	}
	/*********************/
	interface Relocatable {
		void move();
	}
	class CEO implements Relocatable {
		public void move() {} //Compile fine
	}

A class can’t inherit multiple classes, but a class **can implement multiple interfaces**.

**An interface can extend multiple interfaces**.

**POINTS TO NOTE ABOUT CLASS AND INTERFACE INHERITANCE** :

- A `class` can inherit **zero or one class**.

- A `class` uses the keyword `extends` to inherit a class.

- A `class` can implement **multiple interfaces**.

- A `class` uses the keyword `implements` to implement an interface.

- An `interface` can’t implement any class.

- An `interface` can inherit **zero or more interfaces**.

- An `interface` uses the keyword `extends` to inherit interfaces.

- An `abstract class` can extend a concrete class and vice versa.

- An `abstract class` can implement interfaces.

- An `abstract class` can extend another abstract class.

- The **first** `concrete class` in the hierarchy must **supply actual method implementations for all abstract methods**.

##Reference Variable and Object Type

objects of derived classes can be referred to using a **reference
variable of either of the following types**:

- **Its own type** — An object of a class `HRExecutive` can be referred to using an object reference variable of type `HRExecutive` .

- **Its base class** — If the class `HRExecutive` **inherits** the class `Employee`, an object of the class `HRExecutive` can be referred to using a variable of type `Employee` .

- **Implemented interfaces** — If the class `HRExecutive` implements the interface `Interviewer` , an object of the class `HRExecutive` can be referred using a variable of type `Interviewer` .

**Imporant**

- If a reference type is `based class`, it **cannot** access member in `derviced class`.

- If a reference type is `base class`, it **cannot** access memeber in `interface` if derived class also implement interface. Same idea, if a reference type is `interface`, it **cannot** access memeber is `base class`.

- If a reference tyope is `own type`, it can access everything.

>Example:

	:::java
	class Employee {
	    String name;
	    String address;
	    String phoneNumber;
	    float experience;
	}
	interface Interviewer {
	    public void conductInterview();
	}
	class HRExecutive extends Employee implements Interviewer {
	    String[] specialization;
	    public void conductInterview() {
	    System.out.println("HRExecutive - conducting interview");
	    }
	}
	/************/
	class Office {
		public static void main(String args[]) {
		    Employee emp = new HRExecutive();
		    //not compile. Cannot access
		    emp.specialization = new String[] {"Staffing"};
		    System.out.println(emp.specialization[0]);
		    //Works fine
		    emp.name = "Pavni Gupta";
		    System.out.println(emp.name);
		    //not compile. Cannot access
		    emp.conductInterview();
		}
	}

The reason we want to do above is **you might not be interested in all the members of a derived class**.

	:::java
	class OfficeInheritanceList {
		public static void main(String args[]) {
		    Interviewer[] interviewers = new Interviewer[2];
		  //Following compile fine. Manager/HRExectuive implements interviewers
		    interviewers[0] = new Manager();
		    interviewers[1] = new HRExecutive();
		    for (Interviewer interviewer : interviewers) {
		    	interviewer.conductInterview();
		    }
		  //Won't compile. You cannot initiate interface
		    HRExecutive hr = new Interviewer();
		}
	}

##Casting

`Casting` is the process of forcefully making a variable behave as a variable of another type.

If a `class` shares an `IS-A` or `inheritance` relationship with another `class` or `interface`, their variables can be cast to each other’s type.

Example: `((HRExecutive)interviewer).specialization = new String[] {"Staffing"};`

##Use this and super to access objects and constructors

###this

The `this` reference always points to an **object’s own instance**.

Any object can use the this reference to refer to its own instance.

You can use the keyword `this` to refer to all methods and variables that are **accessible to a class**.

`this` is often being used to differentiate between `local` and `nstance variable`s name:

	:::java
	class Employee {
	    String name;
	    Employee(String name) {
	        this.name = name;
	    }
	}

`this` is often being used to **access `onstructor`s**:

	:::java
	class Employee {
	    String name;
	    String address;
	    Employee(String name) {
	        this.name = name;
	    }
	    Employee(String name, String address) {
	        this(name); //Call contructor that only accept name
	        this.address = address;
	    }
	}

`this()` is used to call **default `contructor`** :

	:::java
	class Employee {
	    String name;
	    String address;
	    Employee() {
	        name = "NoName";
	        address = "NoAddress";
	    }
	    Employee(String name, String address) {
	        this(); //Must be first statement in this method!
	        if (name != null) this.name = name;
	        if (address != null) this.address = address;
	    }
	}

**If present, a call to a constructorfrom another constructor must be done on the first line of code of the calling constructor**.

###super

`super` is also an object reference, but `super` refers to the **parent or base class of a class**.

Example:

	:::java
	void printNames() {
	    //Can print difference value if two class have different setting
	    System.out.println(super.name);
	    System.out.println(this.name);
	}

The reference variable `super` can also be used to refer to the **constructors of the base class** in a

	:::java
	class Employee {
	    String name;
	    String address;
	    Employee(String name, String address) {
	        this.name = name;
	        this.address = address;
	    }
	}
	class Programmer extends Employee {
	    String progLanguage;
	    Programmer(String name, String address, String progLang) {
	        //Contructor in base class which accepts two parameter
	        //First statement in dervied class constructor
	        super(name, address);
	        this.progLanguage = progLang;
	    }
	}

**If present, a call to a superclass’s constructor must be the *first
statement in a derived class’s constructor*. Otherwise, a call to `super();` (the no-arg constructor) is inserted automatically by the compiler.**

Because `static method`s belong to a class, not to objects of a class, **you can’t use `this` and `super` in `static method`s.**

##Polymorphism

###Polymorphism with classes

`Polymorphism`

- a class **inherit**s another class

- both the base and the derived classes define methods with the **same method signature** (the same method `name` and method `parameters`)

`Polymorphic method`s are also called `overridden method`s.

**Important Note about Overriden Method**

- Overridden methods are defined by `classe`s and `interface`s that share inheritance relationships.

- The **name** of the overridden method must be the **same** in both the `base class` and the `derived class`.

- The **argument list** passed to the overridden method must be the **same** in both the `base class` and `derived class`.

- The **return type** of an overriding method in the derived class **can be the `same`, or a `subclass` of the return type of the overridden method in the `base class`**.

- When the overriding method returns a `subclass` of the return type of the overridden method, it is known as a `covariant return type`.

- An overridden method defined in the `base class` can be an `abstract method` or a `non-abstract method`.

- **Access modifier**s for an overriding method can be the **same or less restrictive** than the method being overridden, but they **can’t be more restrictive**.

Polymorphic methods **don’t always have to be `abstract`**

Polymorphism works only with `overridden method`s.

Polymorphism cannot work with `overload method`s.

Review: `overloaded method`s define a method argument list with **either a different number or type of method parameters**.

**`Overloaded method`s only share the same name**; the `JRE` treats them like **different methods**.

In the case of `overridden method`s, **the `JRE` decides at `runtime` which method should be called based on *the exact type of the object on which it’s called*.**

###Binding of variables and methods at compile time and runtime

With inheritance, the `instance variable`s bind at **compile time**

`Method`s bind at **runtime**.

Example:

	:::java
	class Employee {
	    String name = "Employee";
	    void printName() {
	        System.out.println(name);
	    }
	}
	class Programmer extends Employee {
	    String name = "Programmer";
	    void printName() {
	        System.out.println(name);
	    }
	}
	class Office1 {
	    public static void main(String[] args) {
	        Employee emp = new Employee();
	        Employee programmer = new Programmer(); //Type is Programmer
	        System.out.println(emp.name); //Employee. Instance Variable
	        System.out.println(programmer.name); //Employee
	        emp.printName(); //Employee. Method
	        programmer.printName(); //Programmer. Decide at run time
	    }
	}

###Polymorphism with Interfaces

Polymorphism can also be implemented using `interfaces`.

Polymorphism with interfaces requires a `class` to **implement** an interface.

Polymorphism with interfaces **always involves `abstract method`s from the implemented interface** because interfaces can define only abstract methods.

Review: all the methods defined in an `interface` are implicitly `abstract` and `public`

If a `base class` implement an `interface`, its `derviced class` don't need to implement again. They can just `extend` base class.

Only `overridden method`s — methods with the same method `signatures` participate in `polymorphism`.
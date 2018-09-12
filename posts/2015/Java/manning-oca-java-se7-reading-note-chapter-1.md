.. title: Manning OCA Java SE 7 Reading Note: Chapter 1
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-1
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 1



This is a post that I moved from <a href="http://blogpengyin.herokuapp.com/">my old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

#Chapter 1: Java Basics

Topics Covered in Chapter 1

>Understanding the structure and components of a Java class

>Understanding executable Java applications

>Understanding Java packages

>Importing Java packages into your code

>Applying access and nonaccess modifiers

## 1.1: The Structrue of a Java Class and Source Code File

### 1.1.1 Struture of a Java Class

Java source code file: xxx.**java**. A Java source code file (.java file) can define **multiple classes and interfaces**.

>in Java compiler: **javac** (.exe)

>then output Java bytecode (compiled code for JVM): xxx.**class**

**List of Components in a class**

- The **package** statement

- The **import** statement

- Comments

- Class declarations and definitions

- Variables

- Methods

- Constructors

**Package Statement**
All Java classes are part of a package.

A Java class can be explicitly defined in a named package; otherwise it becomes part of a **default package**, which doesn’t have a name.

The package statement should be **the first statement** in a class.

The package statement cannot appear within a class declaration or after the class declaration.

The package statement must appear **exactly once** in a class.

**Import Statement**

Classes and interfaces in the same package can use each other without prefixing their names with the package name.

Code will fail compiling because an import statement can’t be placed before a package statement.

The `import` statement can’t be used to import **multiple classes or interfaces with the same name**.

If a class includes a `package` statement, all the `import` statements should follow the package statement.

**Comments**

Multiline comments span multiple lines of code. They start with `/*` and end with `*/`.

Multiline comments can contain any special characters (including Unicode characters).

People use an asterisk (`*`) to start the comment in the next line. Please note that this isn’t required—it’s done more for aesthetic reasons.

End-of-line comments start with `//` and, as evident by their name, they are placed at the end of a line of code.

A comment can precede a package statement.

**Class Declaration**

The class declaration marks the start of a class. It can be as simple as the keyword `class` followed by the name of a class.

The declaration of a class is composed of the following parts:

- Access modifiers

- Nonaccess modifiers

- Class name

- Name of the **base class**, if the class is extending another class

- All implemented **interfaces**, if the class is implementing any interfaces

- Class body (class fields, methods, constructors), included within a pair of curly braces, `{}`

To declare a class, you must have:

- Keyword `class`

- Name of the class

- Class body, marked by the opening and closing curly braces, {}

- The **property** of an object: `variable`

- The **behavior** of an object: `method`

- The **state** of a class: `attribute` or `instance variable`

Points to remember:

>A class name **starts** with the keyword `class`. Watch out for the case of the keyword class. **Java is case sEnSiTivE**. class (lowercase c) isn’t the same as Class (uppercase C). **You can’t use the word Class (capital C) to define a class**.

>The state of a class is defined using attributes or instance variables.

>The behavior is defined using methods

>A class definition may also include comments and constructors

A class is a design from which an object can be created.

**Variables**

Variables that store the **state** of an object (also called an **instance**), they are called `instance variable`s or `instance attribute`s.

Each object has its own copy of the instance variables.

The instance variables are defined **within a class** but **outside all methods** in a class.

A class may define an `instance variable` **before or after** the definition of a `method` and still use it.

A single copy of a `class variable` or `static variable` is **shared** by all the objects of a class.

**Methods**

`Instance method`s are generally used to manipulate the instance variables.

A `class method` or `static method` is used to work with the static variables.

**Constructors**

A `class constructor` is used to create and initialize the objects of a class.

A class can define **multiple** constructors that accept different sets of method parameters.

###1.1.2 Structure and Components of a Java Source Code File

A Java source code file is used to define classes and interfaces.

An `interface` is a grouping of related methods and constants, but the methods in an interface **cannot define any implementation**. An interface specifies a **contract** for the classes to implement.

The definition of an interface starts with the keyword `interface`. An interface can define `constant`s and `method`s. **You can’t use the word Interface (with a capital I) to define an interface.**

You can also define a **combination** of classes and interfaces in the same Java source code file, in any order.

If you define a `public` class or an interface in a class, **its name should match the name of the Java source code file**. Also, a source code file **can’t define more than one public class or interface**.

When you use a package or import statement within such Java files, both the package and import statements apply to **all of the classes and interfaces** defined in that source code file.

Classes and interfaces defined in the same Java source code file **can’t be defined in separate packages**.

Classes and interfaces imported using the `import` statement are **available to all the classes and interfaces** defined in the same Java source code file.

##1.2 Executable Java Applications

###1.2.1 Executable Java Classes versus Non-executable Java Classes

The `JVM` executes the code that is defined in the `main` method.

The `main` method should comply with the following rules:

- The method must be marked as a `public` method.

- The method must be marked as a `static` method.

- The name of the method must be `main`.

- The return type of this method must be `void`.

- The method must accept a method argument of a `String array` or a `variable argument` of type String. i.e. `String... args` and `String[] args` are all acceptable.

To define a variable argument variable, the ellipsis (`...`) should follow the type of the variable and not the variable itself. i.e. `String args...` is **not compiling**.

To define an array, the square brackets, `[]`, can follow either the variable name or its type. i.e., `String[] args` and `String args[]` are all acceptable.

The placement of the keywords `public` and `static` can be **interchanged**. i.e. `public staic` and `static public` are all acceptable. **You cannot move `void`!**

>**Important:** As long as you do `java class_name_of_main (parameters)` in command line, you are calling `main` method. If you do `java name_of_other_class (parameters)`, you will be recogized as calling other methods.

##1.3 Java Packages

If you don’t include an explicit package statement in a class or an interface, it’s part of a `default` package.

###1.3.2 Defining classes in a package using the package statement

It’s common for organiza- tions to use **subpackages** to define all their classes, such as `com.test.example`.

A few of important rules about packages:

- Per Java naming conventions, package names should all be in **lowercase**.

- The package and subpackage names are separated using a dot (`.`).

- Package names follow the rules defined for valid identifiers in Java.

- For packaged classes and interfaces, the package statement is the **first statement** in a Java source file (a .java file). The exception is that comments can appear before or after a package statement.

- There can be a **maximum of one package** statement per Java source code file(.java file).

- All the classes and interfaces defined in a Java source code file will be defined in the same package. There is no way to package classes and interfaces defined within the same Java source code file in different packages.

A **fully qualified name** for a class or interface is formed by prefixing its package name with its name (separated by a period), such as `packagename.Classname`.

To enable the Java Runtime Environment (`JRE`) to find your classes, add the base directory that contains your packaged Java code to the **classpath**.

###1.3.3 - 1.3.8

Importing more classes doesn’t increase the size of your own class.

It is possible to use a packaged class or interface without using the import statement, by using its **fully qualified name**.

You can’t use the import statement to access multiple classes or interfaces with the **same names from different packages**. For example, you cannot import `java.util.Date` and `java.sql.Date` at the same time.

By using the wildcard character, an asterisk (`*`), you can import all of the public members, classes, and interfaces of a package. However, you can only use `*` to import **current level class**. You cannot import **sub-level classes**.

The **default** package is **automatically imported** in the Java classes and interfaces defined within the same directory on your system. However, **A class from a default package can’t be used in any named packaged class**, regardless of whether they are defined within the same directory or not.

You can import an individual **static** member of a class or all its static members by using the `import static` statement. **Note correct statement is `import static`, not `static import`.**

##1.4 Java Access Modifiers

A **top-level class** is a class that isn’t defined within any other class. A class that is defined within another class is called a **nested or inner class**.

>**Important: Local variables** and **method parameters** can’t be defined using access modifiers.

Java defines four access modifiers:

- `public` (least restrictive)

- `protected`

- `default`

- `private` (most restrictive)

Think of Access Modifier from the following four perspectives:

- Same Package/Different Package

- Derived Classes/Unrelated Classes

`Public`:

- The **least restrictive** access modifier.

- Classes and interfaces defined using the public access modifier are accessible **across all packages, from derived to unrelated classes**.

- All four perspeactives are avaiable.

`Proctected`:

The members of a class defined using the `protected` access modifier are accessible to:

- Classes and interfaces defined in the **same package**

- **All derived classes**, even if they’re defined in separate packages

- Only *unrelated/different package* perspective cannot access.

- i.e. the subclass of derived class in different package cannot access.

`Default`:

- The members with `package access` are only accessible to classes and interfaces defined **in the same package**.

- Only *same package* perspective get access.

- `Default` access can be compared to *package-private* (accessible only within a package) and `protected` access can be compared to *package- private + kids* (“kids” refer to derived classes)

`Private`:

- The members of a class defined using the `private` access modifier are accessible **only to themselves**.

- **None of the four perspectives are accessiable**.

##1.5 Nonaccess Modifiers

]Access modifiers control the **accessibility** of your class and its members outside the class and the package.

Nonaccess modifiers change **the default properties** of a Java class and its members.

###1.5.1 Abstract Modifier

Only `variable` cannot use `abstract`.

**An abstract `class` can’t be instantiated**. i.e You cannot do `new abstract_class`.

An abstract class may or may not define an abstract method; **you can define an abstract class without any abstract methods. But a concrete class can’t define an abstract method.**

An `interface` is an abstract entity **by default**.

You can add `abstract` keyword to interface if you like.

An abstract `method` doesn’t have a body.

Usually, an abstract method is implemented by a derived class.

A method with an empty body isn’t an abstract method. i.e. a method that havs `{}` is not a abstract method. a method that has `abstract` buy doesn't have `{}` is abstract method.

###1.5.2 Final Modifier

Only `interface` cannot use `final`

A class that is marked final **cannot be extended** by another class.

An `interface` cannot be marked as final.

A final `variable` can’t be reassigned a value. **It can be assigned a value only once.**

You can call methods on a final variable, such as `a.append(b)`,assuming `b` is a final variable. But you cannot reassign another object to a final variable.

A final `method` defined in a base class **can’t be overridden** by a derived class.

###1.5.3 Static Modifier

Variables, methods, classes and interfaces can all use `static` modifier.

`static variables` belong to a class.

>`static attributes` exist **independently** of any instances of a class and may be accessed even when no instances of the class have been created.

>A `static variable` is shared by all of the objects of a class.**, i.e. if a instance change the value of a static variable, all instances that access this static variable after it will get same new value.

>A `static variable` can be accessed using the name of the object
reference variable or the name of a class.

>static method`s aren’t associated with objects and **can’t use any of the `instance variable`s of a class**.

You can use static methods to define `utility method`s, which are methods that usually manipulate the method parameters to compute and return an appropriate value.

The static members aren’t involved in **runtime polymorphism**. **You can’t override the static members in a derived class**, but you can **redefine** them.

**Neither `static method`s nor `static variable`s can access the `non-static` variables and methods of a class.** But **the reverse is true**: `non-static` variables and methods can access `static` variables and methods because the static members of a class exist even if no instances of the class exist.

>You can’t prefix the definition of a **top-level** class or an interface with the keyword `static`.
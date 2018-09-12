.. title: Java Knowledge: Enum
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: java-knowledge-enum
.. authors: Pengyin Shan
.. description: Enum is a very useful type in Java, and I'm not very familiar with it. This post records some basic knowledge of using Enum in Java, mainly are my reading notes for OCP Java SE7 MEAP V12 from Manning Publican, Chapter 2.3.



`Enum` is use to define **pre-defined**, **finite** set of objects.

We can also use `Enumerated Types` to describe `Enum` type.

An `enum` defines a new **custom data type** (like `interfaces` and `classes`).

>Users are allowed to **use** only **existing** `enum` objects;

>They **can’t create** new enum objects.

### Create Enum

An `enum` enables you to create a **type**, which has a **fixed** set of `constants`.

Code Example:

	:::java
	//Assume we have: enum Level {BEGINNER,INTERMEDIATE,EXPERT}
	class Game {
	    Level gameLevel; //gameLevel is a variable with type Level
	}
	class GameApp {
	    Game game = null;
	    public void startGame () {
	        game = new Game();
	        game.gameLevel = Level.BEGINNER; //Assgin constant BEGINNER
	    }
	}

>You can assign **only one constants** defined in the enum level to `gameLevel`, since it is type `Level`.

###Detail about a Enum Class

Following is the implicate class for `enum Level {BEGINNER,INTERMEDIATE,EXPERT}`:

	:::java
	final class Level extends Enum //enum is implicitly final
	{
	    //enum constants are implicitly public, static and final
	    public static final Level BEGINNER;
	    public static final Level INTERMEDIATE;
	    public static final Level EXPERT;
	    private static final Level $VALUES[];
	    //creation of enum constants. This compiles after constructor
	    static
	    {
	        BEGINNER = new Level("BEGINNER", 0);
	        INTERMEDIATE = new Level("INTERMEDIATE", 1);
	        EXPERT = new Level("EXPERT", 2);
	        $VALUES = (new Level[] {
	            BEGINNER, INTERMEDIATE, EXPERT
	        });
	    }
	    //return an array of all enum constants
	    public static Level[] values()
	    {
	        return (Level[])$VALUES.clone();
	    }
	    //pass a string and return corresponding enum constant
	    public static Level valueOf(String s)
	    {
	        return (Level)Enum.valueOf(Level, s);
	    }
	    //constructor
	    private Level(String s, int i)
	    {
	        super(s, i);
	    }
	}

### java.lang.Enum

All enums in Java extend the abstract class `java.lang.Enum`, defined in the Java API.

Code:

	:::java
	public abstract class Enum<E extends Enum<E>> implements Comparable<E>, Serializable {
	    private final String name; //name of enum constant
	    private final int ordinal; //position of enum constant
	    protected Enum(String name, int ordinal) {
	        this.name = name;
	        this.ordinal = ordinal;
	    }
	    //Can be overridden, return name of constant
	    public String toString() {
	        return name;
	    }
	    //Can not be overridden, return name of constant
	    public final String name() {
	        return name;
	    }
	}

The class `Enum` defines only **one constructor** with `String` and `int` parameters to specify its *name* and *ordinal (order)*. Every `enum` constant is implicitly assigned **an order on its creation**.

The **default order** of enum constants is their **order of definition**. The enum constants *aren’t sorted alphabetically*.

>Note that both methods—`toString()` and `name()` defined in `java.lang.Enum` — return the value of the instance variable `name`

Because method `name()` is a `final` method, you **can’t override** it. But you **can override** method `toString()` to return any description that you want.

For an `enum` constant `BEGINNER` in `enum` `Level`, calling `System.out.println(Level.BEGINNER)` returns the **name** of the enum constant—that is, `BEGINNER`

You can override `toString()` in an `enum` to modify this default return value.

A class can **extend from only one base class**, an attempt to make your `enum` extend any another class will fail. The following code won’t compile:

	:::java
	//Won't compile
	class Person {}
	enum Level extends Person { BEGINNER, INTERMEDIATE, EXPERT }

But you can make your `enum` implement any number of `interfaces`. A class can extend only one base class but **can implement multiple interfaces**. The following code compiles successfully:

	:::java
	//Compile successfully
	interface MyInterface {}
	enum Level implements MyInterface { BEGINNER, INTERMEDIATE, EXPERT }
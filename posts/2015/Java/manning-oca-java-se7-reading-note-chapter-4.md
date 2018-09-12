.. title: Manning OCA Java SE 7 Reading Note: Chapter 4
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: manning-oca-java-se7-reading-note-chapter-4
.. authors: Pengyin Shan
.. description: Manning OCA Java SE 7 Reading Note: Chapter 4



This is a post that I moved from my <a href="blogpengyin.herokuapp.com">old blog site</a>. This is the reading note for **OCA Java SE 7 Certification Guide** from **Manning**. *Please note that all definations and examples in this post are taken from the book.*

#Chapter 4. String, StringBuilder, Arrays and ArrayList

This chapter mainly covers:

- Creating and manipulating `String` and `StringBuilder` objects
- Using common methods from class String and StringBuilder

- Creating and using one-dimensional and multidimensional `arrays` in single and multiple steps

- Accessing elements in asymmetric multidimensional arrays
Declaring, creating, and using an `ArrayList` and understanding the advantages of an ArrayList over arrays

- Using methods that add, modify, and delete elements of an ArrayList

##4.1 String

###Create a String

You can create objects of the class `String` by:

- using the `new` operator

- by using the assignment operator ( `=` )

- by enclosing a value within double quotes ( `"` ).

**Important:** `String` objects created using the operator `new` always refer to **seperate objects** and storing in **seperate locations**, even if they store the same sequence of characters.

>i.e. Following code will print `false`:

	:::java
	String str1 = new String("Paul");
	String str2 = new String("Paul");
	System.out.println(str1 == str2);

**Important: ** `String` object is created using `=` always refer to **same objects**.  The objects are created and stored in a **pool of String objects**. Before creating a new object in the pool, Java first **searches for an object with similar contents**.

>So when the following line of code executes, no String object with the value "Harry" is found in the pool of String objects:`String str3 = "Harry";`

As a result, Java **creates** a String object with the value "Harry" in the pool of String objects referred to by variable `str3` .

When the following line of code executes, Java **is able to find** a String object with the value "Harry" in the pool of String objects:`String str4 = "Harry";`

So now `System.out.println(str3 == str4);` should be `true`.

**Important: ** `String` object is created using `"string_value"` (without `new`) are **reused from the String constant pool** if a matching value is found.

If a matching value isn’t found, the JVM **creates** a String object with the specified value and **places it in the String constant pool**:

	:::java
	String morning1 = "Morning";
	System.out.println("Morning" == morning1); //True

	String morning2 = new String("Morning");
	System.out.println("Morning" == morning2); //False since it use "new"

**Conclusion**

- If a String object is created using the keyword `new` , it always results in the creation of a new String object.

- A new String object gets created using the assignment operator ( `=` ) or double quotes (`""`) only if a matching String object with the same value isn’t found in the String constant pool.

String constructor can accept a `char array` and create new String:
	:::java
	String girl = new String("Shreya");
	char[] name = new char[]{'P','a','u','l'};
	String boy = new String(name);

`StringBuilder` and `StringBuffer` can be used to create new String:

	:::java
	StringBuilder sd1 = new StringBuilder("String Builder");
	String str5 = new String(sd1);
	StringBuffer sb2 = new StringBuffer("String Buffer");
	String str6 = new String(sb2);

>**The literal value for String is null .**

###The Class String is Immutable

The concept that the class **String is immutable** is an important point to remember. **Once created, the contents of an object of the class String can never be modified**.

the JVM creates a **pool** of String objects that can be referenced by multiple variables across the JVM . The JVM can make this optimiza-
tion only because String is immutable.

**String objects can be shared across multiple reference variables without any fear of changes in their values**.

If the reference variables `str1` and `str2` refer to the same String object value "Java" , `str1` need not worry for its lifetime that the value "Java" might be changed by variable `str2` .

class `String` is **implemented** by the authors of this class:

- The class String **stores its values** in a **private** variable of the type **char array** ( `char value[]` ). *Arrays are fixed in size and don’t grow once initialized*.

- This value variable is marked as `final` in the class String . Note that final is a nonaccess modifier, and **a final variable can be initialized only once**.

- None of the methods defined in the class String manipulate the individual elements of the array value .

All the methods defined in the class String , such as `substring()` , `concat()`, `toLowerCase()`, `toUpperCase()`, `trim()`, and so on, which **seem** to modify the contents of the String object on
which they’re called, **create and return a new String object**, rather than modifying the existing value.

###Methods of the class String

`charAt(int index)` can be used to retrieve a **character** at a specified **index** of a String

`indexOf(char c)` is used to search a String for the **occurrence** of a char or a String.

If the specified char or String is found in the target String, this method returns the first matching position; otherwise, it returns -1

If you wish, you can also set the starting position: `System.out.println(letters.indexOf('B', 2));` starts from position 2

`substring(int start, int end)` is shipped in two flavors. The first returns a substring of a String from the position you specify to the end of the String (**end position exclusive**)

`trim()` returns a new String by **removing all the leading and trailing white space** in a String . White spaces are blanks (new lines, spaces, or tabs).

>*this method doesn’t remove the space **within** a String .*


`replace(char,char)` or `replace(string, string)` return a new String by **replacing** all the occurrences of a `char` with another `char`. - - Instead of specifying a char to be replaced by another char , you can also specify a sequence of characters—a `String` to be replaced by another String.

>*Notice the type of the method parameters passed on this method: either char or String.You can’t mix these parameter types*.

`length()` is used to retrieve the length of a String.

`startsWith(String)` and `endWith(String)` determines whether a String starts/ends with a specified prefix/suffix, specified as a `String`.

>You can also specify whether you wish to search from the start of
a String or from a particular position. This method returns `true` if a match is found and `false` otherwise

>*These two methods are case-sensitive!*

>*These two methods only accept string parameter!*

When chained, the methods are evaluated **from left to right**.

	:::java
	String day = "SunDday";
	day.replace('D', 'Z').substring(3);
	System.out.println(day); //prints Sunday. String is immutable

	day = day.replace('D', 'Z').substring(3);
	System.out.println(day); //prints ZDay because We hava an re-assignment here.

###String Objects and Operators

Of all the operators that are on this exam, you can use just a handful with the String objects:

- **Concatenation**: `+` and `+=`

- **Equality**: `==` and `!=`

You can use the operators `+` and `+=` to concatenate two String values. Behind the scenes, string concatenation is implemented by using the `StringBuilder` (covered in the next section) or `StringBuffer` (similar to StringBuilder ) classes.

The `+` operator enables you to create a new object of class
String with a value equal to the concatenated values of multiple Strings .

The + operator can be used with the primitive values, **Which means if you do num + num + string, first two numbers will be added together, then transfer to string!**

`"" + num + num + aStr;` can be used to transfer all nums to string to concatenate

When you use += to concatenate String values, ensure that the variable you’re using has been **initialized** (and doesn’t contain `null` )

However, **no compile or runtime error will appear. Just null value will be print out.**

###Determining Equality of String

The correct way to compare two String values for equality is to use the `equals()` method defined in the String class.

This method returns a `true` value if the object being compared to:

- It isn’t `null`

- It is a `String` object

- Represents the same sequence of characters as the object to which it’s being compared.

The operator `==` won’t always return the value true , even if the two objects store the same String values. **The operator `==` compares whether the reference variables refer to the same objects**.

You can use the operator `!=` to compare the **inequality of objects referred to by the String variables**. It’s the **inverse** of the operator `==` :

	:::java
	String var1 = new String("Java");
	String var2 = new String("Java");
	System.out.println(var1.equals(var2)); //true
	System.out.println(var1 == var2); //false
	System.out.println(var1 != var2); //true

	String var3 = "code";
	String var4 = "code";
	System.out.println(var3.equals(var4)); //true
	System.out.println(var3 == var4); //true
	System.out.println(var3 != var4); //false

##Mutable Strings: StringBuilder

You must use class `StringBuilder` when you’re dealing with larger strings or modifying the contents of a string **often**.

###StringBuilder is Mutable

In contrast to the class `String` , the class `StringBuilder` uses a **non– final char array** to store its value.

###Creating StringBuilder Objects

You can create objects of class `StringBuilder` using multiple overloaded constructors `new StringBuilder()`:

	:::java
	class CreateStringBuilderObjects {
		public static void main(String args[]) {
			//No arguments
			StringBuilder sb1 = new StringBuilder();
			//Take a StringBuilder
			StringBuilder sb2 = new StringBuilder(sb1);
			//Take a int
			StringBuilder sb3 = new StringBuilder(50);
			//Take a String
			StringBuilder sb4 = new StringBuilder("Shreya Gupta");
		}
	}

When you create a StringBuilder object using its **default constructor**, the following code executes behind the scenes to **initialize** the array value defined in the class `StringBuilder` itself:

	:::java
	StringBuilder() {
	//When initialize a StringBuilder, create an array of length 16
	value = new char[16];
	}

When you create a StringBuilder object by **passing it a String** , the following code executes behind the scenes to **initialize**the array value:

	:::java
	public StringBuilder(String str) {
	value = new char[str.length() + 16];
	append(str);
	}

This means you can extend StringBuilder size when you initialize it*

###Methods of StringBuilder

`append()` method adds the specified value **at the end of the existing value** of a `StringBuilder` object.

>This method **accepts all the primitives**, `String` , `char array`, and `Object` as method parameters

>You can append a complete `char array`, `StringBuffer` , or `String` or its subset as follows:

	:::java
	StringBuilder sb1 = new StringBuilder();
	char[] name = {'J', 'a', 'v', 'a', '7'};
	sb1.append(name, 1, 3);
	System.out.println(sb1); //ava

When you append an **object**’s value to a StringBuilder , the method append calls the target class’s `toString()` method to retrieve the object’s String representation.

The `insert()` method is as powerful as the `append()` method. It also exists in multiple flavors (read: overloaded methods) that **accept any data type**.

The main difference between the `append()` and `insert()` methods is that the `insert()` method enables you to insert the requested data at **a particular position**, but the `append()` method only allows you to add the requested data **at the end of** the `StringBuilder` object

Usage of `insert()`:

	:::java
	StringBuilder sb1 = new StringBuilder("123");
	char[] name = {'J', 'a', 'v', 'a'};
	sb1.insert(1, name, 1, 3); //Note 1 and 3 are all inclusive!
	System.out.println(sb1); //1ava23

The method `delete(int start, int end)` removes the characters in a substring of the specified StringBuilder. *End Position is exclusive!*

The method `deleteCharAt(int position)` removes the char **at the specified position**.

the `reverse()` method **reverses the sequence of characters** of a
StringBuilder

>You can’t use the method `reverse()` to reverse a substring of
StringBuilder.**

the `replace(int start, int end, String str)` method in the class StringBuilder **replace**s a sequence of characters, identified by their positions, with another String
- **start int and end int are all inclusive!**

>you can also use the method `subSequence(int start, int end)` to retrieve a subsequence of a StringBuilder object. This method returns objects of type `CharSequence`

>**end int is exclusive!**

###StringBuffer

The classes `StringBuffer` and `StringBuilder` offer the same functionality, with one difference: **the methods of the class `StringBuffer` are synchronized where necessary, whereas the methods of the class `StringBuilder` aren’t**.

So when you work with the class `StringBuffer` , **only one thread out of multiple threads can execute your method.** Working with synchronized methods and the `StringBuffer` class affects the performance of your code.

If you need to access your code **from multiple threads**, use `StringBuffer` ; otherwise use `StringBuilder` .

##Arrays

an `array` is an object itself, which implies that it stores references to the data it stores. Arrays can store two types of data:

- A collection of `primitive data type`s

- A collection of `object`s

An `array` of `primitive`s stores a collection of values that constitute the primitive values themselves. (**With primitives, there are no objects to reference.**) An array of objects stores a collection of values, which are in fact **heap-memory addresses or pointers**.

**`object array`s store references (to objects) and `primitive array`s store primitive values.**

The members of an array are defined in **contiguous (continuous) memory locations** and hence offer improved access speed.

- A `one-dimensional` array is an object that refers to a collection of scalar values.

- A `two-dimensional` (or more) array is referred to as a multidimensional array. A two-dimensional array refers to a collection of objects in which **each of the objects is a one-dimensional array**. - Similarly, a `three-dimensional` array refers to a collection of two-dimensional arrays, and so on.

>Note that multidimensional arrays **may or may not contain the same number of elements in each row or column**.

Creating an array involves three steps:

- **Declaring** the array

- **Allocating** the array

- **Initializing** the array elements

###Array Declaration

An **array declaration** includes the **array type** and **array variable**. Ezample:

	:::java
	int intArray[]; //One dimentional
	String[] strArray; //One dimentional
	int[] multiArray[]; //Muti dimentional

The square bracket (`[]`)s can follow the array type or its name:

	:::java
	int[] multiArr[];  = int[][] multiArr; = int multiArr[][];
	int[] anArr; = int anArr[];

**The array declaration only creates a variable that refers to `null`**.

**it’s invalid to define the size of an array with its declaration**: i.e. `int[2] nums` is invalid.

###Array Allocation

**array allocation** will allocate memory for the elements of an
array. **When you allocate memory for an array, you should specify its dimensions, such as the number of elements the array should store.**

**The size of an array can’t expand or reduce once it is allocated.**

Because an array is an object, it’s allocated using the keyword `new` , followed by the type of value that it stores, and then its size.

The code won’t compile if you don’t specify the size of the array or if you place the array size on the left of the `=` sign:

	:::java
	intArray = new int[]; //won't compile
	intArray[2] = new int; //won't compile

Once allocated, all the array elements **store their default values**.

Elements in an array that store **object**s default to `null` . -

Elements of an array that store **primitive data type**s store `0` for **integer types ( byte , short , int , long )**

Store `0.0` for **decimal types ( float and double )**

Store `false` for **boolean**

Store `/u0000` for **char data**.

###Array Initialization

	:::java
	//Initialize array in a loop
	for (int i=0; i<intArray.length; i++) {
	intArray[i] = i + 5;
	}

	//Initialize array by assigning value to sepcific element in array
	intArray[0] = 10;
	intArray[1] = 1870;


When you initialize a `two-dimensional array`, you can use nested for loops to initialize its array elements.

Also notice that to access an element in a two-dimensional array, you should use **two array position values**. Example:

	:::java
	for (int i=0; i<multiArr.length; i++) {
		for (int j=0; j<multiArr[i].length; j++) {
			multiArr[i][j] = i + j;
		}
	}

If you try to access a **nonexistence array index position**, `ArrayIndexOutOfBoundsException` will be throwed out, buy complie is fine:

	:::java
	int intArray[] = new int[2];
	//Compile fine even though it access negative position
	System.out.println(intArray[-10]);

Code to access an array element will **fail to compile** if you **don’t pass** it a `char`, `byte`, `short`, or `int` data type.

you can’t remove array positions. For an array of objects, you can set a position to value `null` , but **it doesn’t remove the array position**.

These code will work:

	:::java
	//If you add new() on code below, code will still work
	int intArray[] = {0, 1};
	String[] strArray = {"Summer", "Winter"};
	int multiArray[][] = { {0, 1}, {3, 4, 5} };

However, if you try to specify the size of an array with the following approach, the code won’t compile because **the size of the array is calculated by the number of values that are assigned to the array.**

	:::java
	int intArray2[] = new int[2]{0, 1};
	String[] strArray2 = new String[2]{"Summer", "Winter"};
	int multiArray2[][] = new int[2][]{ {0, 1}, {3, 4, 5}};

If you declare and initialize an array using **two separate lines of code**, you’ll use the keyword `new` to initialize the values. For example:

	:::java
	int intArray[];
	intArray = new int[]{0, 1}; //it is fine if there is new()

Without the keyword `new` code will fail to compile:

	:::java
	int intArray[];
	intArray = {0, 1}; //Will fail to compile

###Asymmetrical Multidimensional Arrays

A `multidimensional array` can be **asymmetrical** (i.e. two parts are not corresponding each other in shape).

Arrays can define a **different number of columns** for each of its rows.

For example, for code below:

	:::java
	String multiStrArr[][] = new String[][]{
	{"A", "B"},
	null,
	{"Jan", "Feb", "Mar"},
	};

An attempt to access any element of this array, such as `multiStrArr[1][0]`, will throw an exception, since second postion is `null`

###Arrays of type interface, abstract class, and class Object

If the type of an array is an `interface`, its elements are **either `null` or objects that implement the relevant interface type**.

For example:

	:::java
	interface MyInterface {}
	class MyClass1 implements MyInterface {}
	class MyClass2 implements MyInterface {}
	class Test {
		MyInterface[] interfaceArray = new MyInterface[]
		{
			new MyClass1(), //Note you use new() here
			null,
			new MyClass2()
		};
	}

If the type of an array is an `abstract class`, its elements are **either `null` or objects of concrete classes that extend the relevant abstract class**.

For example:

	:::java
	abstract class Vehicle{}
	class Car extends Vehicle {}
	class Bus extends Vehicle {}
	class Test {
			Vehicle[] vehicleArray = {
			new Car(),  //Note you use new() here
			new Bus(),
			null
		};
	}

Because all classes **extend** the class `java.lang.Object` , elements of an array whose type is `java.lang.Object` can **refer to any object**.


For example, below is a `object array`, with a **combination** of `interface`, `abs class` and `object`:

	:::java
	interface MyInterface {}
	class MyClass1 implements MyInterface {}
	abstract class Vehicle{}
	class Car extends Vehicle {}

	class Test {
		Object[] objArray = new Object[] {
			new MyClass1(),
			null,
			new Car(),
			new java.util.Date(),
			new String("name"),
			new Integer [7] //Array element of type Object can refer to another array
		};
	}

###Members of an array

Array objects have the following **public members**:

- `length` : *not a method*

- `clone()`: The `return` type of this method is the same as the array’s type.

- Methods **inherited** from the class `Object` , except the method `clone()` .

**The way to accept length**

- `String` — Retrieve length using the **method** `length()`

- `Array` — Determine element count using the **variable** `length`

##ArrayList

**Important Notes about `ArrayList`**

It implements the **interface** `List`.

It **allow**s `null` values to be added to it.

It implements all list operations ( `add()` , `modify()` , and `delete()` values).

It allows `duplicate values` to be added to it.

It maintains its **insertion order**.

You can use either `Iterator` or `ListIterator` (an implementation of the Iterator interface) to **iterate** over the items of an ArrayList .

It supports `generics`, making it type safe. (**You have to declare the type of the elements that should be added to an ArrayList with its declaration**.)

###Create ArrayList

Starting with Java version 7, you **can omit the object type on the right side** of the equal sign and create an ArrayList as follows: `ArrayList<String> myArrList = new ArrayList<>();`

An ArrayList **uses an array** to store its elements. It provides you with the functionality of a dynamic array.

###Add Element to ArrayList

When you add an element to the **end** of the list, the ArrayList first checks whether its instance variable elementData **has an empty slot** at the end.

If no empty slots exist, the method `ensureCapacity()` **creates another array with a higher capacity** and **copies** the existing values to this newly created array. It then copies the newly added
value at the first available empty slot in the array.

When you add an element at a particular position, an ArrayList creates a new array and **inserts all its elements at positions other than the position you specified**. If there are any subsequent elements to the right of the position that you specified, it **shifts them by one position. Then it adds the new element at the requested position**.

###Accessing Elements of an ArrayList

To access the elements of an ArrayList, you can either use Java’s enhanced `for` loop, `Iterator` , or `ListIterator`.

Code Example:

	:::java
	for (String element : myArrList) {
		System.out.println(element);
	}

Code Example:

	:::java
	ListIterator<String> iterator = myArrList.listIterator();
	while (iterator.hasNext()) {
		System.out.println(iterator.next());
	}

An ArrayList **preserves the order of insertion** of its elements.

`Iterator` , `ListIterator` , and the enhanced `for` loop will return the elements in the order in which they were added to the ArrayList . - - An **iterator** ( `Iterator` or `ListIterator` ) lets you **remove** elements as you iterate an ArrayList.

**It’s not possible to remove elements from an ArrayList while iterating it using a `for` loop**.

###Modify Elements of an ArrayList

You can modify an ArrayList by either **replacing an existing element** in ArrayList or **modifying all of its existing values**.

	:::java
	myArrList.set(1, "One and Half");

###Deleting the Elements of an ArrayList

ArrayList defines two methods to remove its elements, as follows:

- `remove(int index)`

- `remove(Object o)`

	:::java
	//Assume we have 'One'...'Four' in myArrList
	myArrList.remove(1);
	for (StringBuilder element:myArrList)
	{
	System.out.println(element);
	}
	myArrList.remove(sb3);
	myArrList.remove(new StringBuilder("Four")); //This line will note remove "Four"
	for (StringBuilder element : myArrList)
	{
	System.out.println(element);
	}

**Important**

We are not deleting in `for` loop

The removal of the specified element fails because of **the manner in which the object references are compared for equality.**

Two objects are equal if their object references (the variables that store them) point to the same object.

When elements of an ArrayList are removed, the remaining elements are re-arranged at their correct positions.

###Other methods of ArrayList

You can **add multiple elements to an ArrayList from another ArrayList or any other class that is a subclass of Collection** by using the following overloaded versions of method `addAll()` :

>`addAll(Collection<? extends E> c)` : **appends** all of the elements in the specified collection to **the end of this list** in the order in which they’re returned by the specified collection’s Iterator .

>`addAll(int index, Collection<? extends E> c)`: inserts all of the elements in the specified collection into this list, starting at the specified position.

	:::java
	ArrayList<String> myArrList = new ArrayList<String>();
	myArrList.add("One");
	myArrList.add("Two");
	ArrayList<String> yourArrList = new ArrayList<String>();
	yourArrList.add("Three");
	yourArrList.add("Four");
	myArrList.addAll(1, yourArrList);
	for (String val : myArrList)
	{
		System.out.println(val); //One Three Four two
	}

What happens if you modify the common object references in these lists, `myArrList` and `yourArrList`?

>By default, **objects are considered `equal` if they are referred to by the same variable (the `String` class is an exception

>We have two cases here: In the first one, you **reassign** the object reference using either of the lists. In this case, the value in the second list will remain **unchanged**.
>In the second case, you **modify the internals** of any of the common list elements—in this case, the change **will be reflected** in both of the lists.

You can **remove all** the `ArrayList` elements by calling `clear()` on it

`get(int index)` —This method returns the **element at the specified position** in this list. **If the requested element isn’t within the range, the get method throws a `java.lang.IndexOutOfBoundsException` error at runtime.**

`size()` —This method returns the number of elements in this list.

`contains(Object o)` —This method returns `true` if this list contains the specified element.

`indexOf(Object o)` —This method returns the **index** of the **first occurrence** of the specified element in this list, or `–1` if this list doesn’t contain the element.

`lastIndexOf(Object o)` —This method returns the **index** of the **last occurrence** of the specified element in this list, or `–1` if this list doesn’t contain the element.

An ArrayList can accept **duplicate** object values.

The method `clone()` defined in the class `ArrayList` returns a **shallow copy** of this ArrayList instance. **Shallow copy** means that this method creates a **new instance** of the ArrayList object to be cloned. **Its `element references` are copied, but the `object`s
themselves are not.**

	:::java
	public class MiscMethodsArrayList5 {
		public static void main(String args[]) {
			ArrayList<StringBuilder> myArrList = new ArrayList<StringBuilder>();
			StringBuilder sb1 = new StringBuilder("Jan");
			StringBuilder sb2 = new StringBuilder("Feb");
			myArrList.add(sb1);
			myArrList.add(sb2);
			myArrList.add(sb2);
			\****************************\
			ArrayList<StringBuilder> assignedArrList = myArrList;
			ArrayList<StringBuilder> clonedArrList =
			(ArrayList<StringBuilder>)myArrList.clone();
			System.out.println(myArrList == assignedArrList); //true
			System.out.println(myArrList == clonedArrList); //false
			\********************************\
			StringBuilder myArrVal = myArrList.get(0);
			StringBuilder assignedArrVal = assignedArrList.get(0);
			StringBuilder clonedArrVal = clonedArrList.get(0);
			System.out.println(myArrVal == assignedArrVal); //true. Refer to same object as below
			System.out.println(myArrVal == clonedArrVal); //true
		}
	}

###Create an Array from ArrayList

You can use the method `toArray()` to return an array containing all of the elements in an ArrayList in sequence from the first to the last element.

Method `toArray()` doesn’t return a reference to this array. It **ceates a new array, copies the elements of the ArrayList
to it and then returns it**


The **references to the individual ArrayList** elements are copied to the returned array and are **still referred to by the ArrayList** .

So if you **modify the returned array** by, say, swapping the position of its elements or by assigning new objects to its elements, the elements of **ArrayList won’t be affected**.

But, if you **modify the state of (mutable) elements of the returned
array**, then the modified state of elements **will be reflected** in the ArrayList .

##Comparing Objects for Equality

The default implementation of the `quals()` method **only compares
whether two object variables refer to the same object**.

Because `instance variable`s are used to store the **state** of an object, **it’s common to compare the values of the instance variables** to determine whether two objects should be considered `equal()`.

The `equals()` method in the class `String` returns `true` only if the object that’s being compared to is **a String with the same sequence of characters**.

The method `equals()` defines **a method parameter** of type Object ,
and its return type is `boolean` .

Don’t change the **name** of the method, its **return type**, or the **type of method parameter** when you define (**override**) this method in your class to compare two objects.

The Java API defines a **contract for the `equals()` method**, which should be taken care of when you implement it in any of your classes:

- It is **reflexive**: for any `non-null` reference value x , `x.equals(x)` should return true .

- It is **symmetric**: for any `non-null` reference values x and y , `x.equals(y)` should return true if and only if `y.equals(x)` returns true .

- It is **transitive**: for any `non-null` reference values x , y , and z , if `x.equals(y)` returns true and `y.equals(z)` returns true , then `.equals(z)` should return true .

- It is **consistent**: for any `non-null` reference values x and y , multiple invocations of `x.equals(y)` consistently return `true` or consistently return `false` , provided no information used in `equals()` comparisons on the objects is modified.

- For any non- null reference value x , `x.equals(null)` should return `false` .

**hasCode()**

- The method `hashCode()` is **not called** by the `equals()` method to determine the equality of two objects.

- The `hashCode` of the `key` (an `object`) is used to specify a `bucket number`, which should store its corresponding value.

- The hashCode values of two objects can be the same. When these
collection classes **find the right bucket, they call the equals method to select the correct value object (that shares the same key values)**.

- According to the Java documentation, when you override the `equals()` method in your class, you should also override the `hashCode()` method.
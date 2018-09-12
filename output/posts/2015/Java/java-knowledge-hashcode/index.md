.. title: Java Knowledge: HashCode
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: java-knowledge-hashcode
.. authors: Pengyin Shan
.. description: This post contains the knowledge I just learned about hashCode().



I touched re-write `equal()` when I was doing work in Java Developement, then I learned these exists a `hashCode()` method that I must implement if I re-write `equal()` for objects.

I found very useful posts: <a href="http://tutorials.jenkov.com/java-collections/hashcode-equals.html">Java Collections - hasCode() and equals()</a>, and <a href="http://eclipsesource.com/blogs/2012/09/04/the-3-things-you-should-know-about-hashcode/">The 3 things you should know about hashCode()</a>.

Also refer to <a href="http://docs.oracle.com/javase/7/docs/api/java/lang/Object.html#hashCode()">Oracle API</a> for `hashCode()`.

**Try to avoid change hashCode() unless you are writing hash-related application.**

### Basic Usage

When you insert **objects** to `HashTable`, `HashMap` or `HashSet`, `hashCode()` is called, together with `equal()`. For example, in `hashMap.put("A",a);`, both `equal()` and `hasCode()` are called.

To insert stuff to hash table, you need a hascode to calculate the key for this object. Later you will need hashCode to search the object: hash code **pointing to some area, where you may found the key.**

From Oracle API, `hashCode` returns a hash code, which is a `int` value for the object.

You can use same way you add `getter` and `setter` in `Eclipse` to auto-generate `hashCode()`: *RightClick -> Source -> Generate hashCode() and equals()*.

Code Example:

	:::java
	public class Employee {
	  protected long   employeeId;
	  protected String firstName;
	  protected String lastName;

	  public int hashCode(){
	    return (int) this.employeeId; //Edit hashCode
	  }
	}
	/***OR**/
	  public int hashCode(Object o){
	     return (int)this.employeeId *
	                firstName.hashCode() *
	                lastName.hashCode();
	   }

### Important Notes

If two objects are equal, based on `equal()`, they must also have the **same hash code**.

If two objects have the same hash code, they **may not be equal**.

Above means two different objects can pointing to the same grid in a hash code grid table.

>You must implement `hashCode()` when you implement `equal()`

>If you don't implement both, original `hashCode()` will treat your new two objects unequal, which you have re-defined `equal()` to make them equal. I.E. Now we have two objects are equal but with different hash code. This violate first rule.

Since `hashCode()` can change **from one java class library (e.x.String v.s. StringBuilder) to another, or from one version to another**,be careful and you cannot use them in `distributed` applications.
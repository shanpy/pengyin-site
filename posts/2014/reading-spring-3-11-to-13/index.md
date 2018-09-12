.. title: Reading Notes for Spring 3 Core Components Tutorial Part II (Chapter 11 to Chapter 13)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-11-to-13
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part II (Chapter 11 to Chapter 13)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

This note includes Chapter 11 to Chapter 13 in tutorial.

#Chapter 11: Spring Dependency Injection

Dependency Injection (or Wiring) helps in gluing individual application classes together and same time keeping them independent.

There are two types of DI: `Constructor-Based` DI and `Setter-Based` DI:

- Constructor-based DI is accomplished when the container invokes a *class constructor* with a number of arguments, each representing a dependency on other class.

- Setter-based DI is accomplished by the container calling *setter* methods on your beans *after* invoking a *no-argument constructor* or *no-argument static factory* method to instantiate your bean.

It is a good practive to *use constructor arguments for* **mandatory dependencies** *and setter for* **option dependencies**

##Constructor-Based Dependency Injection

Example:

XML:

	:::xml
	<bean id="textEditor" class="com.sample.TextEditor">
		<contructor-arg ref="spellChecker"/>
	</bean>

	<bean id="spellChecker" class="com.sample.spellChecker">
	</bean>

JAVA:

	:::java
	//Constructor for textEditor
	public class TextEditor{
		private SpellCheck spellChecker;
		//Constructor that takes one argument
		public TextEditor(SpellCheck spellChecker){
			//A SpellCheck will be instantiated first, based on bean setting
			System.out.println("Construcor of Text Editor");
			this.spellChecker = spellChecker;
		}
		public void spellCheck(){
			spellChecker.checkSpelling();
		}
	}

	//Constructor for spellChecker
	public class spellChecker{
			//Construcor that doesn't take any argument
			System.out.prinln("Construcor of Spell Checker")'
		}
		public void checkSpelling(){
			System.out.println("Checking Spelling !");
		}

	//Main Class
	public class Main{
		pulic void static main(String[] args){
		ApplicationContext context = new ClassPathXmlApplicationContext('bean.xml');

		TextEditor te = (TextEditor) context.getBean('textEditor');
		te.spellCheck();

		//Output: Contrutor of Spell Checker
		//Output: Contrutor of Text Editor
		//Output: Check Spelling !
		}
	}

##Consructor Arguments Resolution

`Ambiguity` can happen when a constroctor takes more than one parameters. Spring make sure the *order* of `constrctor-arg` in bean `xml` file defines the *order* of parameters taken by construcor in `java` file.

If you have `type` attribute in `xml` file, Spring can use *Type-Matching* to check these parameters.

**Important**: If you try to pass *reference* in `<constructor-args>`, use `ref` attribute. If you try to pass *value* in `<constructor-args>`, use `value` attribute.

The best way is to use `index` attribute in `xml` file. Example:

XML:

	:::xml
	<beans>
		<bean id="foo" class="x.y.Foo">
			<constructor-arg index="0" ref="bar"/> <!--part by reference-->
			<constroctor-arg index="1" type="java.lang.String" value="Test"/> <!--pass by value. Specify type here-->
		</bean>

		<bean id="bar" class="x.y.Bar"/>
	</beans>

JAVA:

	:::java
	//Class for Foo
	public class Foo{
		public Foo(Bar bar, Stirng t){
			//Here bar call its own constructor
			//t have value "test", which is defined in xml file
		}
	}

##Setter-based Dependncy Injection

Example:

XML:

	:::xml
	<bean id="textEditor" class="com.sample.TextEditor">
		<property name="spellChecker" ref="spellChecker">
	</bean>

	<bean id="spellChecker" class="com.sample.SpellChecker">

JAVA:

	:::java
	//Class for spellChecker
	public class SpellChecker{
		//Constructor
		public SpellChecker(){
		System.out.println("spellChecker constructor!");
		}
		public void checkSpelling(){
		System.out.println("checkSpelling!");
		}
	}

	//Class for textEditor
	//This class use default-construcor (i.e, no self-defined constructor)
	public class TextEditor{
		private SpellChekcer spellChecker;

		//getter to ruturn a spellChecker
		public SpellChecker getSpellChecker{
			return spellChecker;
		}
		//setter
		public ovid setSpellChecker(SepellChekcer spellChecker){
			System.out.println("setSpellChecker!");
			this.spellChecker = spellChecker;
		}
		public void spellCheck(){
			spellChecker.checkSpelling();
		}
	}

	//Main Class
	public class Main{
		public static void main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext('beans.xml');
			(TextEditor) te = (TextEditor) context.getBeans('textEditor');
			te.spellCheck();
		}

		//Output: spellChecker constructor!
		//setSpellChecker!
		//checkSpelling!
	}

The difference in `xml` file between Constructor DI and Setter-Base DI is: `<construcotr-args>` is used by Constructor DI; `<property>` is used by Setter-Based DI.

Similar as Constructor DI, if you want to pass *reference* in `xml` file, use `ref` attribute. If you want to pass *value* in `xml` file, use `value` attribute.

*XML Configuration using P-Namespace*

`p-namespace` is easier for a bean with *many* setter methods.

	:::xml
	<!--old way-->
	<bean id="test" class="com.sample.test">
		<property name="name" value="John Smith"/>
		<property name="spouse" ref="jane"/>
	</bean>
	<bean id="jane" class="com.sample.Person">
		<property name="name" value="John Smith"/>
	</bean>

	<!--new way-->
	<bean id="test" class="com.sample.test"
		p:name="John Smith"
		p:spouse-ref = "jane"
	> <!--you don't need -value attribute if you pass by value-->
	</bean>
	<bean id="jane" class="com.sample.Person"
		p:name="John Smith"
	>
	</bean>

#Chapter 12: Spring Injecting Inner Beans

The code above can be transferred to `inner bean`. Just like `inner class` in Java, `inner bean` is the bean defined inside `<construcor-args>` or `<property>`.

Example:

XML:

	:::xml
	<bean id="testEditor" class="com.sample.testEditor">
		<property name="spellChecker"> <!--only bean has id-->
			<bean id="spellChecker" class="com.sample.spellChecker"/>
		</property>
	</bean>

JAVA:

	:::java
	//Assume the getter and setter for testEditor are the same as above
	//Assume construcor for spellChecker is the same as above
	//Assue main class is the same as above

	//Output: spellChecker constructor!
	//setSpellChecker!
	//checkSpelling!

#Chapter 13: Spring Injecting Collection

Spring has data type so you can pass value groups in `xml` file. There are four types: List, Set, Map and Properties. Difference is following:
images/posts/spring-di-collection.png 

*You can use* `<list>` or `<set>` to wire any implementation of `java.util.Collection` or `Array`.

Same as single value, value collection can be passed by *value* or *reference*.

Example:

XML:

	:::xml
	<beans>
		<bean id="javaCollection" class="com.sample.javaCollection">
			<!--List Example-->
			<property name="addressList">
				<list>
					<value>USA</value>
					<value>USA</value>
					<value>UK</value>
				</list>
			</property>
			<!--Set Example-->
			<property name="addressSet">
				<set>
					<value>USA</value>
					<value>USA</value>
					<value>UK</value>
				</set>
			</property>
			<!--Map Example-->
			<property name="addressMap">
				<map>
					<entry key="1">USA</entry>
					<entry key="2">USA</entry>
					<entry key="3">UK</entry>
				</map>
			</property>
			<!--Property Example-->
			<property name="addressProp">
				<props><!--Note property has different structure-->
					<prop key="one">USA</prop>
					<prop key="two">USA</prop>
					<prop key="three">UK</prop>
				</props>
			</property>
		</bean>
	</beans>

JAVA:

	:::java
	//Class for javaCollection
	public class JavaCollection{
		List addressList;
		Set addressSet;
		Map addressMap;
		Properties addressProp;

		//Assume each one has getter and setter, with corresponding output
	}

	//Class for Test
	public class Test{
		public static void main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext('beans.xml');

			JavaCollection jc = (JavaXollection) context.getBean('javaCollection');

			jc.getAddressList(); //USA, USA, UK
			jc.getAddressSet(); //USA, UK
			jc.getAddressMap(); //1=USA 2=USA 3=UK
			jc.getAddressProp(); //one=USA two=USA three=UK
		}
	}

In `xml` file, you can mix `references` and `values` together:

	:::xml
	<!--List Example-->
	<list>
		<ref bean="addressList1">
		<ref bean="addressList2">
		<value>UK</value>
	</list>
	<!--Set Example-->
	<property name="addressSet">
		<set>
			<ref bean="address1"/>
			<ref bean="address2"/>
			<value>UK</value>
		</set>
	</property>
	<!--Map Example-->
	<map>
		<entry key="one" value="USA"/>
		<entry key="two" value-ref="address1"/>
	</map>

	<!--Reference Bean-->
	<bean id="address1" class="..."></bean>
	<bean id="address2" class="..."></bean>

To use *empty* or *null* value in beans, you can do following:

	:::xml
	<property name="test" value=""/> <!--empty string-->
	<property name="test2"><null/></property> <!--null-->
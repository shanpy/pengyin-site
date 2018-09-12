.. title: Reading Notes for Spring 3 Core Components Tutorial Part Part III (Chapter 14 to Chapter 16)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-14-to-16
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part III (Chapter 14 to Chapter 16)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

This note includes Chapter 14 to Chapter 16 in tutorial.

#Chapter 14: Spring Beans Auto-Wiring

*This is an example of my own problem:* I tried to use `jdbctemplate.update()` function to insert data, which is passed from controller by a *DAO* object.

No matter how hard I try, even using hard-code for sql statement, I kept getting `nested exception: java.lang NullPointerException` error. Problem did not get solved until I realize instead of just declare a DAO object and call update method, I should declare a DAO as a *class variable*, and add `@autowired` to it, such as:

	:::java
	//In xml, we have <bean id="userDAO" class="..."></bean>

	import com.sample.userDAO;

	@Autowired
	userDAO dao;

	public void updateInController(){
		//Object some_object = new Object();
		// some_object.setName()...etc

		//updateOperation() is the method in another class using jdbc.update()
		//If I just create a userDAO instance then do following, I will get NullPointerException
		dao.updateOperation(some_object);
	}

Spring can *auto-wire* relationships between beans without using `<constructor-arg>` or `<property>`

##Auto-wiring Modes

You should be `autowire` attribute of the `<bean/>` element to specify autowire mode for a bean definition. There are four Auto-wiring modes, which are defined in this following table:
images/posts/auto-wiring.png 

`byType` or `constructor` autowiring mode can be used to wire *arrays* and other *typed-collections*.

##Limitations with Autowiring

Autowiring is great to use across a project. However, it do have limitations and you can override it:
images/posts/autowiring-limitation.png 

##Autowiring By Name*

Spring container looks at the beans on which has a `autowirte` attribute in `xml` configuration file.

Then it will go to the java bean class for this bean, and find all attributes that have `setter` for this bean.

Then it will come back to `xml` file, check other bean name, until it find *one* bean that has same *class type (i.e. class="...")* as this bean's attribute variable *name*.

Spring will initialize this bean, based on configuration file. Then Spring will finish previous bean's initialization process.

If Spring finds more than one bean in `xml` file, it will report a error.

Example:

XML:
	:::xml
	<bean id="textEditor" class="com.example.TextEditor" autowire="byName">
	<property name="name" value="Generic Text Editor"/>
	</bean>

	<!--this bean will be detected since it has same name as the attribute which has a setter-->
	<bean id="spellChecker" class="com.example.SpellChecker">
	</bean>

Java:
	:::java
	//java bean class for textEditor
	public class TextEditor{
		private spellChecker spellChecker; //Spring will find this since it has the same name as spellChecker
	 	private String name;

	 	public void setSpellChecker(SpellChecker spellChecker){
	 		this.spellChecker = spellChecker;
	 	}
	 	public SpellChecker getSpellChecker(){
	 		return spellChecker;
	 	}

	 	public void setName(String name){
	 		this.name = name;
	 	}
	 	public String getName(){
	 	 	return name;
	 	}

	 	public void spellCheck(){
	 		spellChecker.checkSpelling();
	 	}
	}

	//java bean class for spellChecker
	public class SpellChecker{
		public spellChecker(){
			System.out.println("Inside spellChecker constructor");
		}
		public void checkSpelling(){
			System.out.println("checkSpelling in spellChecker class");
		}
	}
	//Test class
	public class Test{
		public static void main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

			//In this step, java will do autowire, which include instantiate spellChecker
			TextEditor te = (TextEditor) context.getBean("textEditor");
			te.spellCheck();

			//Output:
			//Inside sellChecker constructor
			//checkSpelling in spellChecker class
		}
	}

##Autowiring By Type

Spring first check `xml` configuration file, find a bean with `autowire` attribute that marked as `byType`.

Spring will go to this bean's java class, then find all its atrribute variables that have `setter`.

Spring comes back to `xml` then go through all the beans. As long as it finds *one* bean that has same *name* as java class attribute's *type*. Spring will instantiate this specific bean.

If Spring finds more than one bean in `xml` file, it will report a error.

Example:

XML:

	:::xml
	<bean id="textEditor" class="com.sample.TextEditor" autowire="byType">
	<property name="name" value="Generic Text Editor"/>
	</bean>
	<bean id="xxx" class="com.sample.SpellChecker">
		<!-- Here is different from auto-wiring by name. Although we use a different id, Spring still find its type is SpellChecker, which is the type that the original attribute has, so Spring can recoginize it as same type-->
	</bean>

Java:

	:::java
	//TextEditor.java and SpellChecker.java are the same as above
	public class Test{
		public void static main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");
			(TextEditor) te = (TextEditor) context.getBean("textEditor");

			te.spellCheck();

			//Output:
			//Inside sellChecker constructor
			//checkSpelling in spellChecker class
		}
	}

##Autowiring By Constructor

Autowirng by *constructor* is very similar to autowiring by *type*. The only difference is it works on *constructor*.

So now Spring will check `xml` file with `autowire="constructor"` attribute, then go to this java bean class and find this bean's constructor parameters.

Spring comes back to `xml` and go through all beans. As long as it find *one* bean that has same *name* as the *type* of constructor parameter, Spring will instantiated this bean based on its configuration, then instantiates original bean.

If Spring find more than one bean which hava same name as original bean's constructor parameter type, it will report an error.

Example:

XML:

	:::xml
	<bean id="textEditor" class="com.sample.TextEditor" autowire="constructor">
		<constructor-arg value="Generic Text Editor"/>
		<!--note this value has String type. So when Spring go to construcor, it will try to find a string parameter and put value on it-->
	</bean>
	<bean id="ttt" class="com.sample.SpellChecker">
		<!-- Here ttt bean has class as SpellChecker and the original bean's contructor use parameter which also has type as SpellChecker, so Spring can recoginize it as same type-->
	</bean>

JAVA:

	:::java
	private SpellChecker spellChecker;
	private String name;

	//Spring will find a bean that has id as SpellChecker
	public TextEditor(SpellChecker spellChecker, String name){
		this.spellChecker = spellChecker;
		this.name = name;
	}

	public SpellChecker getSpellChecker(){
		return spellChecker;
	}
	public String getName(){
		return name;
	}
	public void spellCheck(){
		spellChecker.checkSpelling();
	}

	//Assuame SpellChecker.java is the same as example above
	public Test{
		public static void main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext();
			TextEditor te = (TextEditor) te.getBean("beans.xml");
			te.spellCheck();

			//Output:
			//Inside sellChecker constructor
			//checkSpelling in spellChecker class
		}
	}

#Chapter 15: Spring Annotation Based Configuration

Instead of using `xml` to do *auto-wiring*, you can use move the auto-wiring part to bean's `java class`.

Since annotation is performed *before* xml configuration, auto-writing in xml can *override* annotation.

To add anonotation, make sure you put `<context:annotation-config/>` in `<beans></beans>` in xml file, then add your bean configuration after this line.

There are four types of annotation:

- `@Required`: apply to `setter` methods

- `@Autowired`: apply to `settter` methods or `non-setter` methods or `constructors` or `properties`.

- `@Qualifier`: apply with `@Autowirted`

- `@JSO-250 Annotations`: includes `@Resource`, `@PostConstruct` adn `@PreDestroy`

##@Required Annotation

`@Required` applys to `setter`. It means a configuration in `xml` for this attribute *type* must be declared. Otherwise it will report `BeanInitializationException` error.

Example:

XML:

	:::xml
	<beans xmlns="...">
		<!-- Must sure you include this for annotation-->
		<context:annotation-config/>

		<bean id="student" class="com.test.Student">
			<property name="name" value="Tim"/>

			<!--Comment this out. @Required will raise error message because of this-->
			<!--<property name="age" value="11"/>
		</bean>
	</beans>

JAVA:

	:::java
	public class Student{
		private Integer age;
		private String name;

		@Required
		public void setAge(Integer aga){
			this.age = age;
		}
		public Integer getAge(){
			return age;
		}

		@Required
		public void setName(String name){
			this.name = name;
		}
		public String getName(){
			return name;
		}
	}

	//Now if we initialize bean "student", we will get a error message, said Property 'age' is required for bean "student"

##@Autowired Annotation

###@Autowired on Setter Methods

Instead of put `<property>` in `xml` file, you can use `@Autowired` on setter to do a *byType autowiring*.

Example:

XML:

	:::xml
	<beans xmlns="...">
		<context:annotation-config/>

		<bean id="textEditor" class="com.sample.TextEditor">
		</bean>

		<bean id="spellChecker" class="com.sample.SpellChecker">
		</bean>
	</beans>

JAVA:

	:::java
	public TextEditor{
		private SpellChecker spellChecker;

		@Autowired
		public void setSpellChecker(SpellChecker spellChecker){
			this.spellChecker = spellChecker;
		}
		public SpellChecker getSpellChecker(){
			return spellChecker;
		}
		public void spellCheck(){
			spellChecker.checkSpelling();
		}
	}

	//Assume SpellChecker.java is the same as exmaple above
	//Assume main class is the same as example above

	//Output:
	//Inside sellChecker constructor
	//checkSpelling in spellChecker class

###@Autowired on Properties

Instead of creating a `setter`, you can put `@Autowired` annotation on the property/attribute declaration.

In `xml`, after you configure using `<property>`, Spring will automatically create a `setter` for this attribute, using the configuration in `xml` file for setter's bean. If you define a value in `<property>`, the value will be passed.

When Spring search for corresponding setter bean in `xml` file, it will refer `id` in each beans.

Example:

XML:

	:::xml
	<beans xmlns="...">
		<context:annotation-config/>
		<bean id="textEditor" class="com.sample.TextEditor">
			<property name="spellChecker" />
			<!-- You should do <property name='test' value="ttt"/> if SpellChecker has a String attribute called test and you want its value to be "ttt"-->
		</bean>
		<bean id="spellChecker" class="com.sample.SpellChecker">
		</bean>
	</beans>

JAVA:

	:::java
	public TextEditor{
		@Autowried
		private SpellChecker spellChecker;
		//Now Spring will set for a bean with id "spellChecker", and create setter based on that bean

		public TextEditor(){
			System.out.prinlnt("construtor for TextEditor");
		}
		public SpellChecker getSpellChecker(){
			return spellChecker;
		}
		public void spellCheck(){
			spellChecker.checkSpelling();
		}
	}

	//Now, if we run Text.java in example above, we will get:
	//construtor for TextEditor.    Since we have constructor now, when we instanitated a TextEditor bean, constructor will be called first.
	//Inside sellChecker constructor    This is in SpellChecker.java, since we call spellCheck() function
	//checkSpelling in spellChecker class

###@Autowired on Constructors*

`@Autowired` on constructor means even if no `<constructor-arg>` exists, Spring should check if there is any bean that has same `id` as constructor's *parameter name*.

Example:

	:::java
	//Assume bean.xml is the same as above
	public TextEditor{
			private SpellChecker spellChecker;

			@Autowired
			public TextEditor(SpellChecker spellChecker){
				System.out.println("TextEditor Constructor");
				this.spellChecker = spellChecker;
			}
			}

	//If we do same thing in test.java we will get:
	//TextEditor Constructor     This is because we call this first in construtor
	//Inside sellChecker constructor
	//checkSpelling in spellChecker class

###@Autowired with (required=false) Option

When you add `@Autowired` to setter, you can add use `@Autowired(required=false)` to make sure if this setter doesn't has a bean in `xml` file, it is still fine.

###@Qualifier Annotation

You can use `@Qualifier` with `@Autowire` to select *only one* bean if you have many beans with *same type*. This should be added on properties.

Example:

XML:

	:::xml
	<context:annotation-config/>

	<bean id="all" class="com.sample.All"></bean>

	<bean id="item1" class="com.sample.Item">
	<property name="name" value="Tim"/>
	</bean>

	<bean id="item2" class="com.sample.Item">
	<property name="name" value="Jane"/>
	</bean>

JAVA:

	:::java
	public class All{
		@Autowired
		@Qualifier("item1")
		private Item item;

		public All(){

		}
		public void printName(Item item){
			System.out.prinlnt(item.getName());
			//If you test it, this should output "Tim" because we only autowire with "item1"
		}
	}

##Spring JSP-250 Annotations

###@PostContruct and @PreDestroy Annotations

`@PostConstruct` is to be added on the method that `init=XXX` in `xml` file.

`@PreDestroy` is to be added on the method that `destroy=XXX` in `xml` file.

###@Resource

Follows *byName* convention, it takes a *self-defined* name or default *property* or *setter* name in java file, then come to `xml` file to find the bean with same name.

It can be added on `properties` or `setters`.

Example:

	:::java
	//Now it will try to find bean with name "XXX". If name is not defined, it will find bean with name "spellChecker"
	@Resource(name="XXX")
	public void setSpellChecker(SpellChecker spellChecker){
		//...
	}

#Chapter 16: Spring Java Based Configuration

Java based configuration enables you to write most of your Spring configuration without xml.

##@Configuration and @Bean

`@Configuration` applys to a `class`, which means this java class is used to configure Spring beans (i.e. It is a `IoC Container`).

`@Bean` applys to `properties`/`methods` inside configuration class. It automatically pick up bean ID and returns actual bean.

A `@Configuration` class can have more than one `@Bean`.

Use `AnnotationConfigApplicationContext` to get context.

You can do `context.register();` to load more than one configuration class to one context:

	:::java
	//If you only load one java configuration class here, you can use ApplicationContext ctx = new AnnotationConfigApplicationContext();
	AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext();

	ctx.register(AppConfig.class, OtherAppConfig.class);
	ctx.refresh();

	Item1 item = ctx.getBean(ItemOne.class); //ItemOne should be marked with @Bean

Example:

	:::java
	//This is not HelloWorld.java. This is the special Spring configuration class
	@Configuration
	public class HelloWorldConfig{
		@Bean
		public HelloWorld helloWorld(){
			return new HelloWorld();
			//Since this is a bean, Spring will find HelloWorld.java for instantiation
		}
	}

	public class HelloWorld{
		private String message;
		//Assume we have getter and setter for message
	}

	public class Test{
			public static void main(String[] args){
				ApplicationContext ctx = new AnnotationConfigApplicationContext(HelloWorldConfig.class); //Find Config Class

				HelloWorld hw = (HelloWorld) ctx.getBean(HelloWorld.class);	//Find Bean
				//Now HelloWorld getter and setter will work if we call them
		}
	}

##Injecting Bean Dependencies

To mark one bean has *dependency* with another bean, just *call* this bean from anther bean.

Example:

	:::java
	@Configuration
	public class TextEditorConfig{
		@Bean
		public TextEditor textEditor(){
			return new TextEditor(spellChecker());
			//This means TextEditor has constrctor-arg or property that needs to call spellChecker
		}
		@Bean
		public SpellChecker spellChecker(){
			return new SpellChecker();
		}
	}

	publc class TextEditor{
		private SpellChecker spellChecker; //You still need to define another bean(spellChecker) in this bean class

		public TextEditor(SpellChecker spellChecker){
			System.our.println("TextEditor Constructor");
			this.spellChecker = spellChecker;
			//You needs to put spellChecker as constructor parameter here, because you define this way in config java class
		}
		public void spellCheck(){
			spellChecker.checkSpelling();
		}
	}

	//Assume we SpellCheck.java is the same as examples before with a constrctor
	//Assume Test.java is the same as example before
	//Output should be:
	//SpellChecker Constructor  This comes first because since spellChecker is constructor parameter, it goes to instantiate this bean first
	//TextEditor Constructor
	//CheckSpelling

##@Import Annotation

You can use `@Import` for beans from another configuration class.

When you define class to ApplicationContext, only non-import bean needs to be defined.

Example:

	:::java
	@Configuration
	public class AConfig{
		@Bean
		public A a(){
			//Assume there exists a A class
		}
	}
	@Configuration
	@Import(AConfig.class)
	public class BConfig{
		@Bean
		public B a(){
		//Assume there exists a B class
		}
	}
	//main class
	ApplicationContext ctx = new AnnotationConfigApplicationContext(BConfig.class);

	//Both AConfig and BConfig are available
	A a = ctx.getBean(A.class);
	B b = ctx.getBean(B.class);

##Init and Destroy

You can use `initMethod` and `destoryMethod` with `@Bean` for initialization and destroy of the bean:

	:::java
	public class Foo{
		public void init(){
		//...
		}
		public void cleanup(){
		//...
		}
	}

	@Configuration
	public class FooConfig{
		@Bean(initMethod="init", destroyMethod="cleanup")
		public Foo foo{
			return new Foo();
		}
	}

##Bean Scope

Default scope is `singleton`. You can use `@Scope` to define other scopes:

	:::java
	@Bean
	@Scope("prototype")
	public Foo foo(){
		return new Foo();
	}
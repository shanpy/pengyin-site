.. title: Reading Notes for Spring 3 Core Components Tutorial Part I (Chapter 1 to Chapter 10)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-1-to-10
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part I (Chapter 1 to Chapter 10)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

#Chapter 2: Spring Framework Architecture

Spring is a modular framework, which means you can pick the modules that only fits your need. Basic structure of Spring framework is following. There are three *main* componets: `Core Container`, `Data Access Integration` and `Web (MVC/Remoting)`. Other important componets include `AOP`, `Aspects`, `Instrumentation` and `Test`:
images/posts/spring-structure.png 

##Core Container

`Core Container` contains: `Core` module, `Beans` module, `Context` module and `Expression Language` module:

- `Core`: fundamental of framework, including `loC` and `Dependency Injection` features.

- `Beans`: has `Bean Factory`, implementing *factory pattern*.

- `Context`: based on `Core` module and `Beans` module. It is a medium to *access* any objects defined and configured. The `ApplicationContext` interface is the focal point of the `Context` module.

- `Expression Language`: provides language for *querying* and *manipulating* an object graph at run time.

##Data Access/Integration

`Data Access/Integration` contains: `JDBC` module, `ORM` module, `OXM`, `JMS` module and `Transaction` module:

- `JDBC`: provides a *JDBC-abstraction* layer that can simplify JDBC coding

- `ORM`: provide *integration* for popular *object-mapping* APIs, including `JPA`, `JDO`, `Hibernate`, `iBatis`.

- `OXM`: provide integration for *Object/XML mapping*, such as `JAXB`, `Castor`, `XMLBeans`, `JiBX` and `XStream`

- `JSM`: *Java Messaging Service*. It can producing and consuming messages.

- `Transaction`: contains programmatic and declarative *transaction management* for classes and POJOs.

##Web

`Web` contains: `Web` module, `Web-Servlet` module, `Web-Struts` module and `Web-Portlet` module:

- `Web`: provide important functions for web development, such as `multipart file uploader` and `loC container` using `servlet listeners` and a web-oriented `application context`.

- `Web-Servlet`: provide Spring `MVC` implementation

- `Web-Structs`: provide support for Structs

- `Web-Portlet`: provide `MVC` implemention to be used in a *portlet* environment.

##Other Components

- `AOP` module provides `aspect-oriented` programming implementation, allowing you to define method-interceptor or *pointcut*s to cleanly *decouple* code that implements functionality that should be *seperated*.

- `Aspects` module provides support for `AspectJ`.

- `Instrumenetation` module provide *class instrumentation* support and *class loader* implementation for certain application servers.

- `Test`: provides testing support for `JUnit` or `TestNG`

#Chapter 5: Spring Ioc Containers

The main function of Spring IoC Container is to *create* objects, *wire* objects together, *configure* objects and *manage* objects in their lifecyle.

Spring IoC containter uses `dependency injection/DI` to manage objects, which are called spring `beans`.

Container gets information from the `metadata` in `xml`, `Java annotation` or `Java code`.

This is the process of Spring IoC container works:
images/posts/spring-containers.png 

Spring has two distinct type of containers: `BeanFactory` and `ApplicationContext`:

`BeanFactory`: this is the *simplest* container from DI. Most commonly used implementation is `XmlBeanFactory` class. It reading the configuration metadata from `xml` file and use it.

XML:

	:::xml
	<bean id="helloWorld" class="com.example.helloWorld">
		<property name="message" value="Hello World!"/>
	</bean>

JAVA:

	:::java
	public class helloWorld{
		private String message; //with getter and setter
	}

	public class test{
		public static void main(String[] args){
			XmlBeanFactory factory = new XmlBeanFacotry(new ClassPathResource('Beans.xml'));
			//Note we use ClassPathResource so spring will find relative address for Beans.xml

			helloWorld obj = (helloWorld) factory.getBean("helloWorld");
			//Using casting here. Notice the factory.getBean() method use corespoding bean id. Then find name of class variable in <property>

			obj.getMessage(); //return message in getter, which is Hello World!
		}
	}

`ApplicationContext`: More advanced and widely used container compare to the one above. This includes some enterprise-function. Most common implementations are: `FileSystemXmlApplicationContext`, `ClassPathXmlApplicationContext` and `WebXmlApplicationContext`.

`FileSystemXmlApplicationContext`: loads the definations of the beans from `xml` file. Note you need to provide *full path* of xml bean configuration file path. Example:

	:::java
	//Use same xml example as above

	ApplicationContext context = new FileSystemXmlApplicationContext("C:/Users/pshan/workspace/Sample/Beans.xml"); //You need full path here

	helloWorld obj = (helloWorld) context.getBean("helloWorld"); //Use casting here

	obj.getMessage(); //return message in getter (i.e, property in xml), which is Hello World!

`ClassPathXmlApplicationContext`: example is in `BeanFactory Container`. You *do not* need *full* path of xml file but you need *Class Path* to let spring find xml configuration file.

`WebXmlApplicationContext`: loads all beans with in a `web` application from xml.

#Chapter 6: Spring Bean Definition

`Beans` are *objects* that are initialized, assembled, and otherwise managed by Spring IoC *Container*. They are created with the `configuration metadata` that supplied by `<bean/>` defination from `xml` file.

`Configuration MetaData` provide following:

- How to *create* a bean

- Bean's *lifecycle* details

- Bean's *dependencies*

##Bean Properties

`class`: mandatory. Give the java class that is used to create beans.

`name`: specifies the bean `identifier` uniquely. In an `xml`, you need `id` and/or `name` to specify the bean identifiers.

`scope`: specifies bean *scope*. See notes in chapter 7.

`constructor-arg`: for inject the dependencies. See notes in chapter 8

`properties`:  for inject the dependencies. See notes in chapter 8

`autowiring mode`:  for inject the dependencies. See notes in chapter 8

`lazy-initialization mode`: tells the IoC container to create a bean instance when it is *firstly requested*, rather than at *startup*.

`initialization method`: a `callback` to be called just after all `properties` for the bean have been set by container. See notes in Chapter 8.

`destruction method`: a `callback` to be used when the `container` containing the bean is *destroyed*. See notes in chaper 8.

`Configuration Metadata` can be provided by:

- `xml` based configuration file.

- `Annotation-based` configuration

- `Java-based` configuration

Example of Bean Properties from book:
images/posts/spring-configuration-metadata.png 

#Chapter 7: Spring Bean Scopes

You can declaring *scope* of beans when you creates `<bean/>` in xml file. There are five scopes that Spring support:

`singleton`: *Default*. Spring IoC container cretes *exactly one* instance of the object defined by that bean defination. This object is stored in a *cache* of such singletion beans. A request will return the cached object. Example:

XML:

	:::xml
	<!--beans.xml-->

	<bean id="helloWorld" class="com.sample.helloWorld" scope="singleton">
	</bean>

JAVA:

	:::java
	ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

	helloWorld objA = (helloWorld) context.getBean("helloWorld"); //get from bean id and cast it

	objA.setMessage = "testA";

	helloWorld objB = (helloWorld) context.getBean("helloWorld");

	System.out.prinlnt(objB.getMessage); //print out "testA" since objA and objB are pointing to same bean instance

`prototype`: create new bean instance of object *every time* a *request* for the specific bean is made.

*As a rule, use the prototype scope for all* **state-full** *beans and the singleton scope for* **stateless** *beans*.

	:::java
	//Assume we have same xml as above

	ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

	helloWorld objA = (helloWorld) context.getBean("helloWorld");

	objA.setMessage = "testA";
	objA.getMessage(); // "testA"

	helloWorld objB = (helloWorld) context.getBean("helloWorld");

	objB.getMessage(); //null. Becuase this is a new request and a new instance is created

#Chapter 8: Spring Bean Life Cycle

In java, `initialization` work can be done inside `afterPropertiesSet()` method.

In xml, you can use `init-method` attribute to call a self-defined method when a bean instance is created. Then add this method in your bean java class.

Similarly, `destruction` can be done insdie `destory()` method.
In xml, you can use `destroy-method` attribute to call a self-defined method. You need to add this method in your bean java class.

Example:

XML:

	:::xml
	<bean id="helloWorld" class="com.sample.helloWorld" init-method = "init" destory-method="destroy">
		<property name="message" value="hello World!"/>
	</bean>

JAVA:

	:::java
	//This is the bean class defined in java: com.sample.helloWorld
	public class helloWorld{
		private String message; //The value of message is defined in xml

		public void setMessage(String message){
			this.message = message;
		}
		public void getMessage(){
			System.out.println(message);
		}
		public void init(){
		//This is the initialization method
			System.out.println("create bean");
		}
		public void destroy(){
		//This is the destroy method
			System.out.println("destory bean");
		}
	}

	//Now we test it
	public class Test{
		public static void main(String[] args){
			AbstractApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

			helloWorld obj = (helloWorld) context.getBean("helloWorld");
			obj.getMessage();
			context.registerShutdownHook(); //shutdown if you are in a desktop-application

			//Output: create bean | hello World ! | destroy bean
		}
	}

You can also put `default-init-method` and `defalut-destory-method` attributes in the main bean in `xml` file, such as `<bean xmlns="..." xmlns:xsi="..."></bean>`, to let all beans use same initialization method or destruction method.

#Chapter 9: Spring Bean Post Processors

`BeanPostProcessor` *interface* defines **callback** methods that you can implement to provide your own instantiation logic, dependency-resolution logic, etc.

You can configure multiple BeanPostProcess interfaces. You can control the *order* of them.

Spring IoC container *instantiates* a bean instance and then BeanPostProcessor works.

An `ApplicationContext` automatically detect beans with BeanPostProcessor implementation and register these beans as post-processors. These processors will be automatcally called when bean is created.

Example:

XML:

	:::xml
	<bean id="helloWorld" class="com.sample.helloWorld" init-method="init" destroy-method="destroy">
	<property name="message" value="Hello World!"/>
	</bean>

	<!--bean with BeanPostProcessor-->
	<bean class="com.sample.InitHelloWorld"/>

JAVA:

	:::java
	//Bean Class is defined as example in chapter 8

	//Class for BeanPostProcessor
	public class InitHelloWorld implements BeanPostProcessor{
		//This should be called before bean is initialized
		public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException{
			System.out.println("Before Init!");
			return bean; //Any object can be returned
		}
		//This should be called after bean is initialized
		public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException{
			System.out.println("After Init!");
			return bean; //Any object can be returned
		}
	}

	//Test Class
	public class Test{
		public void static main(String[] args){
			AbstractApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

			helloWorld obj = (helloWorld) context.getBean("helloWorld");
			obj.getMessage();
			context.registerShutdownHook();

			//Output: Before Init!
			//create bean
			//After Init!
			//Hello World!
			//destry bean
		}
	}

#Chapter 10: Spring Bean Definition Inheritance**

A `parent bean` can be inherited by a `child bean`. Child bean can *override* parent bean's attributes.

`parent` attribute should be used in `xml` file to define a parent bean in child bean.

Example:

XML:

	:::xml
	<bean id="parentBean" class="com.sample.parentBean">
		<property name="message1" value="Parent Message 1"/>
		<property name="message2" value="Parent Message 2"/>
	</bean>

	<bean id="childBean" class="com.sample.childBean" parent="parentBean"> <!--note we find parent bean id here-->
		<property name="message1" value="Child Message1"/>
		<property name="message3" value="Child Message3"/>
	</bean>

JAVA:

	:::java
	//Assume we have a normal setter and getter for both parent and child bean

	public class Test{
		public void static main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

			parentBean p = (parentBean) context.getBean('parentBean');
			p.getMessage1(); //Parent Message 1
			p.getMessage2(); //Parent Message 2

			childBean c = (childBean) context.getBean('childBean');
			c.getMessage1();
			//Child Message 1: Override attribute from parent bean
			c.getMessage2();
			//Parent Message 2: Important! c inherient property from parent bean, so it will not output null value.
			//However c still need getter and setter for message 2
			c.getMessage3();
			//Child Message 3: child bean can define its own property
		}
	}

You can create `Bean Defination Template` in `xml` file if you need a general parent bean for all childs beans. You *can not* use `class` attribue in bean template. You *must* define `abstruct` attribute as **true**. Example:

	:::xml
	<bean id="templateBean" abstruct="true">
	<!--template bean can not be instantiated since it is abstract-->
		<property name="message1" value="template 1!"/>
		<property name="message2" value="template 2"/>
	</bean>

	<bean id="childBean" class="com.sample.childBean" parent="templateBean">
		<property name="message1" value="child 1!"/>
		<property name="message3" value="child 3!"/>
	</bean>














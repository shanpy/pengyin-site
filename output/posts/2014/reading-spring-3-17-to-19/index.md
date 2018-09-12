.. title: Reading Notes for Spring 3 Core Components Tutorial Part I Part IV (Chapter 17 to Chapter 19)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-17-to-19
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part IV (Chapter 17 to Chapter 19)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

This note includes Chapter 17 to Chapter 19 in tutorial.

#Chapter 17: Event Handling in Spring

In Spring, the `ApplicatonContext` publishes certain types of `events` when loading the beans.

`ApplicationEvent` class and `ApplicationListener` interface is used in `ApplicationContext` to deal with event handling.

If a bean implements `ApplicationListener`, then every time `ApplicatioContext` publish an `ApplicationEvent`, this bean will be notified.

Spring Events are following:
images/posts/spring_events.png 

Spring event handling is *single-threaded*. So if an event is published, unless all receivers get the message, the processes are *blocked* and the flow will not continue.

A bean can *implement* the `ApplicationListener` interface to listen a event. `ApplicationListener` only has one method, which is `onApplicationEvent()`.

Example:

XML:

	:::xml
	<bean id="helloWorld" class="com.sample.HelloWorld">
		<property name="message" value="Hello World!"/>
	</bean>
	<bean id="cStartEventHandler" class="com.sample.CStartEventHandler" />
	<bean id="cStopEventHandler" class="com.sample.CStopEventHandler"/>

JAVA:

	:::java
	public class HelloWorld{
			private String message;
			//Assume we give message a setter and getter
	}
	//This is a listener we defined for start an event. So we implements ContextStartedEvent
	public class CStartEventHandler implements ApplicationListener<ContextStartedEvent>{
		public void onApplicationContext(ContextStartedEvent event){
			System.out.println("ContextStartedEvent Received");
		}
	}
	//This is a listener we defined for stop an event. So we implements ContextStoppedEvent
	public class CStopEventHandler implements ApplicationListener<ContextStoppedEvent>{
		public void onApplicationContext(ContextStartedEvent event){
			System.out.println("ContextStoppedEvent Received");
		}
	}
	public class Test{
		public static void main(String[] args){
			ConfigurableApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

			//Start a event
			context.start();

			HelloWorld obj = (HelloWorld) context.getBean("helloWorld");

			obj.getMessage();

			//Stop an event
			context.stop();
		}
	}

#Chapter 18: Custom Events in Spring**

To create a custom event, you need a `event` class, a `event publisher` class and a `event handler` class:

XML:
	:::xml
	<bean id="customEventHanler" class="com.sample.CustomEventHandler"/>
	<bean id="customEventListener" class="com.sample.CustomEventListener"/>

JAVA:

	:::java
	//To create a custom event, event class needs to extend ApplicationEvent
	public class CustomEvent extends ApplicationContext{
		public CustomEvent(Object source){
			super(source);
		}
		public String toString(){
		return "Custom Event";
		}
	}
	//To create a custom event publisher, publisher class needs to implement ApplicationEventPublisherAware
	public class CustomEventPublisher implements ApplicationEventPublisherAware{
		private ApplicationEventPublisher publisher;

		public void setApplicationEventPublisher(ApplicationEventPublisher publisher){
			this.publisher = publisher;
		}
		public void publish(){
			ConstomEvent ce = new CustomEvent(this);
			publisher.publishEvent(ce);
		}
	}
	//To create a custom event handler, handler class needs to implement ApplicationListener<CustomEvent>
	public class CustomEventHandler implements ApplicationListener(CustomEvent){
		public void onApplicationEvent(CustomEvent event){
			System.out.println(event.toString());
		}
	}
	//...
	ConfiguraableApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

	CustomEventPublisher cvp = (CustomEventPublisher) context.getBean("customEventPublisher");
	cvp.publish(); //My Custom Event
	cvp.publish(); //My Custom Event

#Chapter 19: AOP with Spring Framework

`Aspect Oriented Programming (AOP)` entails *breaking down* program logic into distinct parts called `concerns`,or `crossing-cutting concerns`. These concerns are conceptually separate from the application's bussiness logic.

Spring AOP modules provides interceptors to intercept an application. For example. when a method is executed, you can *add extra functionality* before or after the method execution.

*AOP Terminologies*
images/posts/AOP_Term1.png 
images/posts/AOP_Term2.png 

*Type of Advice*
images/posts/AOP_Advice.png 

##XML Schema Based Aspect Implementation

Use regular classes along with `xml` based configuration

`xml` needs to be configured:

	:::xml
	<beans xmlns="..."
		   xmlns:aop="..."
		   xmlns:schemaLocation="...">
	</bean>

You need to add `AspectJ` libraries to your CLASSPATH.

The way to *declare* an `aspect` is using `<aop:aspect>` element and usint `ref` attribute to find bean:

	:::xml
	<aop:config>
		<aop:aspect id="testAspect" ref="testBean">
		...
		</aop:aspect>
	</aop:config>

	<bean id="testBean" class="...">
	</bean>

The way to *declare* an `pointcut` is to use `<aop:pointcut>` elements. `pointcut` is sued to determine the `method`(i.e. `join point`) to be excuted in advices:

	:::xml
	<aop:config>
		<aop:aspect id="testAspect" ref="testBean">
			<aop:pointcut id="testAttribute" expression="execution(* com.xyz.Classes.*.*(...))"/>
			<!--We use regular expression to make sure all classes under com.xyz.Classes package have a "testAttribute" attribute. This attribute can carry advices-->

			<aop:pointcut id="testArribute2" express="executon(* com.sample.Test.getName(...))"/>
			<!--This means the method getName() in com.sample.Test class has a pointcut called testAttribute2-->
	 	</aop:aspect>
	</aop:config>

	<bean id="testBean" class="...">
	</bean>

The way to *declare* an `advice` is to add *five* advices inside an `<aop:aspect>` element, using `<aop:{ADVICE Name}>` element:

	:::xml
	<aop:config>
		<aop:aspect id="testAspect" ref="testBean">
			<aop:pointcut id="testAttribute" expression="execution(* com.sample.test.*.*(...))"/>

			<aop:before pointcut-ref="testAttribute" method="task"/>
			<aop:after pointcut-ref="testAttribute" method="task"/>
			<aop:around pointcut-ref="testAttribute" method="task"/>

			<aop:after-returning returning="retVal" pointcut-ref="testAttribute" method="task"/><!--method must hava papameter named retVal-->
			<aop:after-throwing throwing="ex" pointcut-ref="testAttribute" method="task"/><!--method must hava papameter named ex-->
		</aop:aspect>
	</aop:config>

	<bean id="testBean" class="...">
	</bean>


Example:

XML:

	:::xml
	<beans xmlns="..."
		   xmlns:aop="..."
		   xmlns:schemaLocation="..."
	>
		<aop:config>
			<aop:aspect id="log" ref="logging"> <!--Spring will find a bean with id logging for aspect class-->
				<aop:pointcut id="selectAll" expression="execution(* com.sample.setName(...))"/>
				<!--Here we define advices trriger for method setName() -->
				<aop:before pointcut-ref="selectAll" method="beforeAdvice"/>
				<aop:after pointcut-ref="selectAll" method="afterAdvice"/>
				<aop:after-returning pointcut-ref="selectAll" returning="retVal" method="afterReturingAdvice"/>
				<aop:after-throwing pointcut-ref="selectAll" throwing="ex" method="AfterThrowingAdvice"/>
			</aop:aspect>
		</aop:config>

		<bean id="student" class="com.sample.Student">
			<property name="name" value="Tim"/>
			<property name="age" value="11"/>
		</bean>

		<bean id="logging" class="com.sample.Logging"/>
	</beans>

JAVA:

	:::java
	public class Logging{
		//Execute before a selected method execution
		public void beforeAdvice(){
			System.out.println("Before Execution");
		}
		//Execute after a selected method execution
		public void afterAdvice(){
			System.out.println("After Execution");
		}
		//Execute when any method returns
		public void afterReturningAdvice(Object retVal){
			System.out.println("Returning Execution");
		}
		//Execute if there is any exception raised
		public void AfterThrowingAdvice(IllegalArgumentException ex){
			System.out.println("Exception Execution");
		}
	}
	public class Student{
		private Integer age;
		private String name;
		//Assume we have getter and setter for them with message print out

		public void printThrowException(){
			System.out.println("Exception raise") throw new IllegalArgumentException();
		}
	}
	public class Test{
		public static void main(String[] args){
			ApplicationContext context = new ClassPathApplicationContext("beans.xml");
			Student student = (Student) context.getBean("student");

			student.getName();
			student.setName("Ann");
			student.printThrowException();
		}
	}

	//Output:
	//Tim
	//Before Execution
	//Returning Execution
	//After Execution
	//Exception Execution

##@AspectJ Based AOP with Spring

`@AspectJ` refers a style of declaring aspects as regular *Java classes* with Java 5 annotations.

You need to add `<aop:aspectj-autoproxy>` in `xml` file first.

You also need AspectJ libraries in your CLASSPATH

To *declaring* an `aspect`, you add `@Aspect` above the class name.

To *declaring* an `pointcut`, you need to declar two parts:

A *pointcut expression* using `@Pointcut`

A *pointcut signature*, which is a method without implementation. The name of the method is like the id of pointcut in `xml` file above:

	:::java
	@Pointcut("execution(*com.sample.*.*(...))") //Pointcut expression, telling Spring the place to exectue advices
	private void testAttribute(); //Pointcut Signature

To *declaring* `advice`, using `@{advice_name}` annotations:

	:::java
	@Before("testAttribute()") //pointcut expression. We use method here
	public void doBeforeTask(){...}

	@Before("testAttribute()")
	public void doAfterTask(){...}

	@Around("testAttribute()")
	public void doAroundTask(){...}

	@AfterReturning(pointcut="testAttribute()",returning="retVal")
	public void doAfterReturnningTask(Object retVal){...}

	@AfterThrowing(pointcut="testAttribute()",throwing="ex")
	public void doAfterThrowingTask(Exception ex){...}

Example:

XML:
	:::xml
	<!--Assume we have xmln:aop...-->
	<aop:aspectj-autoproxy/>

	<!--Assume we have Student bean the same as example above-->
	<!--Assume we have Logging bean the same as example above-->

JAVA:

	:::java
	@Aspect
	public class Logging{
		@Pointcut("exectution(*com.sample.Student.setName(...))")
		private void selectAll();   //If we use xml, this is defined in xml file. Now we move it to jave

		@Before(selectAll())
		public void beforeAdvice(){
			//same as last example
		}
		@After(selectAll())
		public void afterAdvice(){
			//same as last example
		}
		@AfterReturning(pointcut="selectAll()", returning="retVal")
		public void afterReturningAdvice(Object retVal){
			//same as last example
		}
		@AfterThrowing(pointcut="selectAll()" throwing="ex")
		public void AfterThrowingAdvice(IllegalArgumentException ex){
			//same as last example
		}
	}

	//If we run Test.java from last example, we should get same results.
.. title: Reading Notes for Spring 3 Core Components Tutorial Part VI (Chapter 22)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-22
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part VI (Chapter 22)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

This note includes Chapter 22 in tutorial.

#Spring Web MVC Framework

##The Dispacher Servlet

images/posts/dispatcher_servlet.png 

##Required Configuration

XML:

	:::xml
	<!--First: You set up dispacher servlet in web.xml-->
	<web-app id="testWebApp">
		<display-name>Test Web App</display-name>
		<servlet>
			<servlet-name>TestServlet</servlet-name>
			<!--Since we define TestServelt as dispacther servlet here, Spring will now try to find a servlet called TestServlet-servlet.xml in WebContent/WEB-INF directory-->
			<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
			<load-on-startup>1</load-on-startup>
		</servlet>

		<!--servlet-mapping here means all jsp files should be handled by TestServlet-->
		<servlet-mapping>
			<servlet-name>TestServlet</servlet-name>
			<url-pattern>*.jsp</url-patterm>
		</servlet-mapping>

		<!--You can also define your own servlet name instead of [servlet-name]-servelet.xml-->
		<context-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>/WEB-INF/test-servlet</param-value>
		</context-param>
		<!--make sure you add this listener if you want to define your own-->
		<listener>
			<listener-class>org.springframework.web.context.ContextLoadListener</listener-class>
		</listener>
	</web-app>

	<beans xmlns="...">
		<!--Now we create beans and set up ViewResolver, using [servlet-name]-servlet.xml-->
		<context:compont-scan base-package="com.sample"/>
		<!--The line above means we want search Spring MVC Annotation such as @Controller or @RequestMapping in com.sample package-->

		<!--We want to search for /WEB-INF/jsp folder to get .jsp files to resolve view names. For example, a logical view named hello should be a /WEB-INF/jsp/hellp.jsp-->
		<bean class="org.springframework.web.servlet.view.InternalResourceViewResolover">
			<property name="prefix" value="/WEB-INF/jsp"/>
			<property name="suffix" value=".jsp"/>
		</bean>
	</beans>

##Controller

You need `@Controller` annotation to make a controller class, and use `@RequestMapping` to get path and define type of request.

Example:

	:::java
	@Controller
	public class testController{
		@RequestMapping(value="/test", method=RequestMethod.GET)
		public String printHello(ModelMap model){
			model.addAttribute('message','Hello World!'); //Use ${message} in jsp file to get model attribute
			return "index"; //Return a view and string is the logical view name, which is defined in ViewResolver above
		}
	}

##Form Submmision Example

HTML:

	:::html
	<form:form method="POST" action="/HelloWorld/Student" modelAttribute="Person">
	<!--You can also do action="addStudent", which is corresponding controller-->
		<table>
			<tr>
				<td><form:label path="name">Name</form:label></td>
				<td><form:input path="name"/></td>
			</tr>
			<tr>
				<td><form:label path="age">Age</form:label></td>
				<td><form:input path="age"/></td>
			</tr>
			<tr>
				<td><form:label path="id">Id</form:label></td>
				<td><form:input path="id"/></td>
			</tr>
			<tr>
				<td colspan="2"><input type="commit" value="Submit"/></td>
			</tr>
		</table>
	</form:form>

JAVA:

	:::java
	//Assume we hava web.xml, testServlet-servlet.xml, Student.java as example above

	@Controller
	public class testController{

		//This step has other ways to implement it
		@RequestMapping(value="/student", method=RequestMethod.GET)
		public ModelAndView student(){
			return new ModelAndView("student","studentModel",new Student());
			//Here we first create a Student object and go to student view(i.e student.jsp).
			//Note "studentModel" is a model idetifier. Spring use it to recognize "<form:form>" value"
		}

		@RequestMapping(value="/Student",method=RequestMethod.POST)
		public String addStudent(@ModelAttribute("studentModel")Student student, ModalMap model){
			//Since we have set studentModel is a Student object, Spring get attributes from form, and set it to a Student object.
			//So now you can directly use student.getname();
			model.addAttribute("name", student.getname());
			//age, id is the same

			return "result"; //Now you can use ${name}, ${age} and ${id} in result.jsp
		}
	}



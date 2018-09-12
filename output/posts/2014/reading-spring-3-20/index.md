.. title: Reading Notes for Spring 3 Core Components Tutorial Part V (Chapter 20)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-20
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part V (Chapter 20)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

This note includes Chapter 20 in tutorial.

#Spring JDBC Framework

Spring JDBC Framework takes care of all the low-level details starting from opening the connection, prepare and execute the SQL statement, process exceptions, handing transactions and finally close the connection.

`JDBCTemplate` is the most popular approach of using Spring JDBC framework.

##JDBC Template Class

The `JdbcTemplate` class executes SQL queries, update statements and stored procedure calls, performs iteration over `ResultSets` and extraction of returned parameter values. It also catches `JDBC exceptions` and translates them to the generic, more informative, exception hierarchy defined in the `org.springframework.dao` package.

Since instance of `JdbcTemplate` classes are *threadsafe* once it is configured, you can just configure *one* instance of `JdbcTemplate`, then *inject* it to different `DAO`s.

A comment practice is to configure a `DataSource` in your spring configuration file, then *inject* that bean to your `DAO` classes. For example:

	:::xml
	<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
		<property name="driverClassName" value="com.mysql.jdbc.Driver"> <!--MySQL here as an example -->
		<property name="url" value="jdbc:mysql://localhost:3306/TEST"/>
		<property name="username" value="root"/>
		<property name="password" value="password"/>
		<!--You need URL, username and password -->
	</bean>

##Executing SQL Statements

`DAO` means `Data Access Object`. DAO often implements an `interface`, which provides ablity to read/write data from database. Other parts of application access DAO.

The way to achieve CRUD(Create, Read, Update and Delete) operation is (Assume `SQL` ia a SQL statement):

*Query*:

- Query for Integer: `jdbcTemplateObject.queryForInt(SQL);`

- Query for Long: `jdbcTemplateObject.queryForLong(SQL);`

- Query for Int, with a *bind variable*: `jdbcTemplateObject.queryForInt(SQL, new Object[]{10});`

- Query for String, with a *bind variable*: `jdbcTemplateObject.queryForInt(SQL, new Object[]{10}, String.class);`

- Query with `ObjectMapper`. This `ObejctMapper` will be returned after query finishes:

>
	:::java
	//Assume we want a Studnet object being returned
	Student student = jdbcTemplateObject.queryForObject(SQL, new Object[]{10}, new StudentMapper());

	public class StudentMapper implements RowMapper<student>{
		public Student mapRow(ResultSet rs, int rowNum) throws SQLException{
			Student student = new Student();
			student.setName(rs.getSring("name"));
			student.setId(rs.getInt("id"));
			//Just apply these to setters
			return Student;
		}
	}

- Query with `ObjectMapper`, return *multiple objects*:

>

	:::java
	List<Student> students = jdbcTemplateObject.query(SQL,new StudentMapper());
	//StudentMapper class is the same as example above

*Insert*: SQL Statement: `insert into Student(name,age) values (?,?)`. JDBCTemplate: `jdbcTemplateObject.update(SQL, new Object[]{"Tim", 11});`. If you want to insert more, just add more field and and key/value pair to SQL statement and JDBCTemplate.

*Update*: SQL Statement: `update Student set name=? where id=?`. JDBCTemplate: `jdbcTemplateObject.update(SLQ, new Object[]{"Time",1});`

*Delete*: SQL Statement: `delete Student where id=?`. JDBCTemplate: `jdbcTemplateObject.update(SQL, new Object[]{10});`

*Create*: SQL Statement: `CREATE TABLE STUDENT(` + `ID  INT NOT NULL AUTO_INCREMENT`, etc. JDBCTemplate: `jdbcTemplateObject.execute(SQL);`

Example:

XML:

	:::xml
	<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
		<property name="driverClassName" value="com.mysql.jdbc.Driver"> <!--MySQL here as an example -->
		<property name="url" value="jdbc:mysql://localhost:3306/TEST"/>
		<property name="username" value="root"/>
		<property name="password" value="password"/>
		<!--You need URL, username and password -->
	</bean>

	<bean id="studentDAOImpl" class="com.sample.StudentDAOImpl">
		<property name="datSource" ref="dataSource"/>
	</bean>

JAVA:

	:::java
	//Assume we have a Student class with getter and setter for id, name and age attribute.

	public class StudentMapper implements RowMapper<Student>{
		public Student mapRow(ResultSet rs, int rowNum) throws SQLException{
			Student student = new Student();
			student.setName(rs.getSring("name"));
			student.setId(rs.getInt("id"));
			student.setAge(rs.getInt("age"));
			return Student;
		}
		}

	import javax.sql.DataSource;
	import org.springframework.jdbc.core.JdbcTemplate;

	public interface StudentDAO{
		//Initialize database resource. i.e. connection
		public void setDataSource(DataSource ds);

		//Create Record
		public void create(String name, Integer age);

		//Get One Record from Id
		public Student getStudent(Integer id);

		//Get All Records
		public List<Student> listStudents();

		//Delete A Record from Id
		public void delete(Integer id)();

		//Update a Record from Id
		public void update(Integer id, Integer age)();
	}

	import javax.sql.DataSource;
	import org.springframework.jdbc.core.JdbcTemplate;

	//This class is the JDBCTemplate class, which is used to implement DAO interface above

	publc class StudentDAOImpl implements StudentDAO{
		private DataSource dataSource; //we define this in beans.xml
		private JdbcTemplate jdbcTemplateObject;

		public void setDataSource(DataSource dataSource){
			this.dataSource = dataSource;
			this.jdbcTemplateObject = new JdbcTemplate(dataSource);
		}
		public void create(String name, Integer age){
			String SQL = "insert into Student(name,age) values (?,?)";
			jdbcTemplateObject.update(SQL, name, age);
			return;
		}
		public Student getStudent(Integer id){
			//Same as update example above
		}
		public List<Student> listStudents(){
			//Same as query example above
		}
		public void delete(Integer id)(){
			//Same as delete example above;
		}
		public void update(Integer id, Integer age)(){
			//Same as udpat example above;
		}
	}

	public class Test{
		publc static void main(String[] args){
			ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

			StudentDAOImpl studentDaoImpl = (StudentDAOImpl) context.getBeans("studentDAOImpl");
			//Note we don't need to get dataSource bean. Spring does that automatically

			studentDaoImpl.create("Tim", 1);
			//You can now use DAO operation
		}
	}

There are other JDBC framework prepared by Spring, such as `NamedParameterJdbcTemplate` and `SimpleJdbcTemplate` classes.

##Stored Procedure

`SimpleJdbcCall` class is used to call a *stored procedure* with `IN` and `OUT` parameters.

Example:

	:::java
	import javax.sql.DataSource;
	import org.springframework.jdbc.core.JdbcTemplate;
	import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
	import org.springframework.jdbc.core.namedparam.SqlParameterSource;
	import org.springframework.jdbc.core.simple.SimpleJdbcCall;

	//bean.xml, Student.java, StudentMapper.java and StudentDAO.java are the same as example above

	public class StudentDAOImpl implements StudentDAO{
		private DataSource dataSource;
		private SimpleJdbcCall jdbcCall;

		public void setDataSource(DataSource dataSource){
			this.dataSource = dataSource;
			this.jdbcCall = new SimpleJdbcCall(dataSource).withProcedureName("Procedure_Name");
			//This is the way to call the stored procedure
		}
		public void create(String name, Integer age){
			JdbcTemplate jdbcTemplateObject = new JdbcTemplate(dataSource);
			String SQL = "insert into Student (name,age) values (?,?)";
			//Since we don't have a JdbcTemplate attribute now, we need to create new one here
			jdbcTemplateObject.update(SQL, name, age);
		}
		public Student getStudent(Integer id){
			SqlParameterSource in = new MapSqlParameterSource().addValue("in_id", id);
			//Add value parameter for stored procedure
			Map<String, Object> out = jdbcCall.execute(in);

			Student student = new Student();
			student.setId(id);
			student.setName((String) out.get("out_name")); //Add stored procedure value to setter
			student.setAge((Integer) out.get("out_age"));
			return Student;
		}
		//listStudents() is the same as example above
		//Test class is the same as example above, and you should get same result
	}





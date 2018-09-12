.. title: Reading Notes for Spring 3 Core Components Tutorial Part VII (Chapter 21)
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Java
.. tags: Java
.. slug: reading-spring-3-21
.. authors: Pengyin Shan
.. description: Reading Notes for Spring 3 Core Components Tutorial Part VII (Chapter 21)

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014.

This is a reading note from Spring Framework 3.1 Tutorial pdf, created by <a href="http://www.tutorialspoint.com/spring">**tutorialspoint**</a>. This pdf contains information for Spring 3 Core Basics, which is very useful for understanding defination and practive in Spring programming.

This note includes Chapter 21 in tutorial.

#Spring Transaction Management

A **Database Transaction** is a sequence of actions that are treated as a single unit of work. *You either run all of actions once, or you don't run any of them*.

##Four Properties About Database**

There are four key property that a transaction must have, called **ACID**:

- `Atomicity`: A transaction must be treated as *a single unit of operation*, which means either the entire sequence of operations is *successful* or *unsuccessful*.

- `Consistency`: This represents the consistency of the referential integrity of the database, unique primary keys in tables etc. *All the rules must be applied for transactions, so that all data is complete.* For example, all B-Tree index or double-linked list must be right after a transaction.

- `Isolation`: There may be *many* transactions processing with the *same* data set at the *same* time, each transaction should be *isolated* from others to prevent the data corruption.

- `Durability`: Once a transaction has completed, the results of this transaction has to be *permanent* and *cannot be earased from the database* due to system failure.

##A Typical Sequence of Transaction

Begin the transaction using begining transaction command

Perfom `deleted`, `update` or `insert` operations using SQL queries.

If all the operation are successful then perfom `commit` otherwise `rollback` all the operations.

Spring transaction support aims to provide an alternative to `EJB` transactions by adding transaction capabilities to `POJO`s.

Spring supports both `programmatic` and `declarative` transaction management.

Spring transaction management can be implemented *without* a need of application server.

##Local vs Global Transactions

`Local Transaction` is specific to a *single* transaction resource such as a JDBC connection, whereas `Global Transactions` can span *multiple* transaction resources like transaction in a Distributed System.

`Local Transaction` is useful in a centralized computing environment where application components and resources are located at *a single site* and transaction management only involves a *local data manager* runing on a *single machine*. Local transactions are easier to implement.

`Global Transaction` management is required in a *distributed* computing environment where all the resources are distributed across *multiple systems*. In such a case transaction management needs to be done both *at local and global events*. A distributed or a global transaction is executed across multiple systems, and its execution requires *coordination* between the global transaction management system and all the local data managers of all the involved systems.

##Programmatic vs Declarative

Spring supports two type of transaction management:

- `Programmatic Transaction Management`: You manage the transaction with the help of programming. This ways has most *flexibility*, but it is *difficult to maintain*.

- `Declarative Transaction Management`: You *seperate* transaction management from the *business code*. You only use `xml` based configuration to manage transactions. This is more preferable. Spring supports declarative transaction management through the Spring AOP framework.

##Spring Transaction Abstractions

The key to Spring transaction is: `org.springframework.transaction.PlatformTransactionManager` interface.
images/posts/PlatformTransactionManager.png 

`TransactionDefinition` is the core interface of the transaction support in Spring.
images/posts/TransactionDefinition.png 

`TransactionStatus` interface is used to control transaction execution and query transaction status.
images/posts/TransactionStatus.png 

##Programmatic Transaction Management

The generate process of `Programmatic Transaction Management` is:

- Use an instance of `TransactionDefinition` with appropriate transaction attributes to start a new transaction.

- Start your transaction by calling `getTransaction()` method, which returns an instance of `TransactionStatus`.

- `TransactionStatus` objects helps in tracking the current status of transaction.

- If everything goes fine, you can use `commit()` method of `PlatformTransactionManager` to commit the transaction, otherwise use `rollback()` to rollback the complate operation.

Example:

XML:

	:::xml
	<!--Initialization for data source -->
	<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource"/>
		<property name="driverClassName" value="com.mysql.jdbc.Driver"/>
		<property name="url" value="jdbc:mysql://localhost:3306/TEST"/>
		<property name="username" value="root"/>
		<property name="password" value="password"/>
	</bean>

	<!--Initialization for TransactionManager -->
	<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManger">
		<property name="dataSource" ref="dataSource"/>
	</bean>

	<!--Defination of studentDaoImpl bean-->
	<bean id="studentDaoImpl" class="com.sample.StudentDaoImpl">
		<property name="dataSource" ref="dataSource"/>
		<property name="transactionManager" ref="transactionManager"/>
	</bean>

JAVA:

	:::java
	//Assume we have a StudentDao interface, a student class with getters and setters, and a studentMapper class
	//Assume we have a Student table and a Marks table

	public class StudentDaoImpl implements StudentDao{
		private DataSouce dataSource;
		private JdbcTemplate jdbcTemplateObject;
		private PlatformTransactionManager transactionManager;

		public void setDataSource(DataSource dataSource){
			this.dataSource = dataSource;
			this.jdbcTemplateObject = new JdbcTemplate(dataSource);
		}
		//Differnet from examples before, we need to set up TransactionManager
		public void setTransactionManager(PlatformTransacionManager tansactionManager){
			this.transactionManager = transactionManager;
		}
		public void create(String name, Integer age){
			//Start Transaction
			TransactionDefination def = new DefaultTransactionDefinition();
			TransactionStatus status = transactionManager.getTransaction(def);

			try{
				String SQL1 = "insert into Student (name,age) values (?,?)";
				jdbcTemplateObject.update(SQL1, name, age);

				//Get latest student id from student table
				String SQL2 = "select max(id) from Student";
				int sid = jdbcTemplateObject.queryForInt(SQL2);

				String SQL3 = "insert into Marks(sid, marks, year) " + "values (?,?,?)";
				jdbcTemplateObject.udpate(SQL3, sid, marks, year);

				transactionManager.commit(status); //Make sure you commit after sql operation!
			}
			catch(Exception e){
				System.out.println(e);
			}
		}

		public List<Student> listStudents(){
			String SQL = "select * from Student, Marks where Student.id = Marks.sid";
			List<Student> students = jdbcTemplateObject.query(SQL, new StudentMapper());
			return students;
		}
	}

	public static void main(String[] args){
		ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

		StudentDaoImpl studetnDaoImpl = (StudentDaoImpl)context.getBean("studentDapImpl");
		//Now you can dp studentDaoImpl.create(), etc.
	}

##Declarative Transaction Management

If you use `Declarative Transaction Management`, you only use `Annotations` or `XML` based configuration to manage the transactions. Steps are:

- Add `<tx:advice />` tag in `XML` file, which creates a transaction-handling advice and ame time we define a *pointcut* that matches all methods we wish to make transactional and reference the transactional advice.

- If a method name has been included in the transactional configuration then created advice will begin the transaction *before* calling the method.

- Target method should be in a `Try/Catch` block.

- If the method finishes normally, the AOP advice `commits` the transaction successfully otherwise it performs a `rollback`.

Example:

XML:

	:::xml
	<!--Data Source Setup is the same as example above-->
	<tx:advice id="txAdivce" transaction-manager="transactionManager">
		<tx:attribute>
		<tx:method name="create"/> <!--Transaction will begin before calling this method-->
		</tx:attribute>
	</tx:advice>

	<aop:config>
		<aop:pointcut id="createOperation" express="execution(*com.sample.StudentDaoImpl.create(...))"/>
		<aop:advisor advice-ref="txAdvice" point-cut="createOperation"/>
	</aop:config>
	<!--TransactionManager and StudentDaoImpl are the same as example above-->

JAVA:

	:::java
	//Assume we have a StudentDao interface, a student class with getters and setters, and a studentMapper class
	//Assume we have a Student table and a Marks table

	public class StudentDaoImpl implements StudentDao{
		private JdbcTemplate jdbcTemplateObject;

		public void setDataSource(DataSource dataSource){
			this.dataSource = dataSource;
			//No need to declare dataSource in java class
		}
		//No need to set up TransactionManager in java class
		public void create(String name, Integer age){
			//No need to set up Transaction
			try{
				String SQL1 = "insert into Student (name,age) values (?,?)";
				jdbcTemplateObject.update(SQL1, name, age);

				//Get latest student id from student table
				String SQL2 = "select max(id) from Student";
				int sid = jdbcTemplateObject.queryForInt(SQL2);

				String SQL3 = "insert into Marks(sid, marks, year) " + "values (?,?,?)";
				jdbcTemplateObject.udpate(SQL3, sid, marks, year);

				//No need to commit after sql operation!
			}
			catch(Exception e){
				System.out.println(e);
			}
		}

		public List<Student> listStudents(){
			String SQL = "select * from Student, Marks where Student.id = Marks.sid";
			List<Student> students = jdbcTemplateObject.query(SQL, new StudentMapper());
			return students;
		}
	}

	public static void main(String[] args){
		ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

		StudentDaoImpl studetnDaoImpl = (StudentDaoImpl)context.getBean("studentDapImpl");
		//Now you can dp studentDaoImpl.create(), etc.
	}
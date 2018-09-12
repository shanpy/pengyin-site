.. title: JUnit Basics
.. modified: 2015-07-27
.. date: 2015-07-24
.. category: Java
.. tags: JUnit, Software Testing, Java
.. slug: junit-basics
.. authors: Pengyin Shan
.. description: I'm planing to add JUnit and Cucumber to one of my work project. Before digging into Cucumber directly, I want to do a brief overview about JUnit.

##Reference

- <a href="http://www.tutorialspoint.com//junit/index.htm">JUnit Tutorial from Tutorialspoint.com</a>

##Overview

A `Unit Test Case` is a part of code which ensures that the another part of code (method) works as expected. To achieve those desired results quickly, test framework is required.

JUnit is perfect unit test framework for java programming language.

##Test Framework

###Features

JUnit test framework provides following important features:

- `Fixtures`

- `Test suites`

- `Test runners`

- `JUnit classes`

####Fixtures

`Fixtures` is a fixed state of a set of **objects** used as a baseline for running tests.

The purpose of a test fixture is to ensure that there is a well known and **fixed environment** in which tests are run so that results are repeatable. It includes:

- `setUp()` method which runs before every test invocation.

- `tearDown()` method which runs after every test method.

Example Code from Tutorialspoint.com:

    :::java
    import junit.framework.*;
    public class JavaTest extends TestCase {
       protected int value1, value2;
       // setUp() method: assigning the values
       protected void setUp(){
          value1=3;
          value2=3;
       }
       // test method to add two values
       public void testAdd(){
          double result= value1 + value2;
          assertTrue(result == 6);
       }
       //No tearDown() in this example
    }

####Test Suite

`Test suite` means **bundle** a few unit test cases and run it together.

In JUnit, both `@RunWith` and `@Suite` annotation are used to run the suite test.

Here is an example which uses TestJunit1 & TestJunit2 test classes from Tutorialspoint.com:

    :::java
    import org.junit.runner.RunWith;
    import org.junit.runners.Suite;
    //JUnit Suite Test with @Runwith and @Suite annotation
    @RunWith(Suite.class)
    @Suite.SuiteClasses({
       TestJunit1.class ,TestJunit2.class
    })
    public class JunitTestSuite {
    }

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    public class TestJunit1 {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       //@Test Annotation
       @Test
       public void testPrintMessage() {
          System.out.println("Inside testPrintMessage()");
          assertEquals(message, messageUtil.printMessage());
       }
    }

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    public class TestJunit2 {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       @Test
       public void testSalutationMessage() {
          System.out.println("Inside testSalutationMessage()");
          message = "Hi!" + "Robert";
          assertEquals(message,messageUtil.salutationMessage());
       }
    }

####Test Runner

`Test runner` is used for **executing** the test cases.

Here is an example which assumes TestJunit test class already exists, from Tutorialspoint.com:

    :::java
    import org.junit.runner.JUnitCore;
    import org.junit.runner.Result;
    import org.junit.runner.notification.Failure;
    public class TestRunner {
       public static void main(String[] args) {
          //Note this line of using exiting TestJunit.class
          Result result = JUnitCore.runClasses(TestJunit.class);
          for (Failure failure : result.getFailures()) {
             System.out.println(failure.toString());
          }
          System.out.println(result.wasSuccessful());
       }
    }

####JUnit Classes

JUnit classes are important classes which is used in writing and testing JUnits.

Some of the important classes are:

- `Assert` which contain a set of assert methods.

- `TestCase` which contain a test case defines the fixture to run multiple tests.

- `TestResult` which contain methods to collect the results of executing a test case.

###JUnit Basic Usage

####1. Create a Message Class

Example code from Tutorialspoint.com:

    :::java
    /*
    * This class prints the given message on console.
    */
    public class MessageUtil {
       private String message;
       //Constructor
       //@param message to be printed
       public MessageUtil(String message){
          this.message = message;
       }
       // prints the message
       public String printMessage(){
          System.out.println(message);
          return message;
       }
    }

####2. Create a Test Case Class

Example code from Tutorialspoint.com

    :::java
    import org.junit.Test;
    import static org.junit.Assert.assertEquals;
    public class TestJunit {
       String message = "Hello World";
       //Use the message class above
       MessageUtil messageUtil = new MessageUtil(message);
       @Test
       public void testPrintMessage() {
          //Use assestion for printing out message
          assertEquals(message,messageUtil.printMessage());
       }
    }

####3. Create a Test Runner Class

Example code from Tutorialspoint.com

    :::java
    import org.junit.runner.JUnitCore;
    import org.junit.runner.Result;
    import org.junit.runner.notification.Failure;
    public class TestRunner {
       public static void main(String[] args) {
          //User the test class created above
          Result result = JUnitCore.runClasses(TestJunit.class);
          //Print failure and successful messages
          for (Failure failure : result.getFailures()) {
             System.out.println(failure.toString());
          }
          System.out.println(result.wasSuccessful());
       }
    }

###Writing Test with POJOs

To write a test for a POJO class, we need following:

- A **POJO** class which defines a object in your business login

- A **Business Logic** class which includes: a. methods for testing, using the POJO class mentioned above b. test class using business login

- A **Test Runner** class which is similar as what we have above for testing

Example code from Tutorialspoint.com:

POJO class example:

    :::java
    public class EmployeeDetails {
       private String name;
       private double monthlySalary;
       private int age;
       /**
       - @return the name
       */
       public String getName() {
          return name;
       }
       /**
       - @param name the name to set
       */
       public void setName(String name) {
          this.name = name;
       }
       //Following parts are skipped
    }

Business Logic class example:

First, Set up a method which needs to be tested:

    :::java
    public class EmpBusinessLogic {
       // Calculate the yearly salary of employee
       public double calculateYearlySalary(EmployeeDetails employeeDetails){
          double yearlySalary=0;
          yearlySalary = employeeDetails.getMonthlySalary() * 12;
          return yearlySalary;
       }
    }

Then, created a test business logic class with **assestion** and **@Test** annotation:

    :::java
    import org.junit.Test;
    import static org.junit.Assert.assertEquals;
    public class TestEmployeeDetails {
       EmpBusinessLogic empBusinessLogic =new EmpBusinessLogic();
       EmployeeDetails employee = new EmployeeDetails();
       // test to check yearly salary
       @Test
       public void testCalculateYearlySalary() {
          employee.setName("Rajeev");
          employee.setAge(25);
          employee.setMonthlySalary(8000);
          double salary= empBusinessLogic.calculateYearlySalary(employee);
          assertEquals(96000, salary, 0.0);
       }
    }

Test Runner class example:

    :::java
    import org.junit.runner.JUnitCore;
    import org.junit.runner.Result;
    import org.junit.runner.notification.Failure;
    public class TestRunner {
       public static void main(String[] args) {
          Result result = JUnitCore.runClasses(TestEmployeeDetails.class);
          for (Failure failure : result.getFailures()) {
             System.out.println(failure.toString());
          }
          System.out.println(result.wasSuccessful());
       }
    }

###Assertion and Annotation

####Assertion

This class provides a set of assertion methods useful for writing tests. *Only failed assertions are recorded.*

#####List of Assertion Methods

- `assertEquals`: Check that two primitives/Objectes are equal

- `assertTrue` or `assertFalse`: Check that a condition is true/false

- **assertNull** or **assertNotNull**: Check that a condition is null/not null

- **assertSame** or **assertNotSame**: Check that if two object references *point* to the same/not same object

- **assertArrayEquals**: Check whether two arrays are equal to each other

####Annotation

The annotation in JUnit gives us information about test methods, include:

- which methods are going to run before & after test methods,

- which methods run before & after all the methods

- which methods or class will be ignore during execution.

#####List of Annotations

- `@Test`: The Test annotation tells JUnit that the **public void method** to which it is attached can be run as a test case.

- `@Before`: Several tests need similar objects created before they can run. Annotating a public void method with @Before causes that method to be **run before each Test method**.

- `@After`: If you allocate external resources in a Before method *you need to release them after the test runs*. Annotating a public void method with @After causes that method to be run after the Test method.

- `@BeforeClass`: Annotating a public static void method with @BeforeClass causes it to be **run once** before any of the test methods in the class.

- `@AfterClass`: This will perform the method after all tests have finished. This can be used to perform **clean-up activities**.

- `@Ignore`: The Ignore annotation is used to ignore the test and that **test will not be executed**.

###Suite Test

Test suites means bundle a few unit test cases and run it together. In JUnit, both `@RunWith` and `@Suite` annotation are used to run the suite test.

####Step 1: Create a Message Class

Example code from Tutorialspoint.com:

    :::java
    /*
    * This class prints the given message on console.
    */
    public class MessageUtil {
       private String message;
       //Constructor
       //@param message to be printed
       public MessageUtil(String message){
          this.message = message;
       }
       // prints the message
       public String printMessage(){
          System.out.println(message);
          return message;
       }
       // add "Hi!" to the message
       public String salutationMessage(){
          message = "Hi!" + message;
          System.out.println(message);
          return message;
       }
    }

####Step 2: Create Business Login Class with Business Login Test Class

Business Logic class with Methods for testing:

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    public class TestJunit1 {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       @Test
       public void testPrintMessage() {
          System.out.println("Inside testPrintMessage()");
          assertEquals(message, messageUtil.printMessage());
       }
    }

Business Logic Test Class with Assertions:

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    public class TestJunit2 {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       @Test
       public void testSalutationMessage() {
          System.out.println("Inside testSalutationMessage()");
          message = "Hi!" + "Robert";
          assertEquals(message,messageUtil.salutationMessage());
       }
    }

####Step3: Create Test Suite Class using @RunWith and @Suite annotation

Example code from Tutorialspoint.com:

    :::java
    import org.junit.runner.RunWith;
    import org.junit.runners.Suite;
    //@RunWith takes Suite.class parameter
    @RunWith(Suite.class)
    @Suite.SuiteClasses({
       //A list of unit tests included in this test suite
       TestJunit1.class,
       TestJunit2.class
    })
    public class JunitTestSuite {
    }

####Create Test Runner Classes

Same code as examples above

###Ignore Test

Sometimes it happens that our code is not ready and test case written to test that method/code will fail if run. The `@Ignore` annotation helps in this regards.

A test method annotated with @Ignore **will not be executed**.

If a test class is annotated with @Ignore then none of its test methods will be executed.

####Step 1: Create a Message Class

Same as example above.

####Step 2: Create Business Login Class with Business Login Test Class

Same as example above.

####Step 3: Create Test Runner Class with @Ignore Annotation

Example code from Tutorialspoint.com:

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    //Note @Ignore is the annotation for test runner class
    @Ignore
    public class TestJunit {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       @Test
       public void testPrintMessage() {
          System.out.println("Inside testPrintMessage()");
          message = "Robert";
          assertEquals(message,messageUtil.printMessage());
       }
       @Test
       public void testSalutationMessage() {
          System.out.println("Inside testSalutationMessage()");
          message = "Hi!" + "Robert";
          assertEquals(message,messageUtil.salutationMessage());
       }
    }

If you run the code above, you will always pass all test because none of test with @Test annotation above is excuted.

###Time Test

If a test case takes more time than specified number of milliseconds then JUnit will automatically mark it as failed.

The `timeout` parameter is used along with @Test annotation.


####Step 1: Create a Message Class

Same as example above.

####Step 2: Create Test Class with Timeout Setting

Example code from Tutorialspoint.com:

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    public class TestJunit {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       //Add timeout parameter for @Test annotation
       @Test(timeout=1000)
       public void testPrintMessage() {
          System.out.println("Inside testPrintMessage()");
          messageUtil.printMessage();
       }
       @Test
       public void testSalutationMessage() {
          System.out.println("Inside testSalutationMessage()");
          message = "Hi!" + "Robert";
          assertEquals(message,messageUtil.salutationMessage());
       }
    }

####Step 3: Create Test Runner Class

Same regular Test Runner class as examples above

###Exceptions Test

You can test the code *whether code throws desired exception or not*.

The **expected** parameter is used along with @Test annotation.

####Step 1: Create a Message Class

Same as example above.

####Step 2: Create Test Class with Exception Setting

Example code from Tutorialspoint.com:

    :::java
    import org.junit.Test;
    import org.junit.Ignore;
    import static org.junit.Assert.assertEquals;
    public class TestJunit {
       String message = "Robert";
       MessageUtil messageUtil = new MessageUtil(message);
       //Put specific exception class as parameter
       @Test(expected = ArithmeticException.class)
       public void testPrintMessage() {
          System.out.println("Inside testPrintMessage()");
          messageUtil.printMessage();
       }
       @Test
       public void testSalutationMessage() {
          System.out.println("Inside testSalutationMessage()");
          message = "Hi!" + "Robert";
          assertEquals(message,messageUtil.salutationMessage());
       }
    }

####Step 3: Create Test Runner Class

Same regular Test Runner class as examples above

###Parameterized Test

Parameterized tests allow developer to *run the same test over and over again using different values*.

Five steps to follow for parameterized test:

1. Annotate test class with `@RunWith(Parameterized.class)``

2. Create a public static method annotated with `@Parameters` that returns a **Collection of Objects** (as Array) as test data set.

3. Create a public constructor that takes in what is equivalent to one "row" of test data.

4. Create an instance variable for each "column" of test data.

5. Create your tests case(s) using the instance variables as the source of the test data.

The test case will be invoked once per each row of data.

####Step 1: Create a Business Logic class with Methods for Testing

Exmaple code from Tutorialspoint.com:

    :::java
    public class PrimeNumberChecker {
       public Boolean validate(final Integer primeNumber) {
          for (int i = 2; i < (primeNumber / 2); i++) {
             if (primeNumber % i == 0) {
                return false;
             }
          }
          return true;
       }
    }

####Step 2: Create a Business Logic Parameterized Test Class

Exmaple code from Tutorialspoint.com:

    :::java
    import java.util.Arrays;
    import java.util.Collection;
    import org.junit.Test;
    import org.junit.Before;
    import org.junit.runners.Parameterized;
    import org.junit.runners.Parameterized.Parameters;
    import org.junit.runner.RunWith;
    import static org.junit.Assert.assertEquals;
    //Parameterized.class works as parameter of @RunWith
    @RunWith(Parameterized.class)
    public class PrimeNumberCheckerTest {
       private Integer inputNumber;
       private Boolean expectedResult;
       private PrimeNumberChecker primeNumberChecker;
       @Before
       public void initialize() {
          primeNumberChecker = new PrimeNumberChecker();
       }
       // Each parameter should be placed as an argument here
       // Every time runner triggers, it will pass the arguments
       // from parameters we defined in primeNumbers() method
       public PrimeNumberCheckerTest(Integer inputNumber,
          Boolean expectedResult) {
          this.inputNumber = inputNumber;
          this.expectedResult = expectedResult;
       }
       //Use @Parameterized.Parameters for defining collection of test data
       @Parameterized.Parameters
       public static Collection primeNumbers() {
          //Note it returns an Array as collection
          return Arrays.asList(new Object[][] {
             { 2, true },
             { 6, false },
             { 19, true },
             { 22, false },
             { 23, true }
          });
       }
       // This test will run 4 times since we have 5 parameters defined
       @Test
       public void testPrimeNumberChecker() {
          System.out.println("Parameterized Number is : " + inputNumber);
          assertEquals(expectedResult, primeNumberChecker.validate (inputNumber));
       }
    }

####Step 3: Create Test Runner Class

Same regular Test Runner class as examples above
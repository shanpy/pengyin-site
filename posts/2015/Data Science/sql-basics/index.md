.. title: SQL Basics
.. date: 2015-06-21
.. modified: 2015-07-30
.. category: Data Science
.. tags: Database, SQL
.. slug: sql-basics
.. authors: Pengyin Shan
.. description: This post includes useful SQL basic knowledge I read online or learned in work. This post will be updated continually.

###Reference List

- <a href="https://en.wikibooks.org/wiki/Oracle_Programming/SQL_Cheatsheet">Oracle Programming/SQL Cheatsheet</a>

- <a href="http://www.tutorialspoint.com/sql/index.htm">SQL Tutorial on TutorialsPoint</a>

###Basic SQL Commands

#####DDL - Data Definition Language

- `CREATE`: Creates a new table, a view of a table, or other object in database

- `ALTER`: Modifies an existing database object, such as a table.

- `DROP`: Deletes an entire table, a view of a table or other object in the database.

#####DML - Data Manipulation Language

- `INSERT`: Creates a record

- `UPDATE`: Modifies records

- `DELETE`: Deletes records

#####DCL - Data Control Language

- `GRANT`: Gives a privilege to user

- `REVOKE`: Takes back privileges granted from user

#####DQL - Data Query Language

- `SELECT`: Retrieves certain records from one or more tables

###Data Integrity

The following categories of the data integrity exist with each RDBMS:

- `Entity Integrity`: There are **no duplicate rows** in a table.

- `Domain Integrity`: Enforces valid entries for a given column by **restricting the type, the format, or the range of values**.

- `Referential Integrity`: Rows **cannot be deleted**, which are **used by other records**.

- `User-Defined Integrity`: Enforces some specific business rules that do not fall into entity, domain or referential integrity.

###Database Normalization

Database normalization is the process of efficiently organizing data in a database.

There are two reasons of the normalization process:

- Eliminating redundant data, for example, storing the same data in more than one tables.

- Ensuring data dependencies make sense.

Normalization guidelines are divided into normal forms; The aim of normal forms is to organize the database structure so that it complies with the rules of `first normal form`, then `second normal form`, and finally `third normal form`.

#####First Normal Form (1NF)

First normal form (`1NF`) sets the very basic rules for an organized database:

- Define the data items required, because they become the columns in a table. Place related data items in a table.

- Ensure that there are *no repeating groups of data*.

- Ensure that there is a *primary key*.

######First Rule of 1NF

You must define the data items.

This means looking at the data to be stored, organizing the data into columns, defining what type of data each column contains, and finally putting related columns into their own table.

######Second Rule of 1NF

Ensure that there are no repeating groups of data: you may need to `JOIN` tables.

######Third Rule of 1NF

Create primary key: `CREATE TABLE CUSTOMERS(PRIMARY KEY (ID));`

#####Second Normal Form (2NF)

Second normal form states that it should meet all the rules for 1NF and there must be no partial dependences of any of the columns on the primary key.

Example:

Consider a customer-order relation and you want to store customer ID, customer name, order ID and order detail, and date of purchase:

    :::sql
    CREATE TABLE CUSTOMERS(
        CUST_ID INT NOT NULL,
        CUST_NAME VARCHAR (20) NOT NULL,
        ORDER_ID INT NOT NULL,
        ORDER_DETAIL VARCHAR (20) NOT NULL,
        SALE_DATE DATETIME,
        PRIMARY KEY (CUST_ID, ORDER_ID) );

This table is in first normal form, in that it obeys all the rules of first normal form.

In this table, the primary key consists of `CUST_ID` and `ORDER_ID`. Combined, they are unique assuming same customer would hardly order same thing.

However, the table is not in second normal form because there are partial dependencies of primary keys and columns:

- `CUST_NAME` is dependent on `CUST_ID`.

- Order detail and purchase date are dependent on `ORDER_ID`, but they are not dependent on `CUST_ID`, because there's no link between a CUST_ID and an ORDER_DETAIL or their SALE_DATE.

- No real link between a customer's name and what he purchased.

>To make this table comply with second normal form, you need to separate the columns into three tables.

#####Third Normal Form (3NF)

A table is in third normal form when the following conditions are met:

- It is in second normal form.

- All nonprimary fields are dependent on the primary key.

The dependency of nonprimary fields is between the data.

Example:

    :::sql
    CREATE TABLE CUSTOMERS(
        CUST_ID INT NOT NULL,
        CUST_NAME VARCHAR (20) NOT NULL,
        DOB DATE,
        STREET VARCHAR(200),
        CITY VARCHAR(100),
        STATE VARCHAR(100),
        ZIP VARCHAR(12),
        EMAIL_ID VARCHAR(256),
        PRIMARY KEY (CUST_ID) );

The dependency between `zip code` and `address` is called a **transitive dependency**.

To comply with third normal form, all you need to do is move the Street, City, and State fields into their own table.

The advantages of removing transitive dependencies:
- The amount of data duplication is reduced and therefore your database becomes smaller.

- Data integrity.

>When duplicated data changes, there's a big risk of updating only some of the data, especially if it's spread out in a number of different places in the database.

###SELECT

`SELECT INTO` can only retrieve **one** line of item. Empty line will get *NO_DATA_FOUND* error. Mutiple lines will get *TOO_MANY_ROWS* error.

###LIKE

User `LIKE` to compare a value to similar values using wildcard operators.

There are two wildcards used in conjunction with the LIKE operator:

- The percent sign `%`

- The underscore `_`


Example:

`WHERE SALARY LIKE '2_%_%'`: Finds any values that start with 2 and are at least 3 characters in length

###TOP

The SQL `TOP` clause is used to fetch a TOP N number or X percent records from a table.

Note: All the databases do not support TOP clause. For example MySQL supports `LIMIT` clause to fetch limited number of records and Oracle uses `ROWNUM` to fetch limited number of records.

Syntax:

    :::sql
    SELECT TOP number|percent column_name(s)
    FROM table_name
    WHERE [condition]

MySQL:

    :::sql
    SELECT columns
    FROM table
    LIMIT [condition]

Oracle Server:

    :::sql
    SELECT columns
    FROM table
    WHERE [ROWNUM condition]

###ORDER BY

The SQL `ORDER BY` clause is used to sort the data in ascending or descending order, based on one or more columns.

Some database sorts query results in ascending order by default.

You can use more than one column in the `ORDER BY` clause. Make sure whatever column you are using to sort, that column should be in column-list.

Syntax:

    :::sql
    SELECT column-list
    FROM table_name
    [WHERE condition]
    [ORDER BY column1, column2, .. columnN] [ASC | DESC];

###GROUP BY

The SQL `GROUP BY` clause is used in collaboration with the `SELECT` statement to arrange identical data into groups.

The `GROUP BY` clause follows the `WHERE` clause in a `SELECT` statement and must precedes the `ORDER BY` clause.

Syntax:

    :::sql
    SELECT column1, column2
    FROM table_name
    WHERE [ conditions ]
    GROUP BY column1, column2
    ORDER BY column1, column2

###DISTINCT

The SQL `DISTINCT` keyword is used in conjunction with `SELECT` statement to eliminate all the duplicate records and fetching only unique records.

Syntax:

    :::sql
    SELECT DISTINCT column1, column2,.....columnN
    FROM table_name
    WHERE [condition]

###SQL Constraints

Constraints could be column level or table level.

Commonly used constraints:

- `NOT NULL` Constraint: Ensures that a column cannot have `NULL` value.

- `DEFAULT` Constraint: Provides a default value for a column when none is specified.

- `UNIQUE` Constraint: Ensures that all values in a column are different.

- `PRIMARY` Key: Uniquely identified each rows/records in a database table.

- `FOREIGN` Key: Uniquely identified a rows/records in any another database table.

- `CHECK` Constraint: The `CHECK` constraint ensures that all values in a column *satisfy certain conditions*.

- `INDEX`: Use to create and retrieve data from the database very quickly.

#####NOT NULL

A NULL is not the same as no data, rather, it represents unknown data.

Example: `CREATE TABLE CUSTOMERS( ID  INT  NOT NULL);`

#####DEFAULT

In case `INSERT INTO` or `INSERT` statement does not provide a value for such column, then the column will have a default value.

Example:

- `CREATE TABLE CUSTOMERS(ID  INT  NOT NULL)`

- `ALTER COLUMN SALARY DROP DEFAULT;`

#####PRIMARY KEY

A primary key is a field in a table which uniquely identifies each row/record in a database table.

Primary keys must contain unique values. A primary key column cannot have `NULL` values.

A table can have only one primary key. When multiple fields are used as a primary key, they are called a `composite key`.

> NOTE: If you use the `ALTER TABLE` statement to add a primary key, the primary key column(s) must already have been declared to not contain `NULL` values (when the table was first created).

Example: `CREATE TABLE CUSTOMERS( PRIMARY KEY (ID, NAME) );`

#####FOREIGN KEY

A `foreign key` is a key used to link two tables together. This is sometimes called a `referencing key`.

Foreign Key is a column or a combination of columns whose values match a Primary Key in a different table.

The relationship between 2 tables matches the Primary Key in one of the tables with a Foreign Key in the second table.

Example:

`CREATE TABLE ORDERS (  CUSTOMER_ID INT references CUSTOMERS(ID) );`

    :::sql
    ALTER TABLE ORDERS
    DROP FOREIGN KEY;

If ORDERS table has already been created, and the foreign key has not yet been set, use the syntax for specifying a foreign key by altering a table:

    :::sql
    ALTER TABLE ORDERS
    ADD FOREIGN KEY (Customer_ID) REFERENCES CUSTOMERS (ID);

#####CHECK

The `CHECK` Constraint enables a condition to check the value being entered into a record. If the condition evaluates to false, the record violates the constraint and isn't entered into the table.

Example:

`CREATE TABLE CUSTOMERS(AGE INT NOT NULL CHECK (AGE >= 18));`

    :::sql
    ALTER TABLE CUSTOMERS
        MODIFY AGE INT NOT NULL CHECK (AGE >= 18 );
    ALTER TABLE CUSTOMERS
        ADD CONSTRAINT myCheckConstraint CHECK(AGE >= 18);
    ALTER TABLE CUSTOMERS
        DROP CONSTRAINT myCheckConstraint;

#####INDEX

The `INDEX` is used to create and retrieve data from the database very quickly.

Index can be created by using single or group of columns in a table.

When index is created, it is assigned a `ROWID` for each row before it sorts out the data.

Example:

    :::sql
    CREATE INDEX index_name
        ON table_name ( column1, column2.....);
    ALTER TABLE CUSTOMERS
        DROP INDEX idx_age;

###JOIN

JOIN is performed in the WHERE clause. Several operators can be used to join tables, such as =, <, >, <>, <=, >=, !=, BETWEEN, LIKE, and NOT;

There are different types of joins available in SQL:

- `INNER JOIN`: returns rows when there is a match in **both tables**.

- `LEFT JOIN`: returns all rows from the **left table**, even if there are no matches in the right table.

- `RIGHT JOIN`: returns all rows from the **right table**, even if there are no matches in the left table.

- `FULL JOIN`: returns rows when there is a match **in one of the tables**.

- `SELF JOIN`: is used to **join a table to itself** as if the table were two tables, temporarily renaming at least one table in the SQL statement.

- `CARTESIAN JOIN`: returns the **Cartesian product** of the sets of records from the two or more joined tables.

#####INNER JOIN

When the join-predicate is satisfied, column values for each matched pair of rows of A and B are combined into a result row.

Example:

    :::sql
    SQL> SELECT  ID, NAME, AMOUNT, DATE
     FROM CUSTOMERS
     INNER JOIN ORDERS
     ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID;

#####LEFT JOIN

The SQL LEFT JOIN returns all rows from the left table, even if there are no matches in the right table.

This means that if the ON clause matches 0 (zero) records in right table, the join will still return a row in the result, but with `NULL` in each column **from right table**.

This means that a left join returns all the values from the left table, plus matched values from the right table or NULL in case of no matching join predicate.

Syntax:

    :::sql
    SELECT table1.column1, table2.column2...
    FROM table1
    LEFT JOIN table2
    ON table1.common_field = table2.common_field;

RIGHT JOIN is similar.

#####FULL JOIN

The SQL FULL JOIN combines **the results of both left and right outer joins**.

The joined table will contain all records from both tables, and fill in NULLs for missing matches on either side.

#####SELF JOIN

Syntax:

    :::sql
    SELECT a.column_name, b.column_name...
    FROM table1 a, table1 b
    WHERE a.common_field = b.common_field;

#####CARTESIAN JOIN/CROSS JOIN

The `CARTESIAN JOIN` or `CROSS JOIN` returns the Cartesian product of the sets of records from the two or more joined tables.

Thus, it equates to *an inner join where the join-condition always evaluates to True* or *where the join-condition is absent* from the statement.

Syntax:

    :::sql
    SELECT table1.column1, table2.column2...
    FROM  table1, table2 [, table3 ]

###UNION

The SQL `UNION` clause/operator is used to combine the results of two or more SELECT statements **without returning any duplicate rows**.

To use UNION, each SELECT must have *the same number of columns selected, the same number of column expressions, the same data type, and have them in the same order*, but they do not have to be the same length.

Syntax:

    :::sql
    SELECT column1 [, column2 ]
        FROM table1 [, table2 ]
        [WHERE condition]
    UNION
    SELECT column1 [, column2 ]
        FROM table1 [, table2 ]
        [WHERE condition]

The `UNION ALL` operator is used to combine the results of two SELECT statements **including duplicate rows**.

There are two other clauses (i.e., operators), which are very similar to UNION clause:

- SQL `INTERSECT` Clause

- SQL `EXCEPT` Clause

#####INTERSECT

The SQL `INTERSECT` clause/operator is used to combine two SELECT statements, but returns rows only from the first SELECT statement that are identical to a row in the second SELECT statement.

This means INTERSECT returns *only common rows returned by the two SELECT statements*.

Syntax:

    :::sql
    SELECT column1 [, column2 ]
        FROM table1 [, table2 ]
        [WHERE condition]
    INTERSECT
    SELECT column1 [, column2 ]
        FROM table1 [, table2 ]
        [WHERE condition]

#####EXCEPT

The SQL `EXCEPT` clause/operator is used to combine two SELECT statements and returns rows from the first SELECT statement that are not returned by the second SELECT statement.

This means EXCEPT returns only rows, which *are not available in second SELECT statement*.

Syntax is similar to `INTERSECT`.

###NULL VALUES

SQL NULL is the term used to represent **no** value.

It is very important to understand that a NULL value is different than a zero value or a field that contains spaces.

You must use the `IS NULL` or `IS NOT NULL` operators in order to check for a NULL value.

###SQL Alias

User can rename a table or a column **temporarily** by giving another name known as `alias`.

Syntax:

	:::sql
	SELECT column1, column2....
	FROM table_name AS alias_name
	WHERE [condition];

	:::sql
	SELECT column_name AS alias_name
	FROM table_name
	WHERE [condition];

Example:

	:::sql
	SQL> SELECT C.ID, C.NAME, C.AGE, O.AMOUNT
	FROM CUSTOMERS AS C, ORDERS AS O
	WHERE C.ID = O.CUSTOMER_ID;

###SQL INDEX

`Index` is special lookup table that the database search engine can use to speed up data retrieval. i.e. an index is a **pointer to data** in a table.

An index helps **speed up** `SELECT` queries and `WHERE` clauses, but it **slows down** data input, with `UPDATE` and `INSERT` statements. Indexes can be created or dropped with no effect on the data.

#####CREATE

Creating index involves the `CREATE INDEX` statement, which allows you to name the index, to specify the table and which column or columns to index, and to indicate whether the index is in ascending or descending
order.

Indexes can also be **unique**, similar to the UNIQUE constraint, in that the index prevents duplicate entries in the column or combination of columns on which there's an index.

Syntax:

	:::sql
	CREATE INDEX index_name ON table_name;


Single-Column Indexes:

	:::sql
	CREATE INDEX index_name
	ON table_name (column_name);

#####Unique Indexes

A unique index does not allow any duplicate values to be inserted into the table.

Syntax:

	:::sql
	CREATE UNIQUE INDEX index_name on table_name(column_name);

#####Composite Indexes

Should there be only one column used, a single-column index should be the choice.

Should there be two or more columns that are frequently used in the WHERE clause as filters, the composite index would be the best choice.

	:::sql
	CREATE INDEX index_name
	on table_name (column1, column2);

#####Implicit Indexed

Implicit indexes are indexes that are automatically created by the database server when an object is created.

Indexes are automatically created for **primary key constraints and unique constraints**.

#####DROP

Syntax:

	:::sql
	DROP INDEX index_name;

#####WHEN TO AVOID INDEX

The following guidelines indicate when the use of an index should be reconsidered:

- Indexes should not be used on **small tables**.

- Tables that have frequent, large **batch update** or **insert** operations.

- Indexes should not be used on columns that contain a high number of NULL values.

- Columns that are **frequently manipulated** should not be indexed.

###ALTER TABLE

SQL `ALTER TABLE` command is used to add, delete or modify columns in an existing table.

Syntax:

	:::sql
	ALTER TABLE table_name
	DO SOMETHING

###TRUNACTE TABLE

SQL `TRUNCATE TABLE` command is used to **delete complete data** from an existing table.

Syntax:

	:::sql
	TRUNCATE TABLE table_name;

###VIEWS

View is nothing more than a SQL statement that is stored in the database with an associated name.

A view is actually a composition of a table in the form of a predefined SQL query.

A view can contain all rows of a table or select rows from a table.

A view can be created from one or many tables which depends on the written SQL query to create a view.

#####CREATING VIEW

Database views are created using the `CREATE VIEW` statement.

Views can be created from a single table, multiple tables, or another view.

	:::sql
	CREATE VIEW view_name AS
	SELECT column1, column2.....
	FROM table_name
	WHERE [condition];

	:::sql
	SQL > SELECT * FROM CUSTOMERS_VIEW;

#####WITH CHECK OPTION

The `WITH CHECK OPTION` is a `CREATE VIEW` statement option.

The purpose of the WITH CHECK OPTION is to ensure that **all UPDATE and INSERTs satisfy the condition(s) in the view definition**.

If they do not satisfy the condition(s), the UPDATE or INSERT returns an error.

Example:

	:::sql
	CREATE VIEW CUSTOMERS_VIEW AS
	SELECT name, age
	FROM CUSTOMERS
	WHERE age IS NOT NULL
	WITH CHECK OPTION;

The WITH CHECK OPTION in this case should deny the entry of any NULL values in the view's AGE column.

#####UPDATE VIEW

A VIEW can be updated in certain conditions:

- The SELECT clause may not contain the keyword DISTINCT.

- The SELECT clause may not contain summary functions.

- The SELECT clause may not contain set functions.

- The SELECT clause may not contain set operators.

- The SELECT clause may not contain an ORDER BY clause.

- The FROM clause may not contain multiple tables.

- The WHERE clause may not contain subqueries.

- The query may not contain GROUP BY or HAVING.

- Calculated columns may not be updated.

- All NOT NULL columns from the base table must be included in the view in order for the INSERT query to function.

Example:

	:::sql
	SQL > UPDATE CUSTOMERS_VIEW
	SET AGE = 35
	WHERE name='Ramesh';

This would ultimately update the base table CUSTOMERS **and** same would reflect in the view itself.

#####INSERT OR DELETE ROWS

Rows of data can be inserted/deleted from a view.

Example:

	:::sql
	SQL > DELETE FROM CUSTOMERS_VIEW
	WHERE age = 22;

This would ultimately delete a row from the base table CUSTOMERS **and** same would reflect in the view itself.

#####DROP VIEW

Syntax:

	:::sql
	DROP VIEW view_name;

###HAVING CLAUSE

HAVING clause enables you to specify conditions that filter which group results appear in the final results.

`HAVING` clause places conditions on groups created by the `GROUP BY` clause.

Syntax:

	:::sql
	SELECT
	FROM
	WHERE
	GROUP BY
	HAVING
	ORDER BY

The `HAVING` clause must follow the `GROUP BY` clause in a query and must also precede the `ORDER BY` clause if used.

Example:

	:::sql
	SELECT column1, column2
	FROM table1, table2
	WHERE [ conditions ]
	GROUP BY column1, column2
	HAVING [ conditions ]
	ORDER BY column1, column2

###TANSACTIONS

Transaction is a unit of work that is performed **against a database**.

Transactions are **units** or **sequences** of work accomplished in a logical order, whether in a manual fashion by a user or automatically by some sort of a database program.

A transaction is the propagation of one or more changes to the database.

Practically, you will club many SQL queries into a group and you will execute all of them together as a part of a transaction.

#####PROPERTIES OF TRANSACTIONS

Transactions have the following four standard properties, usually referred to by the acronym `ACID`:

- `Atomicity`: ensures that all operations within the work unit are completed successfully; otherwise, the transaction is aborted at the point of failure, and previous operations are rolled back to their former state.

- `Consistency`: ensures that the database properly changes states upon a successfully committed transaction.

- `Isolation`: enables transactions to operate independently of and transparent to each other.

- `Durability`: ensures that the result or effect of a committed transaction persists in case of a system failure.

#####TRANSACTION CONTROL

There are following commands used to control transactions:

- `COMMIT`: to save the changes.

- `ROLLBACK`: to rollback the changes.

- `SAVEPOINT`: creates points within groups of transactions in which to ROLLBACK

- `SET TRANSACTION`: Places a name on a transaction.

Transactional control commands are only used with the DML commands `INSERT`, `UPDATE` and `DELETE` only.

They can not be used while creating tables or dropping them because these operations are automatically committed in the database.

#####COMMIT

The COMMIT command is the transactional command used to **save changes** invoked by a transaction to the database.

The COMMIT command saves all transactions to the database since the last `COMMIT` or `ROLLBACK` command.

The syntax for COMMIT command is as follows:

	:::sql
	COMMIT;

#####ROLLBACK

The ROLLBACK command is the transactional command used to **undo transactions** that **have not already been saved** to the database.

The ROLLBACK command can only be used to undo transactions since the last `COMMIT` or `ROLLBACK` command was issued.

The syntax for ROLLBACK command is as follows:

	:::sql
	ROLLBACK;

#####SAVEPOINT

A SAVEPOINT is a point in a transaction when you can roll the transaction back to a certain point without rolling back the entire transaction.

The syntax for SAVEPOINT command is as follows:

	:::sql
	SAVEPOINT SAVEPOINT_NAME;

This command serves only in the creation of a SAVEPOINT among transactional statements.

The ROLLBACK command is used to undo a group of transactions.

The syntax for rolling back to a SAVEPOINT is as follows:

	:::sql
	ROLLBACK TO SAVEPOINT_NAME;

#####RELEASE SAVEPOINT

The RELEASE SAVEPOINT command is used to **remove** a `SAVEPOINT` that you have created.

Syntax:

	:::sql
	RELEASE SAVEPOINT SAVEPOINT_NAME;

#####SET TRANSACTION

The SET TRANSACTION command can be used to **initiate** a database transaction.

	:::sql
	SET TRANSACTION [ READ WRITE | READ ONLY ];

###WILDCARD IN SQL

#####TYPES

- `%`: Matches **one or more** characters. Note that MS Access uses the asterisk (`*`) wildcard character instead of the percent sign (`%`) wildcard character.

- `_`: Matches **one** character. Note that MS Access uses a question mark (`?`) instead of the underscore (`_`) to match any one character.

The percent sign represents zero, one, or multiple characters. The underscore represents a single number or character. The symbols can be used in combinations.

#####Example

`WHERE SALARY LIKE '2_%_%'`: Finds any values that start with 2 and are at least 3 characters in length

###TEMPORARY TABLE

Temporary Tables are a great feature that lets you store and process intermediate results by using the same selection, update, and join capabilities that you can use with typical SQL Server tables.

The temporary tables could be very useful in some cases to **keep temporary data**.

>Temporary tables will be deleted when the current client session terminates.

Example:

	:::sql
	mysql> CREATE TEMPORARY TABLE SALESSUMMARY (
	-> product_name VARCHAR(50) NOT NULL
	-> , total_sales DECIMAL(12,2) NOT NULL DEFAULT 0.00
	-> , avg_unit_price DECIMAL(7,2) NOT NULL DEFAULT 0.00
	-> , total_units_sold INT UNSIGNED NOT NULL DEFAULT 0
	);
	Query OK, 0 rows affected (0.00 sec)

When you issue a `SHOW TABLES` command, then your temporary table **would not be listed out** in the list.

Now if you will log out of the MySQL session and then you will issue a SELECT command, then you will find no data available in the database.

Even your temporary table would also not exist.

By default, all the temporary tables are deleted by MySQL when your database connection gets terminated.

###SQL CLONE TABLES

If you are using MySQL RDBMS, you can handle this situation by the following steps:

- Use `SHOW CREATE TABLE` command to get a `CREATE TABLE` statement that specifies the source table's structure, indexes and all.

- Modify the statement to change the table name to that of the clone table and execute the statement. This way you will have exact clone table.

- Optionally, if you need the table contents copied as well, issue an `INSERT INTO ... SELECT` statement, too.

###SQL SUBQUERY

`Subquery` or `Inner query` or `Nested query` is a query within another SQL query and embedded within the WHERE clause.

There are a few rules that subqueries must follow:

- Subqueries must be enclosed within parentheses.

- A subquery can have only one column in the SELECT clause, unless multiple columns are in the main query for the subquery to compare its selected columns.

- An ORDER BY cannot be used in a subquery, although the main query can use an ORDER BY. The GROUP BY can be used to perform the same function as the ORDER BY in a subquery.

- Subqueries that return more than one row can only be used with multiple value operators, such as the IN operator.

- The SELECT list cannot include any references to values that evaluate to a BLOB, ARRAY, CLOB, or NCLOB.

- A subquery cannot be immediately enclosed in a set function.

- The BETWEEN operator cannot be used with a subquery; however, the BETWEEN operator can be used within the subquery.

#####SELECT EXAMPLE

	:::sql
	(SELECT column_name [, column_name ]
	FROM table1 [, table2 ]
	[WHERE])

#####INSERT EXAMPLE

	:::sql
	INSERT INTO table_name [ (column1 [, column2 ]) ]
	SELECT [ *|column1 [, column2 ]
	FROM table1 [, table2 ]
	[ WHERE VALUE OPERATOR ]

#####UPDATE EXAMPLE

	:::sql
	UPDATE table
	SET column_name = new_value
	[ WHERE OPERATOR [ VALUE ]
	(SELECT COLUMN_NAME
	FROM TABLE_NAME)
	[ WHERE) ]

#####DELETE EXAMPLE

	:::sql
	DELETE FROM TABLE_NAME
	[ WHERE OPERATOR [ VALUE ]
	(SELECT COLUMN_NAME
	FROM TABLE_NAME)
	[ WHERE) ]

###SEQUENCE

Sequence is **a set of integers** 1, 2, 3, ... that are generated in order on demand.

#####CREATING

The simplest way in MySQL to use sequences is to define a column as `AUTO_INCREMENT` and leave rest of the things to MySQL to take care.

	:::sql
	mysql> CREATE TABLE INSECT
	-> (
	-> id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	-> PRIMARY KEY (id),
	-> name VARCHAR(30) NOT NULL, # type of insect
	-> date DATE NOT NULL, # date collected
	-> origin VARCHAR(30) NOT NULL # where collected
	);
	Query OK, 0 rows affected (0.02 sec)

#####RENUMBERING

There may be a case when you have deleted many records from a table and you want to resequence all the records.

This can be done by using a simple trick but you should be very careful to do so if your table is having joins with other table.

If you determine that resequencing an AUTO_INCREMENT column is unavoidable, the way to do it is to:

1. drop the column from the table

2. add it again.

The following example shows how to renumber the id values in the insect
table using this technique:

	:::sql
	mysql> ALTER TABLE INSECT DROP id;
	mysql> ALTER TABLE insect
		-> ADD id INT UNSIGNED NOT NULL AUTO_INCREMENT FIRST,
		-> ADD PRIMARY KEY (id);

#####ASSIGN START VALUE

By default, MySQL will start sequence from 1 but you can specify any other number as well at the time of table creation.

	:::sql
	id INT UNSIGNED NOT NULL AUTO_INCREMENT = 100

Alternative:

	:::sql
	mysql> ALTER TABLE t AUTO_INCREMENT = 100;


###DUPLICATES

The SQL `DISTINCT` keyword, which we already have discussed, is used in conjunction with `SELECT` statement to eliminate all the duplicate records and fetching only unique records.

Syntax:

	:::sql
	SELECT DISTINCT column1, column2,.....columnN
	FROM table_name
	WHERE [condition]

###SQL USFUL FUNCTIONS

- SQL `COUNT` Function - The SQL COUNT aggregate function is used to count the number of rows in a database table.

- SQL `MAX` Function - The SQL MAX aggregate function allows us to select the highest (maximum) value for a certain column.

- SQL `MIN` Function - The SQL MIN aggregate function allows us to select the lowest (minimum) value for a certain column.

- SQL `AVG` Function - The SQL AVG aggregate function selects the average value for certain table column.

- SQL `SUM` Function - The SQL SUM aggregate function allows selecting the total for a numeric column.

- SQL `SQRT` Functions - This is used to generate a square root of a given number.

- SQL `RAND` Function - This is used to generate a random number using SQL command.

- SQL `CONCAT` Function - This is used to concatenate any string inside any SQL command.

- SQL `Numeric` Functions - Complete list of SQL functions required to manipulate numbers in SQL.

- SQL `String` Functions - Complete list of SQL functions required to manipulate strings in SQL.
.. title: SparkSQL Basics
.. date: 2015-08-10
.. category: Data Science
.. tags: Big Data, Spark, Data Science
.. slug: sparksql-basics
.. authors: Pengyin Shan
.. description: This post includes basic knowledge about SparkSQL, which will be continuously updated.

##Resource List

- <a href="www.sparkinchina.com">SparkSQL(Chinese)</a>, written by Junhui Ma, www.sparkinchina.com (i.e. `SparkSQL book` in my post)

##Traditional SQL and RDBMS

This is a graph of how traditional SQL query is processed, from SparkSQL book:

../images/articles/2015/data_science/regular_query.png 

A traditional SQL query following this sequence: `Result` -> `Data Source` -> `Operation`.

Step 1: a traditional RDBMS will first **parse** the sql query to get tokens such as `select`, `where`, etc.

Step 2: RDBMS will **bind** sql query to data source in database system, such as `table` or `view`. If all corresponding data sources in database exists, this sql query is executable.

Execute tree graph from SparkSQL book:

../images/articles/2015/data_science/sql_execute_tree.png 

During step2, RDBMS will also supply a few execution plan. RDBMS will choose the one with the best optimization.

**When RDBMS parse sql, it will transfer the sql to tree structure:**

../images/articles/2015/data_science/sql_tree.png 

#SparkSQL

SparkSQL(1.1) is combined by four modules:

- `core`: I/O operation. Get data resources(`RDD`, `JSON`, etc) then transfer it to `schemaRDD`.

- `catalyst`: Process sql query. The process includes: parsing, binding, optimizing, creating logic plan, etc.

- `hive`: process hive data.

- `hive-Thriftserver`: provide `CLI` and `JDBC/ODBC` interface.

##SparkSQL: Tree and Rule

Similar as traditional RDBMS, SparkSQL also parse SQL query to a **Tree** structure. The operation to tree is **Rule**, which involves in using pattern matching to decide which operation show be taken for a certain tree node.

###Tree

Tree can be used to show: `Logical Plans`, `Expressions` and `Physical Operators`.

The operation to tree is working on **TreeNode**. Just like normal tree data structure, SparkSQL can traverse whole tree or go to a certain tree node to perform operation.

####Three Types of Tree Node

- `UnaryNode`: Only one child node. Using for operations like `Limit`, `Filter`

- `BinaryNode`: Has left and right child node. Using for operations like `Join`, `Union`

- `LeafNode`: No child node. Using for user command, such as `SetCommand`

###Rule

`Rule` is a abstract class. It is extended by `RuleExecutor`.

Rule can perform `transform` operation by using `batch`es.

Rule can perform recursive operations by using `Once` and `FixedPoint`.

####Example for Rule: Analyzer

Analyzer graph from SparkSQL book:

../images/articles/2015/data_science/sparksql_analyzer.png 

Face in `RuleExcutor` class for Analyzer:

- There are multiple batches are used.

- Each batch is combined by different rules. Some rules may be applied multiple times.

- Each rule has its own functions

>Tree and Rule are working together to perform: parse operation, binding operation, optimizing operation, create logical plan, etc. Finally a executable plan will be created.

##SparkSQL: sqlContext

Source Code:

    :::scala
    def sql(sqlText: String): SchemaRDD = {
        if (dialect == "sql") {
        new SchemaRDD(this, parseSql(sqlText)) //parse sql query
        } else {
        sys.error(s"Unsupported SQL dialect: $dialect")
        }
    }

`sqlContext.sql` will return a `new SchemaRDD(this, parseSql(sqlText))`, which has been parsed by `catalyst.SqlParser`. Note `parseSql()` will return a `Unresolved LogicalPlan`.

sqlContext Process Graph from SparkSQL book:

../images/articles/2015/data_science/sqlcontext_process.png 

##SparkSQL: catalyst

Design of SparkSQL(1.1) from SparkSQL Book (dash line means future feature):

../images/articles/2015/data_science/catalyst_design.png 

Main modules for Catalyst:

- `sqlParse`: Parser for SQL query.

    - First, parse sql query to a tree, then apply rules to tree to perform transformation.

- `Analyzer`: Bind `Unresolved LogicalPlan` and meta-data from data resources. Generate `Resolved LogicalPlan`.

    - Use `Analysis Rules` and meta-data to generate `Resolved LogicalPlan`.

- `Optimizer`: Optimize `Resolved LogicalPlan`. Generate `Optimized LogicalPlan`.

    - Use `Optimization Rules` to perform a group of optimizing operations.

- `Planner`: Transfer `Logical Plan` to `Physical Plan`.

    - Use `Planning Strategies` to generate `Physical Plan`.

- `CostModel`: Choose best execution plan based on previous performance statistics.
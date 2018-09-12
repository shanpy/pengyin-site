.. title: SQL Tips
.. date: 2015-07-30
.. category: Data Science
.. tags: Database, SQL
.. slug: sql-tips
.. authors: Pengyin Shan
.. description: This post includes useful SQL tips I read online or learned in work, including using RDBMS directly or programming for it. This post will be updated continually.

###Using SQLProcessor in Java

My current job requires me to work on some old Java web application, which involves in connecting to Oracle SQL database using `SQLProcesoor`.

####Basic Syntax

    :::java
    //Assume you want to return an ArrayList of 'Course' objects
    public class SQLProcessorExample{
        public ArrayList<Course> selectSQLExample(final String anyParameter){
            ArrayList<Course> courses = new ArrayList<Course>;
            try{
                SQLProcessor sProc = new SQLProcessor();
                PreparedStatementGenerator coursePSG = new PreparedStatementGenerator() {
                        public PreparedStatement generatePrepareStatement(Connection conn) throws SQLException {
                            String sql = "select * from test_table where test_para = ?";
                            PreparedStatement ps = conn.prepareStatement(sql);
                            //Note: Index starting from 1. You can also use setInt or other setting methods
                            ps.setString(1, anyParameter);
                            return ps;
                        }
                ArrayList<String[]> result = new ArrayList<String[]>();
                //Use MultiResultListReader if you have mutiple rows returned
                MultiResultListReader reader = new MultiResultListReader(result);
                sProc.query(coursePSG, database_connection, reader);
                //Deal with your results
                for(String[] row : result) {
                    Course result_c = new Course();
                    result_c.setCourseNumber(row[0]);
                    result_c.setSectionNumber(row[1]);
                    //Process results...
                    courses.add(result_c);
                }
            }
            catch(Exception e){
                //Handle exceptions
            }
        }
    }

####Important Tips

If you have any trouble in your query and have no idea after checking with error message, try run this query in your **DB workbench** first. This may help with possible syntax error.

If you run query sucessfully in your DB workbench, but you get a `Invalid Indentifer` or `Invalid Keyword` exception in your Java app. **Make sure you check your query in code with all necessary white spaces. You may have muliple lines of query code and you forget spaces at the end of one line.**

Example:

    ```java
    String sql = "select * from table_test a, table_test2 b" +
                "where id = 1";
    //Notice this sql doesn't have white_space between 'b' and 'where', which will cause trouble
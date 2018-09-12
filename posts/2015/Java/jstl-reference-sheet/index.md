.. title: JSTL Reference Sheet
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Java
.. tags: Java
.. slug: jstl-reference-sheet
.. authors: Pengyin Shan
.. description: This is a reference sheet I created for using JSP-Standard Tage Library/JSTL, based on my learning from <a href="http://www.tutorialspoint.com/cgi-bin/printpage.cgi">JSP tutorial on tutorialspoint.com</a>. All code examples and definations are taken from this website.



There are five types of JSTL tag Library:

- Core Tags

- Formatting Tags

- SQL Tags

- JSTL Functions

- XML Tags (I skip this part)

Before you use JSTL library, you need to download it and put it to `webapps\ROOT\WEB-INF\lib` directoy.

##Core Tages

Make sure you include core tag library in your JSP file: `<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`

Following tags are common core tags with an explaination of their usage:

`<c:out>`: Display the result of an expression. Similar to `<%= %>` exception you use a `.` notation to access property now.

>Example: `<c:out value="person.age"/>`

`<c:set>`: Evaluates an expression and uses the result to set a value of a **JavaBean** or a **java.util.Map** object.

>Example: `<c:set var="var_name" value="${person.age}"/>`

`<c:remove>`: Remove a variable from either a specified scope or the first scope where the variable is found.

>Example: `<c:remove var="var_name"/>`

`<c:catch>`: Catches any throwable error and optionally expost it.

>You can combine it with <c:if>

	:::html
	<c:catch var="exception">
    <p>${person.age}</p>
	</c:catch>

	<c:if test="${exception!=null}">
	    <p>The exception is: ${exception}</p>
	</c:if>

`<c:if>`:Display content only if `test` is passed. `<c:choose>` ,`<c:when>` ,`c:otherwise>` ususally are used together to create (nested) if-else loop

>Example: `<c:if test="${person.age>20}">Hello World!</c:if>`

	:::html
	<c:choose>
	    <c:when test="${person.age>18}">
	        Adult
	    </c:when>
	    <c:when test="${12<person.age<18}">
	        Junior
	    </c:when>
	    <c:otherwise>
	        Child
	    </c:otherwise>
	</c:choose>

`<c:import>`: Work like `<include>`, takes an url and allows for inclusion of content from a differenet website or an FTP server.

>Example: `<c:import var="var_name" url="http://pengyin-shan.com"/>` fetches complete content from this website and would store in variable data.

`<c:forEach>`: Iterates over a collection of objects. Work like **for**, **while** or **do-while** in Java. Possiable Parameters:

- `begin`: Element to start with. 0 means the first item

- `end`: Element to end with. 0 means the first item

- `step`: Process every step items. Default is 1.

- `var`: Name of variable for current item

- `varStatus`: Name of variable for current loop status. Works like `i` or `count` in java.

Example:

	:::html
	<c:forEach items="${people}" var="person" varStatus="theCount">
	${theCount.index}
	</c:forEach>

Note: `{varStatus.index}` starts from **0**. `{varStatus.count}` starts from **1**.

`<c:forTokens>`: Similar as `<c:forEach>`. It is used to break a string into tokens and iterate through each of the tokens. Requested Parameter: **delims**, define character that is used for division.

`<c:url>` formats a URL string and optionally put to a variable and print to page

`<c:param>` allows proper URL request parameter to be specified with URL. Usually work with `<c:url>`

`<c:redirect>` automatically re-direct page to another URL

>Example: `<c:forTokens items="a,b,c" delims="," var="charName">${charName}</c:forTokens>`

	:::html
	<c:url var="testUrl" value="/index.jsp">
	    <c:param name="id" value="1234"/>
	</c:url>
	#now testUrl is: /index.jsp?id=1234
	<a href="<c:url value=${testUrl}">Test</a>
	<c:redirect url="${testUrl}"/>

##Formatting Tags

Make sure you include formatting tag library in your JSP file: `<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>`

Following tags are common formatting tags with an explaination of their usage:

`<fmt:formatNumber>`: format numbers, percentages and currencies. It has lots of parameters for configuration. You can view <a href="http://www.tutorialspoint.com/jsp/jstl_format_formatnumber_tag.htm">here</a> for detail.

>Example: `<p>Number is: <fmt:formatNumber value="${balance}" maxIntegerDigits="3" maxFactionDigits="3" pattern="###.###E0"></p>`

`<fmt:formatDate>`: Similarly but just for date. For example, you can set timezone using this tag. You can view detail <a href="http://www.tutorialspoint.com/jsp/jstl_format_formatdate_tag.htm">here</a>.

`<fmt:parseNumber>`: parse numbers, percentages and currencies. You are given a number and this tag can parse number to certain format. You can view <a href="http://www.tutorialspoint.com/jsp/jstl_format_parsenumber_tag.htm">here</a> for useful parameters.

>Example: `<fmt:parseNumber var="i" type="number" value="${balance}" integerOnly="true"/>`

`<fmt:parseDate>`:Similary, but just for Date. For example, you can set date as "YYYY-MM-DD" format. You can view detail <a href="http://www.tutorialspoint.com/jsp/jstl_format_parsedate_tag.htm">here</a>.

`<fmt:message>` tag maps key to localized message

`<fmt:bundle>` often being used with `<fmt:message>`. It will find a java class which extend ListResourceBunder, and use it for message

`<fmt:setBundle>` is similar to `<fmt:bundle>` except it not wraps `<fmt:message>`

	:::java
	public class Example extends ListResouceBundle{
	    public Object[][] getContents(){
	        return contents;
	    }
	    static final Object[][] contents = {
	        {"count.one","One"},
	        {"count.two","Two"}
	    }
	}

	:::html
	<fmt:bundle basedname="com.pengyinshan.Example">
	    <fmt:message key="count.one"/>
	    <fmt:message key="count.two"/>
	        #if you use <fmt:setBundle>, <fmt:message> will be outside
	</fmt:bundle>

`<fmt:setLocale>` is similar as `<fmt:setBundle>`. You need to specify class Name. Tag will find the scale that corresponds to this name
`<fmt:requestCoding>` set up encoding. You don't need extra class for it

Assume we have same example:

	:::java
	publc class Exmple_en_us extends ListResourceBundle{
		//...
	}

	:::html
	<fmt:requestEncoding value="en_us"/>
	<fmt:setLocale value="en_us"/>
	<fmt:bundle basedname="com.pengyinshan.Example">
	</fmt:bundle>

`<fmt:timeZone>` and `<fmt:setTimeZone>` are used to specify timezone in body.

They are oftern used above `<fmt:formatDate>`

	:::html
	<fmt:setTimeZone value="EST">
	    <fmt:formatDate value="${now}" timeStyle="long" dateStyle="long" type="both" />
	</fmt:setTimeZone>

##SQL Tags

Make sure you include sql tag library in your JSP file: `<%@ taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql" %>`

Following tags are common sql tags with an explaination of their usage:

`<sql:setDateSource>`: Takes several parameters and set data source.

>For example: `<sql:setDataSource var="snapshot" driver="com.mysql.jdbc.Driver" url="jdbc:mysql://localhost/TEST" user="user_id"password="mypassword"/>`

`<sql:query>`: Take several parameters and run a query. You can put result to a variable and use it as `var.id`, `var.last`, `var.name`, etc. You may want to use `<c:forEach>` for result.

>For example:

	:::html
	<sql:query dataSource="${snapshot}" var="result">
	SELECT * from Employees;
	</sql:query>

`<sql:udpate>`: Use for sql query that does not return value, such as **insert**, **update** or **delete**.

For example:

	:::html
	<sql:update dataSource="${snapshot}" var="count">
	   INSERT INTO Employees VALUES (104, 2, 'Nuha', 'Ali');
	</sql:update>

`<sql:param>`: Use for fill parameter to `<sql:update>` or `<sql:query>` if need.

`<sql:dateParam>`: Similaly but specailly used to modify date/timestamp.

The sequence of tags corresponding to sequnce of *?* in query.

For example:

	:::html
	<sql:update dataSource="${snapshot}" var="count">
	  Update Employees Set Dob = ? WHERE Id = ?
	  <sql:dateParam value="<%=DoB%>" type="DATE" />
	  <sql:param value="${empId}" />
	</sql:update>

`<sql:transaction>`: Wrap some `<sql:update>` and `<sql:query>` to create transaction.

For Example:

	:::html
	<sql:transaction dataSource="${snapshot}">
	#<sql:update>....
	</sql:transaction>

##JSTL Functions

Make sure you include function tag library in your JSP file: `<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>`

Normally JSTL functions are used within **${}**.

Following tags are common function tags with an explaination of their usage:

`<fn:contains>`: Equals to `boolean contains(java.lang.String, java.lang.String)`.

`<fn:containsIgnoreCase>`: Similar but just ignore case problem.

>Example:

	:::html
	<c:if test="${fn:contains(var_name,'test')}">
	<p>Found "test" in variable</p>
	</c:if>

`<fn:endsWith>`: Determines whether an input string ends with a specified suffix. Equals to `boolean endsWith(java.lang.String, java.lang.String)`.

`<fn:startWith>`: Similar but it work with prefix.

Example:

	:::html
	<c:if test="${fn:endsWith(var_name, '123')}">
	   <p>String ends with 123<p>
	</c:if>

`<fn:indexOf>`: Returns the index within a string of a specified substring. Equals to `int indexOf(java.lang.String, java.lang.String)`.

`<fn:length>`: Returns the length of a string. Equals to `int length(java.lang.Object)`.

`<fn:split>`: splits a string into an array of substrings. Equals to `java.lang.String[] split(java.lang.String, java.lang.String)`.

`<fn:join>`: Concatenates all the elements of an array into a string with a specified separator. Equals to `String join (java.lang.String[], java.lang.String)`.

`<fn:replace>`: replace **all occurrences** of a string with another string.

Example:

	:::html
	<c:set var="string1" value="This is first String."/>
	<c:set var="string2" value="${fn:split(string1, ' ')}" />
	<c:set var="string3" value="${fn:join(string2, '-')}" />
	<c:set var="string4" value="${fn:replace(string3, '-' , '+')}" />

`<fn:substring>`: Returns a subset of a string specified by start and end index. Equals to `java.lang.String substring(java.lang.String, int, int)`.

`<fn:substringAfter>`: Returns the part of a string after a specified substring. Example: `<c:set var="string2" value="${fn:substringAfter(string1, 'is')}" />`. Note `is` here is **included** in result.

`<fn:substringBefore>`: Returns the part of a string before a specified substring. Example is similar as above. Note `is` here is **excluded** in result.

`<fn:toLowerCase>` and `<fn:toUpperCase>`:take a string and transfer its case. For example: `<c:set var="string2" value="${fn:toLowerCase(string1)}" />`.

`<fn:trim>`: Removes white space from **both ends** of a string. Example: `<c:set var="string1" value="This is first String         "/>`.
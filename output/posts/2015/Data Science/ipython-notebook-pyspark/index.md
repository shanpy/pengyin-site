.. title: Install Apache Spark with IPython Notebook Configuration on Ubuntu 15
.. date: 2015-06-10
.. category: Data Science
.. tags: Python, Spark, IPython, Data Science
.. slug: ipython-notebook-pyspark
.. authors: Pengyin Shan
.. description: I'm attending an "Introduction to Spark" online course, using Python and PySpark. I want to create an development environment on my Ubuntu 15 machine.

After reading a few useful posts and some debugging time, I successfully installed **Apache Spark** on my Ubuntu 15 machine. I also add **PySpark** in **IPython Notebook** for development purpose.

Many thanks to author of these articles:

<a href="http://blog.cloudera.com/blog/2014/08/how-to-use-ipython-notebook-with-apache-spark/">How-to: Use IPython Notebook with Apache Spark</a>, written by Uri Laserson.

<a href="http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/">Configuring IPython Notebook Support for PySpark</a>, written by John Ramey.

<a href="https://beingzy.github.io/tutorial/2014/10/13/spark-tutorial-Part-I-setting-up-spark-and-ipython-notebook-within-10-minutes.html">Spark Tutorial (Part I): Setting Up Spark and IPython Notebook within 10 minutes</a>, written by Yi Zhang.

<a href="https://ipython.org/ipython-doc/dev/config/intro.html">Introduction to IPython Configuration</a>

Install Python and IPython Notebook
------------------------------------

I highly recommend you using <a href="https://virtualenv.pypa.io/en/latest/">Virtualenv</a> or <a href="https://store.continuum.io/cshop/anaconda/">Anacona</a> for Python package control.

You need to install **Python** and **pip** first (You can find installation documents through Google Search). Then in terminal, type following:

    :::shell-session
    $pip install "ipython[notebook]"

If you want to install everything for IPython, including Notebook, type following in terminal:

    :::shell-session
    $pip install "ipython[all]"

You can test your installation by type following command in terminal (Make sure you are in right environment):

    :::shell-session
    $ipython notebook

Your default browser should open a window with IPython Notebook interface.

Install Spark and PySpark
--------------------------

You can download Spark from <a href="https://spark.apache.org/downloads.html">here</a>. You can install either source code package, or a pre-build package. All packages can be installed and configured for IPython Notebook.

Pre-build package can be extracted and being used directly. If you download source package, you need to do this after extracting:

    :::shell-session
    $cd your_spark_source_folder
    $sbt/sbt assembly

>This process may take a while :)

You may need to install **sbt** first. For Linux user, please refer to this article: <a href="http://www.scala-sbt.org/0.13/tutorial/Installing-sbt-on-Linux.html">Installing sbt on Linux</a>.

You can test your installation by doing following:

    :::shell-session
    $cd your_spark_folder
    $./bin/pyspark

>You need java jdk installed on your machine and JAVA_HOME has been set, otherwise PySpark will throw error for that, such as:

../images/articles/2015/python/hadoop2.6_java_home_dir_problem.png 

>Make sure your JAVA_HOME pointing to home folder of your desired JDK. For example, I want to use Oracle JDK 8. So I type `sudo update-alternatives --config java` in terminal to find preferred JDK path (JDK 8 in my case), then add`export JAVA_HOME=/usr/lib/jvm/java-8-oracle` in `.bashrc` file.

You should see following in your terminal. Type `sc` and you should see output as `SparkContext`:

../images/articles/2015/python/test_pyspark.png 

Configure PySpark and IPython Notebook
-----------------------------------

Based on my experience, PySpark has good support for Python 2.7, but not Python 3. I recommend you use **Python 2.7** in this step.

<a href="http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/">Configuring IPython Notebook Support for PySpark</a>, written by John Ramey, gave a very good description of steps you need to follow. However, you need to remember doing following:

In `.bashrc` and `00-pyspark-setup.py`, make sure you have your own Spark folder name. Check your `your_spark_folder/python/lib` for py4j version.

After you do `ipython notebook --profile=pyspark`, you will open Jupyter web interface in your default browser, using the `c.NotebookApp.port` in your `.bashrc` file.

In Jupyter interface, You can upload one existing IPython Notebook to test your configuration by clicking `Upload` button, Or create a new IPython Notebook by clicking `new` button, then select `Python 2` or `Python 3` in drop-down menu.

In IPython Notebook interface, create a new cell and type `sc`. When you run this cell, you should see `SparkContext` object, same as following:

../images/articles/2015/python/test_pyspark_notebook.png 

>Now, if your IPython Notebook show message: `NameError: name 'sc' is not defined`, which means your IPython Notebook doesn't use PySpark profile. You can try typing `ipython --profile=pyspark` in terminal to make PySpark as default IPython profile, then try `ipython notebook --profile=pyspark` again. PySpark should be available now.
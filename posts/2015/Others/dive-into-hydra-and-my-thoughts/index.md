.. title: Dive into Hydra and My Thoughts
.. date: 2015-08-09
.. modified: 2015-08-12
.. category: Others
.. tags: Hydra, Digial Library
.. slug: dive-into-hydra-and-my-thoughts
.. authors: Pengyin Shan
.. description: Project Hydra is a powerful repository solution, which are used by lots of institutions. To learn more about Hydra, I tried the Dive into Hytra tutorial. This posts includes my thoughts about it.

*This post is being updated while I'm learning more about Hydra*

###Main Idea

I used to create a small Spring MVC web app <a href='https://github.com/shanpy/RDFExperiment'>RDF Experiment</a> to experiment the ideas behind Hydra. Following is a graph about my assumption of Hydra Idea:

../images/articles/2015/digital_library/ProjectHydra.png 

Behind this large frame, there are lots of small classes/methods that will push through stages above.

####Key Concerns

Following key concerns should be evaluated carefully during the processes above:

- When parsing RDF file to Model, what are the key properties which should be kept? What are properties that should be ignored? How client and domain expert think about your solution?

- What's the best way of modeling Fedora and Solr such that user can use different way of searching, and getting best result? Is there any possibility to shorten result list, while not losing necessary close-results? Is there any way to shorten the searching time?

- Is there any visualization job can be done to let user understand more about results?

###Problems and Thoughts

####Installation

Although RubyInstaller is available in Windows, I still encountered lots of unexpected errors when setting up environment in Windows 10. I took much less time in Linux. I used to run CygWin for virtual Linux environment in Windows, but it's not work well for any environment setup process, including Python and RoR.

If anyone is like me who are starting a taste of Hydra, I suggest using Unix-Based system first.

*Update on 8/12/15*: I created a <a href="http://pengyin-shan.com/blog/setting-up-ror-hydra-environment-problems-and-solutions">post</a> talking about installation of RoR and Hydra. If you need to install RoR or Hydra, feel free to use this post.

####RoR

Since both Spring and Rails framework are holding MVC structure, it's not hard to transfer idea from Spring to RoR. Subfolders in `app` folder self-explained themselves:

- `controllers`, `models`, `views` are folders for MVC structure.

- `assets` has static resources.

- `helpers` is special for RoR. Since `helper` is targeted to for variables talking before controller and view, they are very similar to `model attributes` in Spring MVC framework.

The basic structure of Hydra-Demo is similar to the a Node.js app, and `Gemfile` is similar to `requirements.txt` file in Python.

####Deployment

Unfortunately, although Hydra is can be deployed on development environment easily for a single developer, there's no hosting platform that fully host a production environment of it. Following problem needs to be considered:

First, the default database needs to be changed in `database.yml`. Obviously not a lot of institutions will use SQLite3 (Default) in production environment.

*Solution*: I have tried to replace it by MySQL and PostgreSQL, and these two solution all work. I believe other RDBMS should also work well. Just need to change `Gemfile`. Replace `gem 'sqlite3'` to `gem 'pg'` or `gem 'mysql2'`.

`database.yml` can be changed as following for development purpose:

    :::yml
    default: &default
    adapter: postgresql
    pool: 5
    development:
      <<: *default
      url: postgresql_url_or_environment_virable
      database: database_name
      username:
      pasword:
    test: #...
    production: #...

Second problem is the host of fedora commons. As a single developer, I cannot find a cloud-hosted fedora to make calls, which cause me the problem of hosting hydra demo on cloud.

*Solution*: Since fedora commons has pretty good deployment guideline, I will try to deploy one on Amazon AWS, then adjust `fedora.yml` in hydra-demo when moving to cloud.

*Update 08/10/15*: When I tried to deploy Fedora 4 on my local machine using Jetty 8, I got unexpected error message, such as  `Problem processing jar entry org/fcrepo/kernel/modeshape/observer/GetNamespacedProperties.class` `java.lang.ArrayIndexOutOfBoundsException: 16680`. It happens to lots of fedora classes, such as `org/fcrepo/http/commons/api/rdf/HttpTripleUtil.class`. I need to figure out this problem before deploying fedora to cloud platform. Tomcat 7 gave no error message, but still unable to deploy it.

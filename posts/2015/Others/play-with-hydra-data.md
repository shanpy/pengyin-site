.. title: A Journal of Playing with Hydra Data
.. date: 2015-08-12
.. category: Others
.. tags: Hydra, Fedora, Solr
.. slug: play-with-hydra-data
.. authors: Pengyin Shan
.. description: When I started to create multiple development environment for my Hydra experiment project, moving data from one to another become a high-priority problem. When I looked into my project to find the proper way, I realize a post is necessary to record my exploration about data processing between Hydra, Fedora and Solr.

##Data Immigration

*This part is based on the <a href="https://github.com/projecthydra/hydra/wiki/Dive-into-Hydra">dive-into-hydra</a> tutorial project.*

What should I do to immigrate Hydra Data (Fedora files, Solr documents and indexes, etc) from one Hydra project to another project?

To figure out a way, I have explored following items:

###Step 1: SQLite3

**8/12/15**

My first idea is to check database. Tutorial project uses SQLite3 as database. All files are included in `/db` folder. Before going to production, you may get `developer.sqlite3`, `test.sqlite3`.

I used `SQLiteStudio` to open these two SQLite3 databases. Each database has four tables, which are:

- `bookmarks`: save information when a bookmark is created. Sample Fields: `user_id`, `document_id`, `title`, `created_at`, etc

- `schema_migrations`: version of query schema

- `searches`: save information when a search operation is performed. Sample Fields: `user_id`, `query_params`, `created_at`, etc

- `users`: user information. Sample Fields: `email`, `current_sign_in_ip`, `encrpted_password`, etc.

It seems that database(SQLite3) here is used to record information in search process, after all previous data has been immigrated.

Now my question is: *Does Hydra have a solution?*

###Step 2: Hydra

**8/12/15**

I did some research about a full immigration solution in Hydra. I didn't find any result, which is nature because Hydra includes so many components: Fedora, Solr, Blacklight, etc. It would be extremely hard to transfer all data from these components once, without any error.

After I re-think my requirement, I realize this is what I want: **Get all data from Fedora in old project -> Put it to Fedora in new project, with same structure -> Solr in new project re-indexing -> Blacklight can find new documents**

Now I want to start the process of *export and import Fedora data*.

###Step 3: Fedora

**8/12/15**

####Data Export

Fedora4 provides a <a href="https://wiki.duraspace.org/display/FEDORA40/RESTful+HTTP+API">RESTful HTTP API</a> for data processing.

To export serialized form of a resource, **with all subtress and binary content**, run following in your terminal (I adjust path based on my project):

    :::
    curl -u fedoraAdmin:fedoraAdmin http://127.0.0.1:8983/fedora/dev/fcr:export?recurse=true&skipBinary=false"

Make sure to use your own fedora username and password.

This command will generate a group of `xml` code, save it to a `xml` file, such as `FedoraExport.xml`.

####Data Import

Now go to your new project and get a copy of your exported xml file. Run following command to import:

    :::
    curl -u fedoraAdmin:fedoraAdmin -X POST --data-binary "@FedoraExport.xml" "http://127.0.0.1:8983/fedora/rest/dev/fcr:import?format=jcr/xml"

Now restart jetty and navigate to `http://127.0.0.1:8983/fedora/rest/dev`. I'll be able to see all data, includes all subtrees, in the Fedora of new project.

I also noticed Fedora UI can import and export xml files. However, there is no recursive export feature there.

>Problem: When I followed tutorial project, I made all the book nodes under /fedora/rest/dev. When I did export, I had to export dev node to make sure it includes book childnodes. After I imported dev node to new /fedora/rest/dev, I realized I had two dev nodes now. Another solution is to replace new fedora's dev node. However after I imported dev node directly to /fedora/rest, the new dev node will show as 'dev%5B2%5D' instead of 'dev'.

>Possible Solution: I should create a summary node, which includes all my books data. I export this summary node and import it to /fedora/rest/dev. Now I can have exactly same structure as old fedora.

Now I want to start the process of *Solr re-indexing*.

###Step 4: Solr

Working in process :)
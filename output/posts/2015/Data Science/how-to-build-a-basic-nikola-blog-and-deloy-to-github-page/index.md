.. title: How to Build A Basic Nikola Blog and Deploy to Github Page
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Data Science
.. tags: Python, Nikola, Github
.. slug: how-to-build-a-basic-nikola-blog-and-deloy-to-github-page
.. authors: Pengyin Shan
.. description: This is a *old post* from my Nikola blog. I created it when I tried Nikola to learn Python. Current blog site is built by Pelican.



One of my goal for 2015 is to learn Python. To prepare for this, I decided to create a new blog site, based on Python.

After doing some research, I decide to use <a href="http://getnikola.com/">**Nikola**</a> to build my blog. One of the reason I choose Nikola is that it has great support to **IPython Notebook**.

#### Lots of Thanks to <a href="http://www.damian.oquanta.info/">Damian Avila</a>! Your blog is so useful and great for Nikola beginners like me!

**1. Create Virtual Environment**

Before you install Nikola, a good practice is to build a virual environment. You can install **Virtualenv** and use it. Since I had **Anaconda** installed, I just type `conda create -n techblog python=3.4 anaconda` to create a virtual environment called "techblog" with python 3.4. You can define your own name and python version.

**2. Install Nikola and Necessary Component**

*First, make sure you use your virtual enviorment. command is:* `source activate name_of_environment`

I suggest you to use **pip** to install followiing components:
- nikola
- requests
- sphinx
- pyzmq
- tornado(?)
- jinja2
- webassets (if you want to use USE_BUNDLES)
- markdown (if you want to use markdown)
- ipython (if you want to use ipython notebook)

For example, you type follwing command in your terminal: `pip install nikola requests sphinx markdown ipython pyzmq tornado jinja2 webasset`

*In the next following steps, make sure you are under your virtual environment.*

**3. Initialize Nikola**

Type `nikola init` in your terminal, where you want to build your site in a *subfolder* of current location.

You will be asked following questions:
- Destination: Name of the folder your site will be
- Site Title
- Site Author
- Author's Email
- Site Description
- Site URL: This is the url that when you click header of your site, the page will jump to. You can set this later in **conf.py** file. If you type one, make sure it ends with a */*.
- Default Language: I use **en** but you can refer Nikola website for more option.
- Time Zone: Short name for your time zone. I use **EST**. For example.
- Comment System: Nikola support popular comment system such as *Disqus*, *Google+* and *Facebook*. You will be asked to enter *comment system site identifier* if required.

**4. Change Theme (Optional)**

If you want to change theme of your website, You can find a list of themes from <a href="http://themes.getnikola.com/">Nikiola Website</a>. Note any theme that has *ipython* in its name supports IPython Notebook.

Then, do `cd your_folder` to get to the folder that Nikola just created for you.

Type `nikola install_theme name_of_theme` to install theme.

You may need to change some setting in **conf.py** file, so read instructions in your terminal carefully.

**5. Configure and Build Site**

First, open **conf.py** file and configure it as your requests:

- If you didn't do some setup in step 3 in terminal, you can found them here. For example, you can re-edit **SITE_URL** if you haven't done so.

- If you have installed new theme and want to change to it, change **THEME=** option to your installed theme. Some theme may also want you to change **NAVIGATION_LINKS** or other settings.

- If you want to use IPython Notebook or Markdown, find **POSTS =** option and add `("posts/*.md", "posts", "post.tmpl"),("posts/*.ipynb", "posts", "post.tmpl"),`. *If you don't need lots of new pages, I suggest you not change PAGES setting.*
- Set **INDEX_TEASERS = ** to **True** to enable teaser. Now you can just put `.. TEASER_END` or `<!--TEASER_END-->` in your post to make index page only show first part of your post

- If you have installed **webassets**, you can set **USE_BUNDLES=** to **True** to speed up your site.

- I skip the process of creating new post. Note if you create a IPython Notebook post, you can edit information such as slugs, dates, tags in **.meta** file, which is automatically generated with **.ipynb** file.

Now you can type `nikola build` to build your site. A list of rendered file will appear.

- What user can see from your website is in **output** folder.

- If you have any external file, such as **PDF** or **IMAGE**, you can put it in **files** folder.

After building, you can type `nikola serve` to host your site locally. By default, you site can be open from `http://localhost:8000/`

**6. Deploy Site to Github Pages**

I find great help from <a href="http://www.damian.oquanta.info/posts/one-line-deployment-of-your-site-to-gh-pages.html">solution of Damian's blog</a>. I used his method to deploy this site to one of my Github page.

Please make sure you do follwing steps except git initiate every time you want to make change:

- First, create a repository. You can use default "user.github.io" repo, but since I prefer a **project Github Page**, so I create a repo called "techblog".

- After installed **Git** to your machine, `cd` to your site folder, then type `git init` to initiate.

- Do `git remote add origin https://github.com/your_user_name/your_repo.git` to add repo, with a name *origin*.

- Push all of your content to **master** branch first

- Do `git checkout -b gh-pages` to create and swich to gh-pages. You can skip `-b` after you do this once.

- Do `git rm -rf .`

- Do `git commit -am "Your Commit"` to commit for gh-pages

- Do `git push origin gh-pages`

- Do `git checkout master` to switch back to master branch

- Do `git branch -D gh-pages` first to avoid commit error. (I tried to skip this step before but I got a git commit error, so I suggest you do this step first)

- Do `git subtree split --prefix output -b gh-pages` to only transfer content in **output** folder from master to gh-pages

- Do `git push -f origin gh-pages:gh-pages` to force push

- Do `git branch -D gh-pages` again to delete local gh-pages branch

**7. Add Custom Domain to Your Github Page (Optional)**

You may want to add custom domain to your Github page. Github has a tutorial <a href="https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/">here</a>. Since I'm hosting my domain (pengyin-shan.com) on GoDaddy, I followed instructions <a href="http://captainwhippet.com/blog/2014/05/11/blog-setup-details.html">in this blog</a>.

A few things I want to mention:

- **CNAME** file should be put to your **files** folder so that when you following steps above to push to Github, this file will show in gh-pages branch.

- The content of **CNAME** file should be bare subdomain of your custom domain, which means you *can not* use `http://test.com` or `http:test.com/blog`. You can only have one custdom domain.

- I think based on Github's role, even though you are hosting project Github pages, your custom domain has to be "test.com" instead of "test.com/name_of_repo"

- On Jan 1st, 2015, the IP address of **Github Project Page** are `192.30.252.153` and `192.30.152.154`. If you have A (Host), make sure your `@` is pointing to these two IPs.

If you finish these settings, you should be able to host your Nikola blog on Github Page. Please feel free to let me know if you have any comments.
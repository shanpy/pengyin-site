.. title: SASS Q&A and Tips CONTINUALLY UPDATE
.. date: 2015-01-13
.. modified: 2015-05-30
.. category: Front End
.. tags: SASS, Compass, CSS
.. slug: sass-qa-and-tips
.. authors: Pengyin Shan
.. description: This is an old blog I created when I started to learn SASS on late 2014. I'll continue to update this post while I'm using Compass/SASS.



This post will serve as a Q&A note during the process of learning Sass. I'm absolutely a new beginner so I'll keep questions and answers updating continously:)

##Question: What is the syntax difference between sass and scss?

So far I've found following difference:

- scss is similar to css style, requires "{" and ";"

- sass has none of these

- sass is white space recoginized while scss not

##Question: How Jekyll work with Sass?

Currently version of Jekyll (2.4.0) has native support for Sass and CoffeeScript. Official documentation is here: http://jekyllrb.com/docs/assets/

I use official way for sass compile by following step:

In home directory, create a folder called _sass. I decide to use this folder for sass files that I will import from.

Add following lines in _config.yml to register _sass folder:

>sass:
>  sass_dir: _sass

You can always modify it to your folder name.

Create a folder called "css", then put all scss file there. Now website has:

	:::javascipt
	/css
		- default.scss
		- header.scss
		- page.scss
	/_sass
		- _test.css

In scss file, first two lines needs to be '- - -'. You can use @import 'test' to import _test.sass file in _sass.

>Please make sure everything in _sass folder start with a '_'.

>You don't need to put '- - -' to files in _sass folder.

In html page, add link to these scss file, using '.css' extension. For example: `<link rel="stylesheet" type="text/css" href="/css/default.css">` pointing to default.scss in css folder. You can actually find default.css in _site/css folder

Jeyll will automatically compile scss and sass file when you build your project.

On Jekyll website, there are some websites that are built with Sass. You can refer them for folder structure on your own blog site.

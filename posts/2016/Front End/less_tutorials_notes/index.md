.. title: LESS Tutorials Notes
.. date: 2016-01-20
.. category: Front End
.. tags: CSS, LESS, draft
.. slug: less_tutorials_notes
.. authors: Pengyin Shan
.. description: This is a reading notes from <a href="http://www.tutorialspoint.com/less/index.htm">Tutorialspoint.com LESS Tutorial</a>. I changed my job on Dec 2015, and LESS is necessary for me to become a better web developer.

###Installation

**Node.js** has to be installed first. Then do `npm install -g less` to install LESS.

After you have a LESS file, run `lessc your_file.less target_name.css` to generate corresponding CSS file.

###Nested in LESS

Nested classes/directives can be used in LESS:

    #!less
    .container{
      h1{
        color: black;
        @media(mid-width: 769px){
          color: pink;
        }
      }
      p{
        color: red;
      }
    }

###Operations in LESS

After declaring variables using `@`, LESS allows use to use `+`, `-`, `*` and `/` to do math operations.

Make sure you always use `@` to refer variables:

    #!less
    @fontSize: 10px;
    .testClass{
      font-size: @fontSize * 1.5;
    }
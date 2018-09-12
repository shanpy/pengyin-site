.. title: Bootstrap 3 Sticky Footer by Martin Bean and Ryan Fait
.. date: 2015-07-09
.. category: Front End
.. tags: HTML5, JavaScript, CSS, Bootstrap3
.. slug: bootstrap3_sticky_footer
.. authors: Pengyin Shan
.. description: When I was working on creating front-end template for my work project, I found this <a href="http://getbootstrap.com/2.3.2/examples/sticky-footer.html">Sticky Footer</a> created by Martin Bean and Ryan Fait. It's a really clean and elegant solution. I learned a lot from it.

You can view introduction page <a href="http://getbootstrap.com/2.3.2/examples/sticky-footer.html">here</a>.

Generally A sticky footer is created just like the `fixed-nav` bar in Bootstrap3. This footer will always stay at the bottom of page, even though there isn't enough content.

Martin Bean and Ryan Fait also have a Sticky Footer with Fixed Nav Bar page <a href="http://getbootstrap.com/2.3.2/examples/sticky-footer-navbar.html">here</a>.

Following is part of basic code for Sticky Nav bar with my analysis (You need Bootstrap3 css library):

>In HTML, You have two big divs: `#wrap` and `#footer`. `#footer` contains everything you want to put in footer.

>`#wrap` has two small divs: `.container` and `#push`. You put all main content in `.container` and nothing in `push`

    :::html
      <body>
        <!-- Part 1: Wrap all page content here -->
        <div id="wrap">
          <!-- Begin page content -->
          <div class="container">
            <!-- Content -->
          </div>
          <div id="push"></div>
        </div>
        <!-- Park 2: Footer -->
        <div id="footer">
          <!-- Footer -->
        </div>
       </body>

>`#wrap` takes full height of page. You set this by using `min-height`. Set `height` to `auto` to make sure small amount of content will not shrink `#wrap`. `#wrap` has a bottom margin `-60px`. This number can be changed, but it must be the same height as `#push` and `#footer`. This negative margin can allow `#footer` always stick to bottom of `#wrap`.

>`#push` is used as a placeholder for `#footer`. `#footer` has same height as `#push`, so it **covers** `#push` because of the negative margin in `#wrap`. Items above `#push` will stay in distance from `#footer`, because since they have bottom margin to `#push`, they now have bottom margin to `#footer`.

    :::css
      /* Sticky footer styles
      -------------------------------------------------- */
      html,
      body {
        height: 100%;
        /* The html and body elements cannot have any padding or margin. */
      }
      /* Wrapper for page content to push down footer */
      #wrap {
        min-height: 100%;
        height: auto !important;
        /* Negative indent footer by it's height */
        margin: 0 auto -60px;
        /**In th
      }
      /* Set the fixed height of the footer here */
      #push,
      #footer {
        height: 60px;
      }


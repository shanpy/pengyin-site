A plugin to create "related posts" data.

This plugin uses [gensim](https://radimrehurek.com/gensim/) to
analyze your posts and find which ones are similar to one another.

The scoring mechanism is "inspired" by [YARPP](https://www.slideshare.net/mitcho/the-yet-another-related-posts-plugin-algorithm-explained/9)
and takes into account the title, tags and content of a post.

For each post there will be a JSON file with the additional data.
For example, if your post is in `output/foo/bar.html` then
the related posts data will be in `output/foo/bar.html.related.json`
and looks like this:

```
[
  {
    "detailed_score": [
      0,
      0.4,
      0.9999980926513672
    ],
    "score": 1.8999971389770507,
    "title": "The Long Post About PyCamp 2012",
    "url": "/posts/the-long-post-about-pycamp-2012.html"
  },

... ]
```

The `detailed_score` is the score from tag, title, and body similarity.

Caveats:

* This will make your builds slower.

  * There is a considerable and somewhat unavoidable startup cost.
  * Any change in any post involves recalculating the
    similarity data for **all** posts.
  * The more translations you have, the longer it takes.
  * My test site contains 1300 posts of varied lengths in 2 languages,
    and initialization takes ~90 seconds.

* You will need to hack your templates to load the
  similarity data and display it to the user.

Assuming you use a theme that makes JQuery available like bootstrap3,
this would work. If not, change as needed.

In post.tmpl, where you want the related post links to appear:

```
    <div id="related-posts" class="related">
    <h3>Related Posts:</h3>
    </div>
```

And then add a script to load them there, like this:

```
<%block name="extra_js">
    <script>
        // If you are using PRETTY_URLS=False
        //jQuery.getJSON("${post.permalink()}.related.json", null, function(data){
        // If you are using PRETTY_URLS=True
        jQuery.getJSON("${post.permalink()}/index.html.related.json", null, function(data){
            var items = [];
            $.each(data, function(i) {
                items.push("<li><a href="+data[i].url+">"+data[i].title+"</a></li>")
            });
            $( "<ul/>", {
                "class": "related-items",
                html: items.join( "" )
            }).appendTo( "#related-posts" );
        });
    </script>
</%block>

```

A ``SIMILAR_COUNT`` option controls how many "similar posts" are chosen, and it defaults to 10.
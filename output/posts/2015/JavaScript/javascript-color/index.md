.. title: JavaScript and Color
.. date: 2015-07-02
.. category: JavaScript
.. tags: JavaScript
.. slug: javascript-color
.. authors: Pengyin Shan
.. description: This post is used to record useful tips of controlling color using JavaScript

##JavaScript Supporting Color Names

In JavaScript, there is a list of SAFE color name that you can use directly:

1. `#00FFFF` aqua
2. `#000000` black
3. `#0000FF` blue
4. `#FF00FF` fuchsia
5. `#808080` gray
6. `#008000` green
7. `#00FF00` lime
8. `#800000` maroon
9. `#000080` navy
10. `#808000` olive
11. `#800080` purple
12. `#FF0000` red
13. `#C0C0C0` silver
14. `#008080` teal
15. `#FFFFFF` white
16. `#FFFF00` yellow

All the colors above can be set or retrive directly, using their name. For example:

    :::javascript
    if(value == 'teal')
        value = 'yellow'
    else
        value = 'purple'

For other colors, you may need to use RBG value in JavaScript, such as 'rgb(0,2,2)'.
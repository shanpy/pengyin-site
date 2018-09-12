.. title: Spring Tips
.. date: 2015-06-16
.. category: Java
.. tags: Java, Spring
.. slug: spring-tips
.. authors: Pengyin Shan
.. description: This post serves as a sticky note for me to record Spring Core/MVC tips I got in job. I will update this post when I learn more.

------------------------------------------------------------------------------

In Spring MVC, if AJAX pass back a `String`, use `JSON.parse()` to transfer it to JSON object first.

------------------------------------------------------------------------------

###Use Session Object in Controller

Way1:

    :::java
    \\...(...HttpSession sessionObj){
        sessionobj.setAttribute('name_of_attribute', attribute_object);
        return "redirect:/...";
    }

Way2:

    :::java
    \\...(...HttpSevletRequest req){
        HttpSession session = req.getSession();
        Object_Type obj = (Object_Type)session.getAttribute("name_of_attribute");
        //Object_Type: int, String, float, etc
    }

Different from `flash attribute`, if we use session, attribute in front-end will not be erased after reloading.

-------------------------------------------------------------------------------

##Spring MVC Form Tips

###Spring Form Validation:

Way 1:

    :::html
    <form:form ... onsubmit='return valid()'>
        <!--. Code... -->
    </form:form>
    <script>
    function valid(){
        //...return true;
        //...return false;
    }
    </script>

Way 2:

    :::html
    <form:form ...>
        <!--. Code... -->
        <button onclick="valid(event)">Submit</button>
    </form>
    <script>
    function valid(event){
        event.preventDefault();;

        //...Add Validation JavaScript
        $('#form_id').submit();
    }
    </script>

###Submit Spring Form in jQuery:

    :::javascript
    $('#Form_ID').submit(function(e){
            e.preventDefault();
            //...
            $.each(this, function(i,v){
                    var all_inputs = $(v); //value of <form:input>
                    //The is a way of get Spring form input value in JavaScript
                    //i is index, v is value. You can use this method to iterate JSON object
                })
        });

>If you add `value` attribute for `<form:input>`, you may got `No Such Element` error

>If you are using Eclipse, comment your unwanted Spring code will not work! You should remove unwanted Spring code instead of commenting them, because Eclipse will compile Spring code anyway, and you may get error because of that.

-------------------------------------------------------------------------------

##Spring and AJAX

I wrote any post about Spring and AJAX <a href="http://pengyin-shan.com/ajax-and-spring-mvc-controller.html">here</a>.
Post Method in jQuery:

    :::javascript
    $.ajax({
            contentType: "application/json; charset = urf-8;"
            url: '...',
            type: 'POST',
            data: JSON.stringify(json_obj),
            success: function(result, textStatus, jqXHR){
                //...;
            },
            error: function(jqXHR, textStatus, Error){
                //...;
            }
        });

Post Method in Spring Controller:

    :::java
    @RequestMapping(value="/your_mapping_url", method={RequestMethod: POST})
    public @ResponseBody String/ModelAndView (@RequestBoday final String json_obj){
        //...You may want to parse json_obj to JSONObject
    }

>In Java, a `Gson` library from <a href="https://code.google.com/p/google-gson/">Google</a> can transfer Java `Object` to `JSONObject` directly.

>Example:

    :::java
    Gson gson = new Gson();
    String json_str = gson.toJson(Object_Instance);
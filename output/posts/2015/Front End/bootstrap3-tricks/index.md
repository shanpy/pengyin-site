.. title: Bootstrap3 Tips CONTINUALLY UPDATE
.. date: 2014-12-10
.. modified: 2015-05-31
.. category: Front End
.. tags: CSS, Bootstrap3, JavaScript, jQuery
.. slug: bootstrap3-tricks
.. authors: Pengyin Shan
.. description: This is an old blog I created when I started to learn Bootstrap3, recording useful tips during my development process. This post will be UPDATING CONTINUALLY, since I'm still digging more into Bootstrap3.

This post is transferred from my <a href="http://blogpengyin.herokuapp.com/">old Hexo blog site</a>, created on 2014. This blog will be **updating continually**.

If you want to find specific topic, feel free to use `ctrl + F` to search for keyword.

#Change Glyphicon when Bootstrap Collapse Show or Hide

This is what I learned from: http://stackoverflow.com/questions/18325779/bootstrap-3-collapse-show-state-with-chevron-icon . The answer is from `zessx`.

    :::html
    <div class="panel-heading" role="tab">
        <a class="collapsed" data-toggle="collapse" data-parent="#accordion" href="#test" aria-expanede="true" aria-controls="test">
            <span class="glyphicon glyphicon-plus"></span>
            Here, when a panel is collapsed, a glyphicon-plus will appear.
            When it is toggled (i.e, change to a different state, which is not collapsed), a glyphicon-minus will appear.
        </a>
    </div>

    <script type="text/javascript">
        function toggleChevron(e) {
        $(e.target)
            .prev('.panel-heading')
            .find('span') //find elements that has tage 'span'
            .toggleClass('glyphicon glyphicon-minus glyphicon-plus');
        }
        $('#accordion').on('hidden.bs.collapse', toggleChevron);
        $('#accordion').on('shown.bs.collapse', toggleChevron);
    </script>

#Collapse Panel Hide or Show

`hide`: will hide panel

`show`: will show panel

`toggle`: will change to opposite status

To use this, try `$('.class_name').collapse('toggle');` or `$('#id_name').collapse('hide')`.

#Sticky Header/Footer

Bootstrap has two classes: `navbar-fixed-top` and `navbar-fixed-bottom` that can be served as sticky header and footer. Make sure add `body{ padding-top: 50px;}` or `body{ padding-bottom: 50px;}` when you use them.

>Note: the default height for navbar in Bootstrap3 is 50px high.

#Dynamically Edit Checkbox

##Default Status

In Bootstrap3, when you add a simple check box, the default code is `<input type="checkbox" />`.

This checkbox will keep un-checked. When you check it, this default code will keep the same.

If you use `this.getAttribute('checked')` to check if checkbox is checked or not, you always get `undefined`.

##Default Checked Status

In Bootstrap3, you can set a default `checked` attribute to checkbox to make it default checked: `<input type='checkbox' checked/>`.

If you use `$(this).attr('checked')` to check status, it will return `checked` or `undefined`. But if you use `this.getAttribute("checked")`, you will always get `empty` value returned.

If you use `<input type='checkbox' checked = "checked"/>`, `$(this).attr('checked')` will return same result as above, but `this.getAttribute("checked")` will always get `checked` no matter if you check it or not.

You can also set `<input type='checkbox' checked="checked"/>` to make it default checked.

##Change Status

Following JQuery Code can divide status of checkbox if someone check or uncheck it:

    :::javascript
    $document.ready(function(){
        //You should change 'type=checkbox' based on your code. 'name' can be skipped
        $('[type=checkbox][name='checkbox_name']').on('click',function){
            if($(this).attr('checked') == undefined){
                $(this).attr("checked", "checked");
                //steps for a checked checkbox...
            }else{
                $(this).attr("checked",false);
                //steps for an un-checked checkbox...
            }
        }
    });

The usage of code above: when you check the checkbox, this default code will become `<input type='checkbox' checked='checked'>`. If you un-check it, code will change back to `<input type="checkbox" />`.

In this case, if you use `$(this).attr(checked)` or `this.getAttribute(`checked`)` to check the status of checkbox, the *un-checked* checkbox will return `undefined`. the *checked* checkbox will return `checked`.

##Check/UnCheck Checkbox Using JavaScirpt

In Bootstrap3, you can also set the `checked` attribute of checkbox to `true` or `false`.

If you use JQuery, `$(this).attr("checked",false)` will remove `checked` attribute in code.

If you use pure JavaScript, You have two steps to do this:

- `this.setAttribute("checked", true)` or `this.setAttribute("checked", "checked")` can change the *code* but not *behavior*. i.e. code will become `<input type='checkbox' checked='checked'>` or `<input type='checkbox' checked='true'>`, but on user interface, checkbox is not checked

- `this.checked="checked"` or `this.checked = true` will only change use interface. Your checkbox will be checked buy there is nothing changed in code.
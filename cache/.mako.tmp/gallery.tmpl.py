# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536926061.522872
_enable_loop = True
_template_filename = '/Users/pengyinshan/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'content', 'extra_head', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_js():
            return render_extra_js(context)
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/flowr.js"></script>\n<script>\njsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\nflowr(document.querySelectorAll("#gallery_container")[0], {\n        data : jsonContent,\n        height : ')
        __M_writer(str(thumbnail_size))
        __M_writer('*.6,\n        padding: 5,\n        rows: -1,\n        render : function(params) {\n            // Just return a div, string or a dom object, anything works fine\n            var img = document.createElement("img");\n            img.setAttribute(\'src\', params.itemData.url_thumb);\n            img.setAttribute(\'width\', params.width);\n            img.setAttribute(\'height\', params.height);\n            img.setAttribute(\'alt\', params.itemData.title);\n            img.style.maxWidth = \'100%\';\n            link = document.createElement("a");\n            link.setAttribute(\'href\', params.itemData.url);\n            link.setAttribute(\'class\', \'image-reference\');\n            div = document.createElement("div");\n            div.setAttribute(\'class\', \'image-block\');\n            div.setAttribute(\'title\', params.itemData.title);\n            div.setAttribute(\'data-toggle\', "tooltip")\n            link.append(img);\n            div.append(link);\n            //div.hover(div.tooltip());\n            return div;\n        },\n        itemWidth : function(data) { return data.size.w; },\n        itemHeight : function(data) { return data.size.h; },\n        complete : function(params) {\n            if( jsonContent.length > params.renderedItems ) {\n                nextRenderList = jsonContent.slice( params.renderedItems );\n            }\n        }\n    });\n    baguetteBox.run(\'#gallery_container\', {\n        captions: function(element) {\n            return element.getElementsByTagName(\'img\')[0].alt;\n    }});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        ui = _mako_get_namespace(context, 'ui')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i\n        class="icon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_head():
            return render_extra_head(context)
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        gallery_path = _import_ns.get('gallery_path', context.get('gallery_path', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    .image-block {\n        display: inline-block;\n    }\n    .flowr_row {\n        width: 100%;\n    }\n    </style>\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        __M_writer('<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/Users/pengyinshan/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/gallery.tmpl", "line_map": {"131": 7, "132": 8, "133": 8, "134": 9, "135": 10, "136": 10, "137": 10, "138": 12, "139": 13, "140": 14, "141": 14, "142": 17, "143": 18, "144": 19, "145": 20, "146": 20, "147": 20, "148": 21, "149": 21, "150": 23, "23": 4, "152": 27, "153": 28, "26": 3, "155": 31, "156": 31, "154": 30, "158": 31, "159": 31, "32": 0, "161": 32, "162": 32, "163": 32, "164": 34, "165": 37, "166": 38, "167": 38, "168": 38, "193": 55, "199": 60, "174": 42, "157": 31, "151": 25, "189": 43, "190": 43, "191": 53, "192": 54, "65": 2, "66": 3, "67": 4, "196": 56, "197": 56, "198": 56, "194": 56, "72": 5, "160": 32, "77": 40, "205": 5, "82": 61, "87": 105, "218": 205, "93": 63, "188": 42, "195": 56, "103": 63, "104": 66, "105": 66, "106": 69, "107": 69, "113": 7}, "uri": "gallery.tmpl"}
__M_END_METADATA
"""

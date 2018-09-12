# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536718303.056068
_enable_loop = True
_template_filename = 'themes/hpstr/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        posts = context.get('posts', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        def content_header():
            return render_content_header(context)
        comments = _mako_get_namespace(context, 'comments')
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        for post in posts:
            __M_writer('    <article class="hentry">\n    <header>\n      <div class="entry-meta">\n      <span class="entry-date date published updated">\n        <time datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('" title="')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('">')
            __M_writer(str(post.formatted_date(date_format)))
            __M_writer('</time>\n      </span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n      <span class="byline author vcard">')
            __M_writer(str(post.author()))
            __M_writer('</span>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('          &nbsp;&nbsp;&middot;&nbsp;&nbsp;<span class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('      </div>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n    </header>\n    <div class="p-summary entry-summary">\n    ')
            __M_writer(str(post.description()))
            __M_writer('\n    </div>\n    </article>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hpstr/templates/index.tmpl", "source_encoding": "utf-8", "line_map": {"128": 20, "129": 22, "130": 22, "131": 23, "132": 24, "133": 24, "134": 24, "135": 26, "136": 27, "137": 27, "138": 27, "139": 27, "140": 30, "141": 30, "142": 34, "143": 34, "144": 35, "145": 35, "146": 36, "147": 36, "23": 2, "153": 147, "26": 3, "32": 0, "51": 2, "52": 3, "53": 4, "58": 11, "63": 37, "69": 14, "80": 6, "90": 6, "91": 7, "92": 7, "93": 8, "94": 9, "95": 9, "96": 9, "102": 13, "115": 13, "120": 14, "121": 15, "122": 16, "123": 20, "124": 20, "125": 20, "126": 20, "127": 20}, "uri": "index.tmpl"}
__M_END_METADATA
"""

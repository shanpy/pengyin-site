# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536944748.84188
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
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        index_file = context.get('index_file', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        permalink = context.get('permalink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
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
        posts = context.get('posts', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
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
        def content():
            return render_content(context)
        def content_header():
            return render_content_header(context)
        helper = _mako_get_namespace(context, 'helper')
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
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
            __M_writer('</span>\n      </div>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n    </header>\n    <div class="p-summary entry-summary">\n    ')
            __M_writer(str(post.description()))
            __M_writer('.\n    </div>\n    </article>\n')
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
{"uri": "index.tmpl", "filename": "themes/hpstr/templates/index.tmpl", "line_map": {"128": 22, "129": 24, "130": 24, "131": 24, "68": 14, "133": 27, "134": 27, "135": 31, "136": 31, "137": 32, "138": 32, "132": 24, "140": 33, "79": 6, "146": 140, "90": 7, "122": 20, "23": 2, "89": 6, "26": 3, "91": 7, "92": 8, "93": 9, "94": 9, "95": 9, "32": 0, "139": 33, "101": 13, "113": 13, "50": 2, "51": 3, "52": 4, "126": 20, "118": 14, "119": 15, "120": 16, "57": 11, "121": 20, "123": 20, "124": 20, "125": 20, "62": 34, "127": 22}, "source_encoding": "utf-8"}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536718564.322987
_enable_loop = True
_template_filename = 'themes/hpstr/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translation_header', 'html_navigation_links', 'html_site_title', 'html_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="dl-menu" class="dl-menuwrapper" role="navigation">\n    <button class="dl-trigger">Open Menu</button>\n    <ul class="dl-menu">\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li>\n                <a href="#">')
                __M_writer(str(text))
                __M_writer('</a>\n                <ul class="dl-submenu">\n')
                for suburl, text in url:
                    __M_writer('                    <li><a href="')
                    __M_writer(str(suburl))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
                __M_writer('                </ul>\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n  <div class="header-title">\n    <div class="header-title-wrap">\n    <h1 id="brand"><a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('" rel="home">\n    ')
        __M_writer(str(blog_title))
        __M_writer('</a></h1>\n      <h2>')
        __M_writer(str(blog_description))
        __M_writer('</h2>\n    </div><!-- /.header-title-wrap -->\n  </div><!-- /.header-title -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n<div class="entry-header">\n<!-- /.image-credit -->\n    <div class="entry-image">\n      <img src="/bk.JPG" alt="Latest Posts">\n    </div><!-- /.entry-image -->\n      ')
        __M_writer(str(html_site_title()))
        __M_writer('\n</div><!-- /.entry-header -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "base_header.tmpl", "line_map": {"130": 4, "140": 4, "141": 5, "142": 5, "143": 11, "144": 11, "150": 144, "23": 2, "26": 0, "33": 2, "34": 13, "35": 23, "36": 46, "37": 55, "43": 48, "53": 48, "54": 49, "55": 50, "56": 51, "57": 51, "58": 52, "59": 52, "65": 25, "76": 25, "77": 29, "78": 30, "79": 31, "80": 32, "81": 32, "82": 34, "83": 35, "84": 35, "85": 35, "86": 35, "87": 35, "88": 37, "89": 38, "90": 39, "91": 39, "92": 39, "93": 39, "94": 39, "95": 42, "96": 42, "97": 42, "98": 43, "99": 43, "105": 15, "116": 15, "117": 18, "118": 18, "119": 18, "120": 18, "121": 19, "122": 19, "123": 20, "124": 20}, "filename": "themes/hpstr/templates/base_header.tmpl"}
__M_END_METADATA
"""

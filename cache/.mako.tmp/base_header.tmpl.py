# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1543344743.183066
_enable_loop = True
_template_filename = 'themes/hpstr/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_translation_header', 'html_navigation_links', 'html_site_title']


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
        __M_writer('\n<div class="entry-header">\n<!-- /.image-credit -->\n    <div class="entry-image">\n      <img src="/images/bk.jpg" alt="Latest Posts">\n    </div><!-- /.entry-image -->\n      ')
        __M_writer(str(html_site_title()))
        __M_writer('\n</div><!-- /.entry-header -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
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
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
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
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
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


"""
__M_BEGIN_METADATA
{"uri": "base_header.tmpl", "line_map": {"136": 15, "137": 18, "138": 18, "139": 18, "140": 18, "141": 19, "142": 19, "143": 20, "144": 20, "150": 144, "23": 2, "26": 0, "33": 2, "34": 13, "35": 23, "36": 46, "37": 55, "43": 4, "53": 4, "54": 5, "55": 5, "56": 11, "57": 11, "63": 48, "73": 48, "74": 49, "75": 50, "76": 51, "77": 51, "78": 52, "79": 52, "85": 25, "96": 25, "97": 29, "98": 30, "99": 31, "100": 32, "101": 32, "102": 34, "103": 35, "104": 35, "105": 35, "106": 35, "107": 35, "108": 37, "109": 38, "110": 39, "111": 39, "112": 39, "113": 39, "114": 39, "115": 42, "116": 42, "117": 42, "118": 43, "119": 43, "125": 15}, "source_encoding": "utf-8", "filename": "themes/hpstr/templates/base_header.tmpl"}
__M_END_METADATA
"""

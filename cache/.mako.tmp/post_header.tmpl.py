# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536926062.286516
_enable_loop = True
_template_filename = 'themes/hpstr/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_post_header', 'html_sourcelink', 'html_translations', 'html_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        helper = _mako_get_namespace(context, 'helper')
        def html_translations(post):
            return render_html_translations(context,post)
        date_format = context.get('date_format', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def html_title():
            return render_html_title(context)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        <div class="entry-meta">\n            <span class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time></a></span>\n            <span class="byline author vcard">')
        __M_writer(str(post.author()))
        __M_writer('</span>\n')
        if post.meta('link'):
            __M_writer("                    <span><a href='")
            __M_writer(str(post.meta('link')))
            __M_writer("'>")
            __M_writer(str(messages("Original site")))
            __M_writer('</a></span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        if post.description():
            __M_writer('                <meta name="description" itemprop="description" content="')
            __M_writer(str(post.description()))
            __M_writer('">\n')
        __M_writer('            <span>')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('</span>\n            <span style="font-style: italic;">')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('</span>\n        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(html_title()))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <span class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "themes/hpstr/templates/post_header.tmpl", "line_map": {"128": 17, "129": 17, "130": 17, "131": 17, "132": 17, "133": 20, "139": 5, "145": 5, "146": 6, "147": 7, "148": 7, "149": 7, "150": 7, "23": 3, "26": 2, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 47, "45": 30, "157": 151, "57": 30, "58": 33, "59": 33, "60": 33, "61": 33, "62": 33, "63": 33, "64": 33, "65": 33, "66": 34, "67": 34, "68": 35, "69": 36, "70": 36, "71": 36, "72": 36, "73": 36, "74": 38, "75": 39, "76": 39, "77": 39, "78": 41, "79": 41, "80": 41, "81": 42, "82": 42, "83": 44, "84": 44, "85": 45, "86": 45, "92": 24, "151": 7, "99": 24, "100": 25, "101": 26, "102": 26, "103": 26, "104": 26, "105": 26, "111": 11, "119": 11, "120": 12, "121": 13, "122": 14, "123": 14, "124": 15, "125": 16, "126": 17, "127": 17}, "uri": "post_header.tmpl"}
__M_END_METADATA
"""

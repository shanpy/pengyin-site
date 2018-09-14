# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536942553.067694
_enable_loop = True
_template_filename = 'themes/hpstr/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_sourcelink', 'html_title', 'html_post_header', 'html_translations']


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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
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


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
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


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_translations(post):
            return render_html_translations(context,post)
        date_format = context.get('date_format', UNDEFINED)
        def html_title():
            return render_html_title(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
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
        __M_writer('            <span>')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('</span>\n            <span style="font-style: italic;">')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('</span>\n        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(html_title()))
        __M_writer('\n    <p>')
        __M_writer(str(post.description()))
        __M_writer('.</p>\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "themes/hpstr/templates/post_header.tmpl", "uri": "post_header.tmpl", "line_map": {"135": 11, "136": 12, "137": 13, "138": 14, "139": 14, "140": 15, "141": 16, "142": 17, "143": 17, "144": 17, "145": 17, "146": 17, "147": 17, "148": 17, "149": 20, "23": 3, "26": 2, "155": 149, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 45, "45": 24, "52": 24, "53": 25, "54": 26, "55": 26, "56": 26, "57": 26, "58": 26, "64": 5, "70": 5, "71": 6, "72": 7, "73": 7, "74": 7, "75": 7, "76": 7, "82": 30, "94": 30, "95": 33, "96": 33, "97": 33, "98": 33, "99": 33, "100": 33, "101": 33, "102": 33, "103": 34, "104": 34, "105": 35, "106": 36, "107": 36, "108": 36, "109": 36, "110": 36, "111": 38, "112": 38, "113": 38, "114": 39, "115": 39, "116": 41, "117": 41, "118": 42, "119": 42, "120": 43, "121": 43, "127": 11}}
__M_END_METADATA
"""

# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536718302.720638
_enable_loop = True
_template_filename = 'themes/hpstr/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_sourcelink', 'html_post_header', 'html_title', 'html_translations']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

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


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        messages = context.get('messages', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def html_title():
            return render_html_title(context)
        comments = _mako_get_namespace(context, 'comments')
        def html_translations(post):
            return render_html_translations(context,post)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n        <div class="entry-meta">\n            <span class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time></a></span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n            <span class="byline author vcard">')
        __M_writer(str(post.author()))
        __M_writer('</span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <span class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('</span>&nbsp;&nbsp;&middot;&nbsp;&nbsp;\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
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
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(html_title()))
        __M_writer('\n    </header>\n')
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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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
{"filename": "themes/hpstr/templates/post_header.tmpl", "source_encoding": "utf-8", "line_map": {"128": 7, "129": 7, "135": 11, "151": 17, "143": 11, "144": 12, "145": 13, "146": 14, "147": 14, "148": 15, "149": 16, "150": 17, "23": 2, "152": 17, "153": 17, "26": 3, "155": 17, "156": 17, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 49, "154": 17, "45": 24, "157": 20, "163": 157, "52": 24, "53": 25, "54": 26, "55": 26, "56": 26, "57": 26, "58": 26, "64": 30, "79": 30, "80": 33, "81": 33, "82": 33, "83": 33, "84": 33, "85": 33, "86": 33, "87": 33, "88": 34, "89": 34, "90": 35, "91": 36, "92": 36, "93": 36, "94": 38, "95": 38, "96": 38, "97": 39, "98": 40, "99": 40, "100": 40, "101": 40, "102": 40, "103": 42, "104": 43, "105": 43, "106": 43, "107": 45, "108": 46, "109": 46, "110": 47, "111": 47, "117": 5, "123": 5, "124": 6, "125": 7, "126": 7, "127": 7}, "uri": "post_header.tmpl"}
__M_END_METADATA
"""

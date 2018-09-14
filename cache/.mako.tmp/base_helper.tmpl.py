# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1536944748.53938
_enable_loop = True
_template_filename = 'themes/hpstr/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'late_load_js', 'html_feedlinks', 'html_headstart', 'html_stylesheets']


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


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="/assets/js/scripts.min.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        description = context.get('description', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        title = context.get('title', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        striphtml = context.get('striphtml', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<!--[if lt IE 7]><html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->\n<!--[if (IE 7)&!(IEMobile)]><html class="no-js lt-ie9 lt-ie8" lang="en"><![endif]-->\n<!--[if (IE 8)&!(IEMobile)]><html class="no-js lt-ie9" lang="en"><![endif]-->\n<!--[if gt IE 8]><!--> <html class="no-js" lang="en"><!--<![endif]-->\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <!-- http://t.co/dKP3o1e -->\n    <meta name="HandheldFriendly" content="True">\n    <meta name="MobileOptimized" content="320">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <!-- Load Modernizr -->\n    <script src="//mmistakes.github.io/hpstr-jekyll-theme/assets/js/vendor/modernizr-2.6.2.custom.min.js"></script>\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            __M_writer('        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/main.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/extra.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        __M_writer('\n    <!-- Webfonts -->\n    <link href="//fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "filename": "themes/hpstr/templates/base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 71, "23": 76, "24": 93, "25": 116, "26": 126, "32": 118, "41": 118, "42": 120, "43": 121, "44": 122, "45": 122, "46": 122, "47": 122, "48": 122, "49": 122, "50": 122, "51": 125, "57": 73, "61": 73, "67": 95, "77": 95, "78": 96, "79": 97, "80": 97, "81": 97, "82": 98, "83": 99, "84": 100, "85": 101, "86": 101, "87": 101, "88": 101, "89": 101, "90": 103, "91": 104, "92": 104, "93": 104, "94": 107, "95": 108, "96": 109, "97": 110, "98": 110, "99": 110, "100": 110, "101": 110, "102": 112, "103": 113, "104": 113, "105": 113, "111": 3, "138": 3, "139": 6, "140": 7, "141": 8, "142": 10, "143": 11, "144": 13, "145": 14, "146": 15, "147": 17, "148": 18, "149": 21, "150": 21, "151": 21, "152": 28, "153": 29, "154": 29, "155": 29, "156": 31, "157": 35, "158": 35, "159": 35, "160": 35, "161": 38, "162": 38, "163": 41, "164": 41, "165": 42, "166": 43, "167": 43, "168": 43, "169": 45, "170": 46, "171": 47, "172": 48, "173": 48, "174": 48, "175": 48, "176": 48, "177": 48, "178": 48, "179": 51, "180": 52, "181": 53, "182": 53, "183": 53, "184": 55, "185": 56, "186": 57, "187": 57, "188": 57, "189": 59, "190": 60, "191": 60, "192": 60, "193": 62, "194": 63, "195": 63, "196": 64, "197": 65, "198": 66, "199": 67, "200": 67, "201": 67, "202": 69, "203": 70, "204": 70, "210": 78, "216": 78, "217": 79, "218": 80, "219": 81, "220": 82, "221": 86, "222": 87, "223": 90, "229": 223}, "source_encoding": "utf-8"}
__M_END_METADATA
"""

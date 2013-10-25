import sublime, sublime_plugin
import re

def match(rex, str):
    m = rex.match(str)
    if m:
        return m.group(0)
    else:
        return None

# This responds to on_query_completions, but conceptually it's expanding
# expressions, rather than completing words.
#
# It expands these simple expressions:
# tag.class
# tag#id
class HtmlCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0],
                "text.html - source - meta.tag, punctuation.definition.tag.begin"):
            return []

        # Get the contents of each line, from the beginning of the line to
        # each point
        lines = [view.substr(sublime.Region(view.line(l).a, l))
            for l in locations]

        # Reverse the contents of each line, to simulate having the regex
        # match backwards
        lines = [l[::-1] for l in lines]

        # Check the first location looks like an expression
        rex = re.compile("([\w-]+)([.#])(\w+)")
        expr = match(rex, lines[0])
        if not expr:
            return []

        # Ensure that all other lines have identical expressions
        for i in xrange(1, len(lines)):
            ex = match(rex, lines[i])
            if ex != expr:
                return []

        # Return the completions
        arg, op, tag = rex.match(expr).groups()

        arg = arg[::-1]
        tag = tag[::-1]
        expr = expr[::-1]

        if op == '.':
            snippet = "<{0} class=\"{1}\">$1</{0}>$0".format(tag, arg)
        else:
            snippet = "<{0} id=\"{1}\">$1</{0}>$0".format(tag, arg)

        return [(expr, snippet)]


# Provide completions that match just after typing an opening angle bracket
class TagCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within ISML
        if not view.match_selector(locations[0],
                "text.isml - source"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '<':
            return []

        return ([
            ("isif\tTag", "isif condition=\"\${$1}\">\n$0\n</isif>"),
            ("isloop\tTag", "isloop items=\"\${$1}\" var=\"$2\">\n\t$0\n</isloop>"),
            ("iscomment\tTag", "iscomment>$1</iscomment>"),
            ("isscript\tTag", "isscript>\n\t$0\n</isscript>"),
            ("isset\tTag", "isset name=\"$1\" value=\"\${$2}\" scope=\"${3:page}\" />"),
            ("isbreak\tTag", "isbreak />"),
            ("iscontinue\tTag", "iscontinue/>"),
            ("iscache\tTag", "iscache type=\"${1:relative|daily}\"${2: status=\"on\" varyby=\"price_promotion\"}/>"),
            ("iscontent\tTag", "iscontent type=\"${1:text/html}\" charset=\"${2:utf-8}\" encoding=\"${3:on|off|html|xml|wml}\" compact=\"true\"/>"),
            ("isdecorate\tTag", "isdecorate template=\"${1:path/to/template}\">\n\t$0\n</isdecorate>"),
            ("isinclude\tTag", "isinclude${1: template=\"$2\"}${3: url=\"\\${URLUtils.url('$4')\\}\"}/>"),
            ("iselse\tTag", "iselse/>"),
            ("iselseif\tTag", "iselseif condition=\"\\${$1}\">\n\t$0\n</iselseif>\n<iselse/>")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

# Demandware.sublime-package #

A package for Sublime Text that provides syntaxes for ISML and Demandware Script. Supported functionality is outlined below.

## ISML Tag Tab-completion ##

* `isloop`
* `isif`
* `isscript`
* `isset`
* `isbreak`
* `iscontinue`
* `iscache`
* `iscontent`
* `isdecorate`
* `isinclude`
* `iselse`
* `iselseif`

## Demandware Script Syntax Embedding ##

The package supports Demandware Script embedded within `.isml` files. The code is colored
with one exception. (see "Theme Modifications" section)

* Within "MoneySquiggles" notation eg: `${product.ID}`
* Within `<isscript>` tags eg: `<isscript>importScript('util/myCoolHelper.ds');</isscript>`

## Theme Modifications ##

*Note* theme modification is only required if you desire code within quotes to be colorized. eg:

    <isset name="customer" value="${pdict.CurrentCustomer.profile}" scope="page" />

Code within `<isscript></isscript>` tags will be colorized normally. The one theme addition
I do recommend is the first rule which sets foreground/background color for
`source.dwscript.embedded`.

The following JSON illustrates some example additions to the theme of your choice. (then built into a .tmTheme ala [AAAPackageDev][] ) in
order to fully support the embedded Demandware Script syntax. Feel free to change the hex
colors and settings for each item. This was just what I felt worked well with the default
'Sunburst' theme.

	,
    {
        "name": "Embedded Demandware Script",
        "scope": "source.dwscript.embedded, source.dwscript.embedded.isml",
        "settings": {
            "background": "#1d1d1d",
            "foreground": "#afafaf"
        }
    },
    {
        "name": "Embedded Demandware Script String",
        "scope": "source.dwscript.embedded string",
        "settings": {
            "foreground": "#5faa5f"
        }
    },
    {
        "name": "Embedded Demandware Script Function",
        "scope": "source.dwscript.embedded function, source.dwscript.embedded variable, source.dwscript.embedded method",
        "settings": {"foreground": "#6b9bd2"}
    },
    {
        "name": "Embedded Demandware Script Markers",
        "scope": "source.dwscript.marker",
        "settings": {
            "foreground": "#ffffff"
        }
    },
    {
        "name": "Embedded Demandware Script Control Chars",
        "scope": "source.dwscript.embedded entity",
        "settings": {
            "foreground": "#ffffff"
        }
    },
    {
        "name": "Entity",
        "scope": "source.dwscript.embedded entity.name.tag.dwscript, punctuation.definition.tag.isml",
        "settings": {
            "fontStyle": "",
            "foreground": "#89BDFF"
        }
    }

## Contributing ##

I welcome contributors. If you feel something needs to be added or fixed then please create an issue for it. If you want to fix an issue then fork the repository, fix it, and submit a pull request. If you have something you'd like to contribute please fork the repository, commit your contribution, and submit a pull request.


[AAAPackageDev]: http://github.com/SublimeText/AAAPackageDev
# Demandware.sublime-package #

A package for Sublime Text that provides syntaxes for ISML and Demandware Script. Supported functionality is outlined below.

## ISML Tag Tab-completion ##

* `isset`
* `isscript`
* `isloop`
* `isif`

## Demandware Script Syntax Embedding ##

The package supports Demandware Script embedded within `.isml` files. The code is colored if you have the theme modifications in place. (see "Theme Modifications" section)

* Within "MoneySquiggles" notation eg: `${product.ID}`
* Within `<isscript>` tags eg: `<isscript>importScript('util/myCoolHelper.ds');</isscript>`

## Theme Modifications ##

The following JSON needs to be added to your theme of choice. (then built into a .tmTheme) in order to fully support the embedded Demandware Script syntax. Feel free to change the hex colors and settings for each item. This was just what worked well with the default 'Sunburst' theme.

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
    }
# Demandware.sublime-package #

A package for Sublime Text that provides syntaxes for ISML and Demandware Script. Supported functionality is outlined below.

## Features ##

### ISML Tag Tab-completion ###

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

### Demandware Script Syntax Embedding ###

The package supports Demandware Script embedded within `.isml` files. The code is colored
with one exception. (see "Theme Modifications" section)

* Within "MoneySquiggles" notation eg: `${product.ID}`
* Within `<isscript>` tags eg: `<isscript>importScript('util/myCoolHelper.ds');</isscript>`

## Compatability ##

This plugin has been tested with Sublime Text 2 and Sublime Text 3 beta.

## Installation ##

*Note: If you have Package Control installed skip to the section called "Installing with Package Control (Recommended)".*

The basic installation is pretty simple. Note you need to replace <kbd>&lt;InsertVersionNumberHere&gt;</kbd> with either <kbd>2</kbd> or <kbd>3</kbd> depending on the version of Sublime Text you use.

```
# For OSX
$ git clone https://github.com/sholsinger/Demandware.git \
  ~/Library/Application\ Support/Sublime\ Text\ <InsertVersionNumberHere>/Packages/Demandware
```
```
# For Windows
C:\ git clone https://github.com/sholsinger/Demandware.git %APPDATA%\Sublime Text <InsertVersionNumberHere>\Demandware
```
```
# For Linux/Unix
$ git clone https://github.com/sholsinger/Demandware.git ~/.Sublime\ Text\ <InsertVersionNumberhere>\Demandware
```

You may need to restart Sublime Text in order for the plugin to automatically colorize the right files.

To update the package you can simply <kbd>cd</kbd> into the package directory and run <kbd>git pull</kbd>.

### Installing with Package Control (Recommended) ###

1. Type <kbd>Cmd+Shift+P</kbd> on a Mac or <kbd>Ctrl+Shift+P</kbd> on Windows/Linux and type <kbd>Package Control</kbd>.
2. Select the "Package Control: Add Repository" option.
3. When prompted paste in the following url:
  ```
  https://github.com/sholsinger/Demandware.git
  ```

Updates are handled using the "Package Control: Upgrade Package" command.

### Theme Modifications ###

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

## Roadmap ##

Ultimately my goal is to be able to do 90% of my Demandware development without Eclipse running. My secondary goal with the project is to provide an alternative editor option to all Demandware developers. To that end the following features are on the roadmap:

* WebDAV upload on change
* Full WebDAV upload command
* Modifications to the repo for submission to Package Manager

## Contributing ##

I welcome contributors. If you feel something needs to be added or fixed then please create an issue for it. If you want to fix an issue then fork the repository, fix it, and submit a pull request. If you have something you'd like to contribute please fork the repository, commit your contribution, and submit a pull request.


[AAAPackageDev]: http://github.com/SublimeText/AAAPackageDev

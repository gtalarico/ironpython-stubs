# IronPython Stubs

Stubs for common IronPython CLR assemblies.

These stubs are intended to be used by the autocomplete engine of editors like Atom, Sublime, and Visual Studio Code.


Demo

![autocomplete-demo](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-demo.gif)


#### Get this Repository

1. Clone this repository using git _or_ download it from [here](https://github.com/gtalarico/ironpython-stubs/archive/master.zip) and unzip it.

#### Configure your Editor

* [Atom](https://github.com/gtalarico/ironpython-stubs/blob/dev/main/docs/atom.md)
* [Visual Studio Code](https://github.com/gtalarico/ironpython-stubs/blob/dev/main/docs/vscode.md)
* [Sublime](https://github.com/gtalarico/ironpython-stubs/blob/dev/main/docs/sublime.md)

----------------------------------------------------------------------

If you haven't yet, read *Note on Performance* above.
Large Namespaces such as `Autodesk.Revit.DB` do not show up right away

#### More Examples

clr

![autocomplete-clr](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-clr.gif)

autodesk

![autocomplete-clr](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-autodesk.gif)

rhino

![autocomplete-clr](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-rhino.gif)


## Known Issues
* Performance is not great for some of the larger classes. If you know how this can be improved please let me know.
* Some of the function/constructor signatures are missing or incorrect. This is a problem with Generator3. Please send a PR or let me know if you have a fix.
* Overloaded Methods do not show correct arguments


## Credits

This project is a fork of the repository started by Gary Edwards on [Gitlab](https://gitlab.com/reje/revit-python-stubs).
Thank you for your work Gary - and thank you [Ehsan](https://github.com/eirannejad) for pointing me to it.

It uses PyCharm's [Generator3](https://github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py)
to create the stubs.


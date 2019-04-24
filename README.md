# IronPython Stubs

Stubs for common IronPython CLR assemblies.
These stubs are intended to be used by the autocomplete engine of editors like Atom, Sublime, and Visual Studio Code.

## Why IronPython Stubs?

If your are writing python code that targets IronPython, and using modules loaded through the Common Language Runtime (clr),
your editor's autocomplete engine (which runs on regular python) will not be able to access those non-native modules.
In other words, modules/or packages loaded through `clr.AddReference()` are not available on your autocomplete engine.

The workaround here is simple: Use IronPython to crawl through these libraries,
and create 'stubs' or ['mock objects'](https://en.wikipedia.org/wiki/Mock_object).
These 'stubs' can then be used by the CPython autocomplete engine.
The stubs include doc strings as well as constructor/function/method signatures.

This repository contains the code to create these stubs, and also stores an
a version of them that can be used by autocomplete-python.

![sublime-large-demo](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/sublime/sublime-demo-large.gif)

------------------------------------

# Documentation

[Wiki](https://github.com/gtalarico/ironpython-stubs/wiki)

The [wiki](https://github.com/gtalarico/ironpython-stubs/wiki) has step-by-step instructions for setting up your stubs for Atom, Sublime, Vim, Visual Studio Code.

For a list of supported Assemblies, see [this list](https://github.com/gtalarico/ironpython-stubs/tree/master/logs)

If you haven't yet, read [Note on Performance](https://github.com/gtalarico/ironpython-stubs/wiki/A-Note-on-Performance)
Large Namespaces such as `Autodesk.Revit.DB` can take a long time to be parsed and cached and might not show up right away.

------------------------------------

# Contribute - WIP

### Generate Stubs - Examples
`ipy -m ironstubs make RhinoCommon`
`ipy -m ironstubs make --all`
`ipy -m ironstubs make DSCoreNodes --folder="DSCore" --directory="C:/Program Files/Dynamo/Dynamo Core/1.3"`
### Process Stubs
WIP

### Known Issues
* Performance is not great for some of the larger classes. If you know how this can be improved please let me know.
* Some of the function/constructor signatures are missing or incorrect. This is a problem with Generator3. Please send a PR or let me know if you have a fix.
* Overloaded Methods do not show correct arguments

### Credits
This project is a fork of the repository started by Gary Edwards on [Gitlab](https://gitlab.com/reje/revit-python-stubs).
Thank you for your work Gary - and thank you [Ehsan](https://github.com/eirannejad) for pointing me to it.

It uses PyCharm's [Generator3](https://github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py)
to create the stubs.


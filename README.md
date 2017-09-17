# IronPython Stubs

Stubs for common IronPython CLR assemblies.

These stubs are intended to be used with [Atom](https://atom.io/) +
[autocomplete-python](https://atom.io/packages/autocomplete-python) package.

The goal of this project is to develop, consolidate + optimize IronPython stubs,
and to provide instructions for how to use them in Atom.

Demo

![autocomplete-demo](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-demo.gif)

## Credits

This project is a fork of the repository started by Gary Edwards on [Gitlab](https://gitlab.com/reje/revit-python-stubs).
Thank you for your work Gary - and thank you [Ehsan](https://github.com/eirannejad) for pointing me to it.

It uses PyCharm's [Generator3](https://github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py)
to create the stubs.


--------------------------------------------------------------------------------

## Background

Autocomplete for Python can be quite good and easy to use in an editor like Atom.

The problem comes when you are using IronPython with modules loaded through the
Common Language Runtime (clr); the autocomplete engine runs regular python,
and regular python cannot access those non-native modules.

The strategy here is simple: Use IronPython to crawl through these libraries,
and create 'stubs' or ['mock object'](https://en.wikipedia.org/wiki/Mock_object)
Those 'stubs' can then be used by an autocomplete engine.

This repository contains the code to create the stubs, and also stores an
optimized version of them that can be used by autocomplete-python.


## A Note on Performance

Behind the scenes, Atom + autocomplete-python use [Jedi](https://jedi.readthedocs.io/en/latest/)
to analyze your code and the libraries you are using.
The work Jedi's does can be quite _expensive_. Make sure your computer has plenty of RAM and CPU power.

Once you are setup, the Autocomplete will be a bit slow at first, but it should get better as you use it
and the engine caches the results and indexes the libraries. Jedi's index is saved here:
`C:\Users\{username}\AppData\Roaming\Jedi\Jedi\{python-version}`

The index can get _very_ large - hundreds of MB up to a few Gigs.
That's an issue with the Jedi Autocomplete engine and beyond the scope of this project.

Lastly, some of the stub files created were too large for Jedi to handle (Memory Errors as ram usage spiked up to +10GB).
To get it work smoothly, this project includes an optimized version of the stubs.
This version is the folder called  `stubs.min`. I highly recommend you use this version as well.

For more information on the 'optimization' see the `proces_stubs.py` file.

## How to Use the Stubs

#### Get this Repository

1. Clone this repository using git _or_ download it from [here](https://github.com/gtalarico/ironpython-stubs/archive/master.zip) and unzip it.

#### Configure your Editor

* [Atom](https://github.com/gtalarico/ironpython-stubs/blob/dev/main/docs/atom.md)
* [Visual Studio Code](https://github.com/gtalarico/ironpython-stubs/blob/dev/main/docs/vscode.md)
* [Sublime](https://github.com/gtalarico/ironpython-stubs/blob/dev/main/docs/sublime.md)


----------------------------------------------------------------------

That should be it. Should work like in the images below.

If you haven't yet, read *Note on Performance* above.
Large Namespaces such as `Autodesk.Revit.DB` do not show up right away
The first time you use them could take  5-10 secondes for options to appear.
After the first time, should be quicker (~1 sec.)

#### Examples

clr

![autocomplete-clr](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-clr.gif)

autodesk

![autocomplete-clr](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-autodesk.gif)

rhino

![autocomplete-clr](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-rhino.gif)


## For Visual Code

You should also be able to use these stubs in Visual Studio Code:

1. Install the [Python Package](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python)
2. Follow the instruction on [the repository](https://github.com/DonJayamanne/pythonVSCode) to set the autocomplete `extraPaths`:

```
"python.autoComplete.extraPaths": ["C:\Path\To\ironpython-stubs\stubs.min"]
```

![vscode](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/vscode.gif)

## Building your Own Stubs

`ipy make_stubs.py`
`ipy make_stubs.py`

## Known Issues
* Performance is not great for some of the larger classes. If you know how this can be improved please let me know.
* Some of the function/constructor signatures are missing or incorrect. This is a problem with Generator3. Please send a PR or let me know if you have a fix.

## Unknown Issues
* Many, probably!

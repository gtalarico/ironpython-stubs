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

## Getting Started

#### Setup Atom

1. If you haven't yet, install Atom + [autocomplete-python](https://atom.io/packages/autocomplete-python)
   (When asked if you want to use Kite or Local Engine, pick local engine)
2. Make sure you have no other autocomplete engine on.
3. At this point, you should make sure you have the autocomplete engine working
   for the native Python libraries. If it's not I recommend you start with a fresh install of atom and go back to step #1.

   Autocomplete Working for Native Libraries.
   ![autocomplete-builtinlibs](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-builtinlibs.gif)


#### Get this Repository

1. Clone this repository using git _or_ download it from [here](https://github.com/gtalarico/ironpython-stubs/archive/master.zip) and unzip it.

#### Configure the autocomplete engine

1. Go to your Atom Settings > Packages > autocomplete-python
2. In the package's settings page, we will need to configure the following settings:

First the less important settings:

* [X] Show Descriptions: ON - Recommended Option
* [X] Case Insensitive: ON - Recommended Option
* [X] Fuzzy Matches: ON - Recommended Option
* [required] Autocomplete Function Parameters - Recommended Option

Now to the ones that matter:

* [ ] Use Kite-powered Completion: OFF - Recommended.

* [X] Output Provider Errors: ON - This will tell you if Jedi runs out of memory.


* Python Executable Path

You can leave blank, or type in the path to your system's python, for example: `C:/Python35/python.exe`
If blank, Atom will automatically use your default system's python.
The only thing to be mindful is that you should probably make sure you are running a 64 bit version.
The 32-bit version is limited to 2GB and will likely not be enough for Jedi.
The system version is displayed when you launch python:
   `Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)` < 64 bit

* Extra Paths for Packages
This is the most important setting. This tells the autocomplete engine where to "crawl" to find the stub files.
`C:\Path\To\ironpython-stubs\stubs.min`

If you have other libraries you would like to add like [rpw](), you add multiple paths using a semicolon.
`C:\Path\To\ironpython-stubs\stubs.min` `;` `C:\Path\To\revitpythonwrapper.lib`

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

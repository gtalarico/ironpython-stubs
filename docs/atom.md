# Atom

1. If you haven't yet, install Atom + [autocomplete-python](https://atom.io/packages/autocomplete-python)
   (When asked if you want to use Kite or Local Engine, pick local engine)
2. Make sure you have no other autocomplete engine on.
3. At this point, you should make sure you have the autocomplete engine working
   for the native Python libraries. If it's not I recommend you start with a fresh install of atom and go back to step #1.

   Autocomplete Working for Native Libraries.
   ![autocomplete-builtinlibs](https://github.com/gtalarico/ironpython-stubs/blob/master/docs/gifs/autocomplete-builtinlibs.gif)


#### Configure the autocomplete engine

1. Go to your Atom Settings > Packages > autocomplete-python
2. In the package's settings page, we will need to configure the following settings:

#### First the less important settings:

* [X] Show Descriptions: ON - Recommended Option
* [X] Case Insensitive: ON - Recommended Option
* [X] Fuzzy Matches: ON - Recommended Option
* [required] Autocomplete Function Parameters - Recommended Option

#### Now to the ones that matter:

* [ ] Use Kite-powered Completion: OFF - Recommended.
* [X] Output Provider Errors: ON - This will tell you if Jedi runs out of memory.

##### Extra Paths for Packages
This is the most important setting. This tells the autocomplete engine where to "crawl" to find the stub files.
`C:\Path\To\ironpython-stubs\stubs.min`

If you have other libraries you would like to add like [rpw](revitpythonwrapper.readthedocs.io/en/latest/),
you cab add multiple paths using a semicolon.
`C:\Path\To\ironpython-stubs\stubs.min` `;` `C:\Path\To\revitpythonwrapper.lib`

#### Python Executable Path
You can leave blank, or type in the path to your system's python, for example: `C:/Python35/python.exe`
If blank, Atom will automatically use your default system's python.
The only thing to be mindful is that you should probably make sure you are running a 64 bit version.
The 32-bit version is limited to 2GB and sometimes is not enough for Jedi.
The system version is displayed when you launch python:
`Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)` < 64 bit

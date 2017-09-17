# Sublime

1. Make sure the Jedi Package is installed.
2. Make sure autocompletion is working for your default python packages:



2. Configure Jedi's settings:

```
{
    "python_package_paths": [
    						 "C:\\Path\\To\\ironpython-stubs\\stubs.min"
    						],
    "sublime_completions_visibility": "default",
    "auto_complete_function_params": "required",
    "logging_level": "warn",
}
```

### Troubleshooting


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

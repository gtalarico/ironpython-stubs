""" Stub Generator for IronPython

Extended script based on script developed by Gary Edwards at:
gitlab.com/reje/revit-python-stubs

This is uses a slightly modify version of generator3,
github.com/JetBrains/intellij-community/blob/master/python/helpers/generator3.py

Iterates through a list of targeted assemblies and generates stub directories
for the namespaces using pycharm's generator3.

Note:
    Some files ended up too large for Jedi to handle and would cause
    memory errors and crashes - 1mb+ in a single files was enough to
    cause problems. To fix this, there is a separate module that creates
    a compressed version of the stubs, but it also split large file
    into separate files to deal with jedi.
    These directories will show up in the stubs as (X_parts)


MIT LICENSE
https://github.com/gtalarico/ironpython-stubs
Gui Talarico
"""

import sys
import os
import json
from pprint import pprint

STUBS_FOLDER = 'stubs2'
DUMP_JSON = True
OVERWRITE = True

# Setp Dir First
PKG_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(PKG_DIR)
release_dir = os.path.join(PROJECT_DIR, 'release', STUBS_FOLDER)
os.chdir(PROJECT_DIR)

from utils.logger import logger
from utils.helper import Timer
from default_settings import PATHS, REVIT_ASSEMBLIES
from make_stubs import make, dump_json_log

# Add Paths
PATHS.append(os.path.join(PROJECT_DIR, 'bin'))
[sys.path.append(p) for p in PATHS]

timer = Timer()
for assembly_name in REVIT_ASSEMBLIES:
    assembly_dict = make(release_dir, assembly_name,
                         overwrite=OVERWRITE,
                         quiet=True)
    if DUMP_JSON:
        dump_json_log(assembly_dict)
print('Done: {} seconds'.format(timer.stop()))

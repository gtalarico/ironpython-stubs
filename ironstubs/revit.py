"""
MIT LICENSE
https://github.com/gtalarico/ironpython-stubs
Gui Talarico

-----------------------------------------------------------------

This file is intented to be executer from withing Revit.
Takes about 3 min

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

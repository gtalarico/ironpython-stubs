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

from utils.docopt import docopt
from utils.logger import logger
from utils.helper import Timer
from default_settings import PATHS, BUILTINS, ASSEMBLIES
from make_stubs import make, dump_json_log

__version__ = '1.0.0'
__doc__ = """
    IronPython-Stubs | {version}

    IronPython Stubs Generator

    Usage:
      ironstubs --help
      ironstubs make (<assembly-name>|--all) [options]

    Examples:
      ipy -m ironstubs RhinoCommon --overwrite

    Options:
        <assembly-name>         Name of Dll Assembly to load
        --all                   Process all Assemblies in the default_settings.py

        --folder=<dir>          Name of Output Directory [default: {out_dir}]
        --directory=<dir>       Additional Directory to add to Path [default: ]
        --overwrite             Force Overwrite if stub already exists [default: False].
        --no-json               Disables Json Log
        --debug                 Enables Debug Messages
        -h, --help              Show this screen.

    """.format(out_dir='stubs', version=__version__)

arguments = docopt(__doc__, version=__version__)

# OPTIONS
option_assembly_name = arguments['<assembly-name>']
option_all = arguments['--all']
option_output_dir = arguments['--folder']
option_overwrite = arguments['--overwrite']
option_json = not arguments['--no-json']
option_directory = arguments['--directory']

if arguments['--debug']:
    logger.enable_debug()

# PROJECT_DIR = os.getcwd()  # Must execute from project dir
PKG_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(PKG_DIR)
release_dir = os.path.join(PROJECT_DIR, 'release', option_output_dir)
os.chdir(PROJECT_DIR)

# Add Paths
PATHS.append(os.path.join(PROJECT_DIR, 'bin'))
[sys.path.append(p) for p in PATHS]

# Additional Paths from Options
if option_directory:
    sys.path.append(option_directory)

logger.debug(sys.path)
logger.debug(arguments)
logger.debug(ASSEMBLIES)
if arguments['make']:
    timer = Timer()
    if not option_all:
        ASSEMBLIES = [option_assembly_name]

    for assembly_name in ASSEMBLIES:
        assembly_dict = make(release_dir, assembly_name,
                             overwrite=option_overwrite, quiet=option_all)
        if option_json:
            dump_json_log(assembly_dict)
    logger.info('Done: {} seconds'.format(timer.stop()))

""" Process Stub

Large files, such as `System/__init__.py` or `Revit/DB/__init__.py`
can exceed memory limits and crash the system.

These files need to be optimized so Jedi won't misbehave and crash your system
when parsing these files to index autocomplete options.

The primary strategies are:
1. Remove unecessary characters (empty lines, extra spaces, etc)
2. Split Large file into parts to improve Jedi perfomance and avoid crashes

#1 is very straight forward. Use a few regexes.
#2 is more complex. Some of the stubs created by generator3 such as DB/__init__.py
had nearyly 2mb. Doesn't seem like much, but for a raw .py file, that's more than
120K lines. System.Windows.Forms had over 7mb.

The strategy here was simple. Take all the classes inside this monster files,
create separate files for each one, and import them back into the original file.

For an example, compare:
`\stubs\Autodesk\Revit\DB\__init__.py`
and
``\stubs.min\Autodesk\Revit\DB\__init__.py`

"""

import re
import os
import sys
import subprocess
from collections import defaultdict
import json
from pprint import pprint

join = os.path.join
project_dir = os.getcwd()  # Must execute from project dir

##########
# CONFIG #
##########
SAVE_PATH = os.path.join(project_dir, 'stubs')
LIMIT_IN_KB = 200
FILESIZE_LIMITE = LIMIT_IN_KB * 1024


def file_is_too_damn_big(filepath):
    return os.path.getsize(filepath) > FILESIZE_LIMITE

def read_source(filepath):
    with open(filepath) as fp:
        source = fp.read()
    return source

def write_source(filepath, source):
    folderpath = os.path.dirname(filepath)
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    with open(filepath, 'w') as fp:
        source = fp.write(source)
    print('File Written: {}'.format(filepath))

target_files = []

TESTING = False
# TESTING = True

for root, subfolders, files in os.walk(SAVE_PATH):
    py_files = [f for f in files if f.endswith('.py')]
    for filename in py_files:
        filepath = join(root, filename)
        filesize = os.path.getsize(filepath)
        filedir = os.path.dirname(filepath)

        new_filedir = filedir.replace('\stubs', '\stubs.min')
        new_filepath = os.path.join(new_filedir, filename)
        source = read_source(filepath)

        print("Processing File detected: {}".format(filepath))

        if TESTING:
            if not filepath.endswith('DB\\__init__.py'):
                continue

        # SOME OF THESE WORK IN TESTS BUT ARE NOT WORKING ON BATCH REPLACEMENT
        replacements = [
                         (r' {4}', ' '),                    # Convert 4 spaces into single
                         (r':\r\n( )+pass', r':pass'),      # Put pass in one line
                         (r'"""\r\n( )+pass', r'"""'),      # If has doc string, not need to keep pass
                         (r'pass\n', r'pass'),              # Remove Extra Line after pass
                         (r' = ', '='),
                         (r', ', ','),
                         (r' # known case of __new__', ''), # Pycharm Note
                         (r' #cannot find CLR method', ''), # Pycharm Note
                         (r'  # default', ''),              # Pycharm Note
                       ]

        new_source = source
        for old, new in replacements:
            new_source = re.sub(old, new, new_source)
        write_source(new_filepath, new_source)
        print('='*30)

        #####################################
        # SEPARATE FILE INTO SEPARATE FILES #
        #####################################

        if file_is_too_damn_big(new_filepath):
            print('='*30)
            print('WARNING: file above breaking max: {}'.format(new_filepath))

            module_name = os.path.basename(filepath).replace('.py', '_parts')
            chunks_dir = join(new_filedir, module_name)

            # Create Blank Init File
            write_source(join(chunks_dir, '__init__.py'), '')

            # Split File into Classes
            chunks = re.split(r'(?:\n)class ', new_source)
            header = chunks.pop(0)
            clean_source = header
            write_source(new_filepath, clean_source)

            for chunk in chunks:
                # Find Class Name and body
                class_source = 'class ' + chunk
                re_class_name = re.search('(class )(\w+)', class_source)
                class_name = re_class_name.group(2)

                if not os.path.exists(chunks_dir):
                    os.mkdir(chunks_dir)

                # Write individual class files
                with open(join(chunks_dir, class_name + '.py'), 'w') as fp:
                    fp.write(class_source)

                # New class file import to __init__
                with open(new_filepath, 'a') as fp:
                    fp.write('from {0}.{1} import {1}\n'.format(module_name, class_name))

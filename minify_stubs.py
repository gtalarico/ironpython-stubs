""" Minify Stub files.

Large files, such as `System/__init__.py` or `Revit/DB/__init__.py`
can exceed memory limits and crash the system.

These files need to be reduced significantly in size so that Jedi won't
misbehave when parsing these files to index autocomplete options.

The primary strategies are:
- Remove unecessary characters (empty lines, extra spaces, etc)
- Use pyminifier to compact
- and as a last options, strip doc strings away. This is less than ideal
  but proved to be necessary in a few cases.


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

# Revit + Dynamo
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017')                                               # RevitAPI
sys.path.append('C:\\Program Files\\Autodesk\\Revit 2017\\en-US')                                      # RevitAPIUI - Revit Req.
sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Core\\1.2')                                           # ProtoGeometry
sys.path.append('C:\\Program Files\\Dynamo\\Dynamo Revit\\1.2\\Revit_2017')                              # RevitServices
sys.path.append(join(project_dir, 'bin'))

SAVE_PATH = os.path.join(project_dir, 'stubs')

# 500KB in Bytes = 500000
LIMIT_IN_KB = 200
FILESIZE_LIMITE = LIMIT_IN_KB * 1024

# Python string size: 331851 bytes = 331.851

def is_too_big(filepath):
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
for root, subfolders, files in os.walk(SAVE_PATH):
    py_files = [f for f in files if f.endswith('.py')]
    for filename in py_files:
        filepath = join(root, filename)
        filesize = os.path.getsize(filepath)
        target_files.append((filepath, filesize))


for filepath, filesize in target_files:
    filename = os.path.basename(filepath)
    filedir = os.path.dirname(filepath)
    new_filedir = filedir.replace('\stubs', '\stubs.min')
    new_filepath = os.path.join(new_filedir, filename)
    if filepath.endswith('.min'):
        continue

    # Uncomment to test with a single file
    # if not filepath.endswith('DB\\__init__.py'):
    #     continue

    print("Processing File detected: {}".format(filepath))
    print("New file: {}".format(new_filepath))

    source = read_source(filepath)
    print('Starting Replacement. Source Size is: {}'.format(filesize))

    replacements = [
                    #  (r'self,', 's,'),         # self in functions signature
                     (r' = ', '='),
                     (r', ', ','),
                     (r' # known case of __new__', ''), # Pycharm Note
                     (r' #cannot find CLR method', ''), # Pycharm Note
                     (r'  # default', ''), # Pycharm Note
                     (r':\r\n( )+pass', r':pass'), # Pycharm Note
                     (r'"""\r\n( )+pass', r'"""'), # If has doc string, not need to keep pass
                     (r'pass\n', r'pass'), # If has doc string, not need to keep pass
                     (r' {4}', ' '),        # Empty Lines
                   ]

    new_source = source
    for old, new in replacements:
        new_source = re.sub(old, new, new_source)

    write_source(new_filepath, new_source)
    print('='*30)


    ## WIP: Separate file into separate files
    if is_too_big(new_filepath):
        print('='*30)
        print('='*30)
        print('='*30)
        print('WARNING: file above breaking max: {}'.format(new_filepath))

        filedir = os.path.dirname(new_filepath)
        module_name = os.path.basename(filepath).replace('.py', '_parts')
        chunks_dir = join(filedir, module_name)
        write_source(join(chunks_dir, '__init__.py'), '')

        chunks = re.split(r'(?:\n)class ', source)
        header = chunks.pop(0)
        clean_source = header
        write_source(new_filepath, clean_source)

        for chunk in chunks:
            class_source = 'class ' + chunk
            class_name = re.search('(class )(\w+)', class_source)
            class_name = class_name.group(2)
            # print(class_source)

            if not os.path.exists(chunks_dir):
                os.mkdir(chunks_dir)

            print(join(chunks_dir, class_name + '.py'))
            with open(join(chunks_dir, class_name + '.py'), 'w') as fp:
                fp.write(class_source)


                print('>>>>>')
                print(join(chunks_dir, '__init__.py'), '')
                with open(new_filepath, 'a') as fp:
                    fp.write('from {0}.{1} import {1}\n'.format(module_name, class_name))

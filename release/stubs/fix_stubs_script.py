"""
This is a script that fixes shortcommings in the existing iron-stubs output, as of 7/5/2023.

Right now, iron-stubs gets types right in the comments it adds, but not the code. It also produces
stubs that have a lot of type errors, and no import statements.

To fix this, this script will re-write the functions and classes with correct syntax.

It will also go through every type in every function, property, and class, and look
for it in  all the other stubs files in the same root. If it finds the class in another stub file,
it will add an import statement at the top of the file. Note that it will use the first class
definition it finds, so if names are not unique and you want to limit the stubs folders it looks through,
remove the unwanted stubs folders. In my case, all the external references were from System

If it does not find a class's inherited class in the current file, another stubs file, or
the builtin types, it will omit that inherited class from the revised code.

This code is not super well written (sorry) (...or commented), but as of now it creates stub files that are
100% warning- and error-free.

Compared to the current repo, I rebuilt my System stubs like this to get the latest datatypes:
C:\'Program Files'\'IronPython 2.7'\ipy.exe -m ironstubs make mscorlib --path="C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319"

How to use this script:
Put this script in the root of the stubs directory.
You will be prompted for the name of the Stubs folder that you want to clean up.
Path syntax is currently handled for Windows (i.e. \), but can be easily fixed for linux

written by Mike Reilly
mreilly92@gmail.com
"""


import os
import re
from pathlib import Path

# Prompt for directory
directory = input("Enter the directory path: ")
# directory = 'test'

# Make a backup
backup_directory = '_' + directory
# shutil.copytree(directory, backup_directory)  # commented out as per request
# print(f"Backup made at {backup_directory}")

# Update the files

class_import_dictionary = {}

def format_new_code(_string):
    return _string.replace("'value'", 'T')

def find_import_declaration(_class_name):
    if _class_name in class_import_dictionary:
        return class_import_dictionary[_class_name]

    # Regular expression to match the class declaration.
    _class_pattern = re.compile(rf"class\s+{_class_name}(?=[\(:\s])")

    for _root, _dirs, _files in os.walk('.'):
        for _filename in _files:
            # Only consider Python files.
            if _filename.endswith('.py'):
                _file_path = os.path.join(_root, _filename)
                # print(f"checking for class {_class_name} in file {_filename}")
                with open(_file_path, 'r') as _file:
                    for _line in _file:
                        # Check the class pattern.
                        if _class_pattern.search(_line):
                            # If a match is found, create the import declaration.
                            # Remove the './' from the root, and replace '/' with '.' to follow Python's import syntax.
                            if _filename == '__init__.py':
                                _module_path = _file_path.split('\\__init__.py')[0].replace('\\','.').lstrip('..')
                            else:
                                _module_path = _file_path.split('.py')[0].replace('\\','.').lstrip('..')
                            _import_declaration = f"from {_module_path} import {_class_name}\n"
                            class_import_dictionary[_class_name] = _import_declaration
                            return _import_declaration
    return None

def handle_class_names(_name):
    if _name is None or _name == '' or _name == 'value':
        return
    _name = _name.strip("'").strip().strip('(').strip(')').strip("'").strip()
    if 'tuple' in _name:
        if len(_name.split("(of ")) > 1:
            _name = _name.split("(of ")
            _name1 = handle_class_names(_name[1])
    elif ',' in _name:
        _name = _name.split(',')
        _name1 = handle_class_names(_name[0])
        if len(_name) > 1:
            _name2 = handle_class_names(_name[1])
            _name = "(" + _name1 + ', ' + _name2 + ')'
    elif '[' in _name:
        _name = _name.split('[')
        _name1 = handle_class_names(_name[0])
        if len(_name) > 1:
            _name2 = handle_class_names(_name[1].strip().strip(']'))
            _name = _name1 + '["' + _name2 + '"]'
    elif not _name in class_names_in_file and not _name in __builtins__:
        # print(f"looking for new class {_name}")
        class_names_in_file.append(_name)
        _import_declaration = find_import_declaration(_name)
        if _import_declaration is not None:
            import_lines.append(_import_declaration)
            print(f"{_name} found. import syntax:  {_import_declaration.strip()}")
    return _name

for path in Path(directory).rglob('*.py'):
    print(f"Working on {path}")
    with open(path, 'r+') as file:
        lines = file.readlines()

        # Collect all class names in the file
        class_names_in_file = [line.split(' ')[1].split(':')[0].split('(')[0] for line in lines if line.lstrip().startswith('class')]
        
        import_lines = []
        new_lines = []  # a new list to store the updated lines
        new_lines.append('from typing import TypeVar\n')
        new_lines.append("\nT = TypeVar('T')\n\n")

        i = 0
        while i < len(lines):
            new_lines.append(lines[i])

            prev_line_index = i - 1  # get the previous line index
            prev_line_indent = len(lines[prev_line_index]) - len(lines[prev_line_index].lstrip())  # get the indentation level of previous line

            if lines[i].startswith('# Error'):
                new_lines.pop()
                new_lines.append(f"{prev_line_indent*' '}{lines[i].strip()}\n")
                new_lines.append(f"{prev_line_indent*' '}    pass")
            
            elif '"""' in lines[i]:
                new_lines.pop()
                comment_block = lines[i]

                if not comment_block.strip().endswith('"""') or comment_block.count('"""') % 2 != 0:  # check if it's a single-line block comment
                    while True:
                        i += 1
                        comment_block += lines[i]
                        if '"""' in lines[i] and lines[i].count('"""') % 2 != 0:  # check if it's the end of a block comment
                            break

                if '->' in comment_block:

                    new_lines.pop()
                    comment_lines = comment_block.strip().split("\n")
                    getter_type = setter_type = None
                    for line in comment_lines:
                        line = line.strip().lstrip('"""').strip()  # remove """ at the start of lines
                        if line.startswith('Get:'):
                            getter_type = line.split('->')[1].strip()
                        elif line.startswith('Set:'):
                            setter_type = line.split('=')[1].strip()
                    
                    if 'property' in lines[prev_line_index]:
                        property_name = lines[prev_line_index].split('=')[0].strip()
                        if not getter_type:
                            getter_type = setter_type
                        if not setter_type:
                            setter_type = getter_type
                        getter_type = handle_class_names(getter_type)
                        setter_type = handle_class_names(setter_type)
                        new_code = f"{prev_line_indent*' '}@property\n{prev_line_indent*' '}def {property_name}(self) -> '{getter_type}':\n{prev_line_indent*' '}    return self._{property_name}\n{prev_line_indent*' '}@{property_name}.setter\n{prev_line_indent*' '}def {property_name}(self, value: '{setter_type}') -> None:\n{prev_line_indent*' '}    self._{property_name} = value"

                    elif 'def' in lines[prev_line_index]:
                        method_line = lines[prev_line_index].strip()
                        method_name = method_line.split(' ')[1].split('(')[0]
                        for line in [line for line in comment_lines if '->' in line]:
                            return_type = line.split('->')[1].strip().split("\n")[0].strip('"""')
                            return_type = handle_class_names(return_type)
                            new_code = f"{prev_line_indent*' '}def {method_name}(self) -> '{return_type}':\n{prev_line_indent*' '}"
                    
                    new_lines.append(format_new_code(new_code+'\n'))
                    old_commented_out_code = f"{prev_line_indent*' '}# {lines[prev_line_index].lstrip()}"
                    new_lines.append(old_commented_out_code)  # Commenting out existing code

                comment_block = comment_block.replace('\n\n\n\n','\n')
                if comment_block.strip().split('\n')[-1] == '"""':
                    comment_block = comment_block.rstrip().split('\n')
                    comment_block.pop()
                    comment_block.append(prev_line_indent*' ' + '"""\n')
                    comment_block = ''.join(comment_block)
                new_lines.append(comment_block)

            elif 'class ' in lines[i] and '(' in lines[i] and not lines[i].strip().startswith('#'):  # Check if the line is a class definition
                class_line_index = i
                class_line_indent = len(lines[class_line_index]) - len(lines[class_line_index].lstrip())  # get the indentation level of class line
                class_name, superclass_names = lines[class_line_index].split(' ')[1].split('(')[0], lines[class_line_index].split(' ')[1].split('(')[1].rstrip('):\n').split(',')
                
                # Keep only superclasses that are defined in the same file
                for name in superclass_names:
                    name = handle_class_names(name)
                superclass_names = [name for name in superclass_names if name in class_names_in_file]

                if superclass_names:
                    new_class_code = f"{class_line_indent*' '}class {class_name}({', '.join(superclass_names)}):"
                else:
                    new_class_code = f"{class_line_indent*' '}class {class_name}:"
                
                new_lines.pop()
                new_lines.append(format_new_code(new_class_code+'\n'))
                new_lines.append(f"{class_line_indent*' '}# {lines[class_line_index]}")  # Commenting out existing code
            
            elif lines[i].strip() == "None = None":
                new_lines.pop()

            i += 1
        for line in import_lines:
            new_lines.insert(0, line)
        file.seek(0)
        file.truncate()
        file.write(''.join(new_lines))

print("\n\nStub files updated!")
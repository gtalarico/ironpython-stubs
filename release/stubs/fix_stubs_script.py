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

This code is not super well written (sorry), but as of now it creates stub files that make full use
of type hinting.

Compared to the current repo, I rebuilt my System stubs like this to get the latest datatypes:
C:\'Program Files'\'IronPython 2.7'\ipy.exe -m ironstubs make mscorlib --path="C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319"

How to use this script:
Put this script in the root of the stubs directory.
You will be prompted for the name of the Stubs folder that you want to clean up.
Path syntax is currently handled for Windows (i.e. \), but can be easily fixed for linux

written by Mike Reilly
mreilly92@gmail.com
"""

from fileinput import filename
import os
import re
from pathlib import Path
from tkinter import N

# Prompt for assembly stub directory
directory = input("Enter the directory path: ")

# initialize empty dictionary for import statements
resolved_class_dictionary = {}
unresolved_class_list = []

def split_ignore_brackets(s):
    stack = []
    result = []
    current = ''
    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]' and stack:
            stack.pop()
        
        if char == ',' and not stack:
            result.append(current)
            current = ''
        else:
            current += char

    if current:
        result.append(current)

    return result

def find_import_declaration(_class_name):
    if _class_name in resolved_class_dictionary:
        # import statement for this class name was already resolved during this run
        return resolved_class_dictionary[_class_name]

    if _class_name in unresolved_class_list:
        return None

    print(f"{file_name}-> Looking for class {_class_name}.")
    # Regular expression to match the class declaration.
    try:
        _class_pattern = re.compile(rf"class\s+{_class_name}(?=[\(:\s])")
    except re.error:
        return None

    # walk all files in directory
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
                            # write the import declaration
                            _import_declaration = f"from {_module_path} import {_class_name}\n"
                            # store the import declaration for this class name
                            resolved_class_dictionary[_class_name] = _import_declaration
                            # return the import declaration
                            return _import_declaration
    # class name not found
    unresolved_class_list.append(_class_name)
    return None

def handle_class_names(_name, return_with_double_quotes = True):
    print(f"{file_name}-> Handling class {_name}")
    # remove garbage from class name
    if _name is None or _name == '':
        return ""
    _name = _name.strip("'").strip().strip("'").strip()
    if _name in __builtins__:
        return _name
    elif _name in valid_class_names_for_file:
        if return_with_double_quotes:
            return f"\"{_name}\""
        else:
            return _name
    elif 'tuple (of' in _name:
        # handle tuple(of foo) syntax
        if len(_name.split("(of ",1)) > 1:
            _name = _name.split("(of ",1)
            _name = handle_class_names(_name[1], return_with_double_quotes)
            _name = f"tuple (of {_name})"
            return _name
    elif _name.endswith(")") and _name.startswith("("):
        # handle (foo, bar) syntax
        _name = _name.strip('(').strip(')')
        _name = "(" + handle_class_names(_name, return_with_double_quotes) + ")"
        return _name
    elif len(split_ignore_brackets(_name)) > 1:
        # handle (foo, bar) syntax
        _name = _name.strip('(').strip(')')
        _name = split_ignore_brackets(_name)
        _name_str = ""
        for _nam in _name:
            test = handle_class_names(_nam, return_with_double_quotes)
            _name_str = _name_str + handle_class_names(_nam, return_with_double_quotes) + ", "
        _name_str = _name_str.strip(", ")
        return _name_str
    elif _name.endswith("]") and "[" in _name:
        # handle foo[bar] syntax
        _name = _name[:-1]
        _name = _name.split('[', 1)
        if len(_name) > 1:
            _name_str = handle_class_names(_name[0], return_with_double_quotes) + "[" + handle_class_names(_name[1], return_with_double_quotes) + "]"
        else:
            _name_str = "[" + handle_class_names(_name[1], return_with_double_quotes) + "]"
        return _name_str
    elif 'value' == _name:
        # replace all instances of 'value' with 'T' (refer to hardcoded import statement T = TypeVar('T'))
        return 'T'
    elif not _name in valid_class_names_for_file:
        # class not found in this file, and is not builtin
        # add to known classes for this file
        valid_class_names_for_file.append(_name)
        # get import declaration
        _import_declaration = find_import_declaration(_name)
        if _import_declaration is not None:
            # import declaration found
            import_lines.append(_import_declaration)
            print(f"{file_name}-> {_name} found. import syntax:  {_import_declaration.strip()}")
        if return_with_double_quotes:
            return f"\"{_name}\""
        else:
            return _name
    else:
        if return_with_double_quotes:
            return f"\"{_name}\""
        else:
            return _name
    # return name in double quotes to avoid editor class type warnings

for path in Path(directory).rglob('*.py'):
    file_name = path
    print(f"Working on {path}")
    with open(path, 'r+') as file:
        # read file lines
        lines = file.readlines()

        # Collect all class names in the file
        valid_class_names_for_file = [line.split(' ')[1].split(':')[0].split('(')[0] for line in lines if line.lstrip().startswith('class')]
        
        # a list of import statements to insert at the top of the file
        import_lines = []
        # write buffer as a list of new lines
        new_lines = []
        
        # import lines used in this code
        new_lines.append('from typing import overload\n')
        new_lines.append('from typing import TypeVar\n')
        new_lines.append("\nT = TypeVar('T')\n\n")

        i = 0
        while i < len(lines):
            # store the line in the write buffer
            new_lines.append(lines[i])

            # get the previous line index and indent
            prev_line_index = i - 1
            prev_line_indent = len(lines[prev_line_index]) - len(lines[prev_line_index].lstrip())

            # special case, replace these lines with 'pass'
            if lines[i].startswith('# Error'):
                # remove the error comment line from the write buffer, which is not indented properly
                new_lines.pop()
                # reinsert the error comment line with correct indenting
                new_lines.append(f"{prev_line_indent*' '}{lines[i].strip()}\n")
                # insert pass with correct indenting
                new_lines.append(f"{prev_line_indent*' '}    pass")
            
            # check if line is the start of a block comment
            elif '"""' in lines[i]:
                # remove the start of the block comment from the write buffer, we will handle it later as one chunk
                new_lines.pop()
                # start storing the commend block in a big string
                comment_block = lines[i]

                 # check if it's a single-line block comment
                if not comment_block.strip().endswith('"""') or comment_block.count('"""') % 2 != 0:
                    # not single-line block comment.
                    # loop until we find the end of the comment block
                    while True:
                        # increment file line number
                        i += 1
                        # add current line to comment block string
                        comment_block += lines[i]
                        # check if it's the end of the block comment
                        if '"""' in lines[i] and lines[i].count('"""') % 2 != 0:
                            # exit while loop, we have gotten the whole comment block
                            break
                
                # check if there is a type hint in the comment block
                if '->' in comment_block:
                    #type hint found
                    # remove the line of code before the comment block from the write buffer
                    new_lines.pop()
                    # get list of lines from the comment block
                    comment_lines = comment_block.strip().split("\n")
                    
                    # handling class property definitions (examine line before comment block)
                    if 'property' in lines[prev_line_index]:
                        # initialize types
                        getter_type = setter_type = None
                        # search every line in the comment block
                        for line in comment_lines :
                            # remove white space and """ at the start of each line
                            line = line.strip().lstrip('"""').strip()
                            if line.startswith('Get:'):
                                # Get the type hint from a line that starts with "Get:", remove white space
                                getter_type = line.split('->')[1].strip()
                            elif line.startswith('Set:'):
                                # Get the type hint from a line that starts with "Set:", remove white space
                                setter_type = line.split('=')[1].strip()
                        # extract the property name
                        property_name = lines[prev_line_index].split('=')[0].strip()
                        if not getter_type:
                            # Catch if get type hint not specified, use set type hint
                            getter_type = setter_type
                        if not setter_type:
                            # Catch if set type hint not specified, use get type hint
                            setter_type = getter_type
                        # look for type hint class, generate import statement if needed, reformat class name
                        getter_type = handle_class_names(getter_type)
                        # look for type hint class, generate import statement if needed, reformat class name
                        setter_type = handle_class_names(setter_type)
                        # new property declaration using type hints from comment block:
                        new_code = f"{prev_line_indent*' '}@property\n{prev_line_indent*' '}def {property_name}(self) -> {getter_type}:\n{prev_line_indent*' '}    return self._{property_name}\n{prev_line_indent*' '}@{property_name}.setter\n{prev_line_indent*' '}def {property_name}(self, value: '{setter_type}') -> None:\n{prev_line_indent*' '}    self._{property_name} = value"

                    # handling class method definitions (examine line before comment block)
                    elif 'def' in lines[prev_line_index]:
                        # get the line of code before the comment block
                        method_line = lines[prev_line_index].strip()
                        # extract the method name
                        method_name = method_line.strip().split('def ')[1].split('(',1)[0]
                        # initialize new code string so it can be added to
                        new_code = ""
                        # get lines from comment block containing type hints
                        comment_lines_with_def_type_hinting = [line for line in comment_lines if '->' in line]
                        if len(comment_lines_with_def_type_hinting) > 1:
                            # multiple type hints, is an overloaded function, set up overloaded syntax
                            overload_decorator = f"{prev_line_indent*' '}@overload\n" 
                            overload_continuation = f"{prev_line_indent*' '}    ...\n"
                        else:
                            # not an overloaded function
                            overload_decorator = ""
                            overload_continuation = ""
                        # loop through all lines with type hinting
                        for line in comment_lines_with_def_type_hinting:
                            # get the type hint
                            return_type = line.split('->')[1].strip().split("\n")[0].strip('"""')
                            # look for type hint class, generate import statement if needed, reformat class name
                            return_type = handle_class_names(return_type)
                            # get the function definition
                            func_def = line.split('->')[0].strip().strip('"""').strip()
                            # get the individual function parameters
                            arg_list = split_ignore_brackets(func_def.split('(',1)[1].strip(')'))
                            # initialize argument string so it can be added to
                            args_string = ""
                            # loop over all arguments (parameters)
                            for arg in arg_list:
                                if len(arg.split(":")) > 1:
                                    # extract the parameter name
                                    param_name = arg.split(":")[0].strip()
                                    # extract the parameter type
                                    param_type = arg.split(":")[1].strip()
                                    # look for type hint class, generate import statement if needed, reformat class name
                                    param_type = handle_class_names(param_type)
                                    # reconstruct sinle parameter
                                    param = f"{param_name}: {param_type}"
                                else:
                                    # no type specified, just use parameter string as-is
                                    param = arg
                                # add to args string, add comma
                                args_string = args_string + param + ","
                            # remove the last comma
                            args_string = args_string.strip(",")
                            # construct new method code
                            new_code = new_code + f"{overload_decorator}{prev_line_indent*' '}def {method_name}({args_string}) -> {return_type}:\n{overload_continuation}"
                    
                    # write new code to write buffer
                    new_lines.append(new_code+'\n')
                    # comment out old code
                    old_commented_out_code = f"{prev_line_indent*' '}# {lines[prev_line_index].lstrip()}"
                    # write old commented out code to buffer
                    new_lines.append(old_commented_out_code)

                # reduce white space in comment blocks
                comment_block = comment_block.replace('\n\n\n\n','\n')
                # fix the indenting of the last end of the comment block
                if comment_block.strip().split('\n')[-1] == '"""':
                    comment_block = comment_block.rstrip().split('\n')
                    comment_block.pop()
                    comment_block.append(prev_line_indent*' ' + '"""\n')
                    comment_block = ''.join(comment_block)
                # write the original comment block to the write buffer
                new_lines.append(comment_block)

            # check if line is a class declaration
            elif 'class ' in lines[i] and '(' in lines[i] and not lines[i].strip().startswith('#'):
                test_line = lines[i]
                class_line_index = i
                # get the indentation level of class line
                class_line_indent = len(lines[class_line_index]) - len(lines[class_line_index].lstrip())
                # get list of inherited classes (superclasses)
                class_name = lines[class_line_index].strip().split('class ')[1].split('(',1)[0]
                test = lines[class_line_index].strip().split('class ')[1].split('(',1)[1].strip("#").strip().strip(":").strip(')')
                args = handle_class_names(lines[class_line_index].strip().split('class ')[1].split('(',1)[1].strip("#").strip().strip(":").strip(')'), False)

                # create new class definition code
                if args:
                    new_class_code = f"{class_line_indent*' '}class {class_name}({args}):"
                else:
                    new_class_code = f"{class_line_indent*' '}class {class_name}:"
                
                # removing existing class declaration
                new_lines.pop()
                # add new class declaration
                new_lines.append(new_class_code+'\n')
                 # Commenting out and add existing class declaration
                new_lines.append(f"{class_line_indent*' '}# {lines[class_line_index]}")
            
            # special case, remove garbage code
            elif lines[i].strip() == "None = None":
                new_lines.pop()

            # next line
            i += 1

        # insert import statements into write buffer
        for line in import_lines:
            new_lines.insert(0, line)
        
        # write buffer to file
        file.seek(0)
        file.truncate()
        file.write(''.join(new_lines))

        # snext file

# all files finishes
print("\n\nStub files updated!")
import os
import json
import glob
import re


def processing(file, classlist):
    open_file = open(file, "r")
    modulebase = file.replace('\\', '.').lower()
    regex1 = " *class .*\((.+)\)"
    regex2 = "(.*stubs.)|(\.__init__?)|(\.py)"

    # searches for inherited classes and removes duplicates
    modulebase = re.sub(regex2, "", modulebase)
    text = open_file.read()
    inherited_classes = re.findall(regex1, text)
    filtered_classes = list(dict.fromkeys(inherited_classes))


    add_references = []
    for inherited_class in filtered_classes:
        if inherited_class in classlist:
            if classlist[inherited_class] not in add_references and modulebase not in classlist[inherited_class].lower(): # and not modulebase.endswith(classlist[inherited_class].lower())
                add_references.append(classlist[inherited_class])
    if add_references == []:
        return
    line_to_prepend = ""
    for reference in add_references:
        line_to_prepend += "from " + reference + " import *\n"

    #read file in preparation
    src = open(file,"r")
    fline = line_to_prepend    
    oline = src.readlines()
    oline.insert(0,fline)
    src.close()

    # remake the whole file prepending the correct references
    src = open(file,"w")
    src.writelines(oline)
    src.close()
            
def add_references():
    process_files = []
    with open('classlist.json') as json_file:
        classlist = json.load(json_file)
        available_classes = classlist.keys()
        os.chdir("release/stubs/wms")

        for subdir, dirs, files in os.walk(os.getcwd()):
            for file in files:
                #print os.path.join(subdir, file)
                filepath = subdir + os.sep + file
                if filepath.endswith(".py"):
                    process_files.append(filepath)
        count = 0
        for file in process_files:
            processing(file, classlist)
    print "references added"


    

    


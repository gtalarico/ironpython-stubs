import os
import json
import sys


data = {}
data['assemblylist'] = []
# adding because this file in particular is added to the GAC with the installation
data['assemblylist'].append("TranCon.Exact.Globe2003")


def make_list(path_dll):
    for path in path_dll:
        for file_path in os.listdir(path):
            if file_path.endswith('.dll'):
                data['assemblylist'].append(file_path[:-4])



def make_assemblylist(path_dll):
    make_list(path_dll)
    with open('assemblylist.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)


if __name__ == "__main__":
    if len(sys.argv) = 2:
        path_dll = sys.argv[1]
        make_list(path_dll)
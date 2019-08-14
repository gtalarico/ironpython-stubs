import os
import json

path_dll = ["C:\Program Files (x86)\TranCon\BOXwisePro\Server"]
data = {}
data['assemblylist'] = []



def make_list():
    for path in path_dll:
        for file_path in os.listdir(path):
            if file_path.endswith('.dll'):
                data['assemblylist'].append(file_path[:-4])



def make_assemblylist():
    make_list()
    with open('assemblylist.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)


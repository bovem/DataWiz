import pandas as pd
import pickle
import json
def find_in_vardict(vardict, name):
    for x in vardict.var_dict:
        if x["variable_name"] == name:
            return x

def check_for_df(vardict, var_name):
    flag = 0
    for x in vardict.var_dict:
        if ((x["variable_name"] == var_name) and (x["type"]==pd.DataFrame)):
            flag = 1  
    if flag==0:
        return False
    return True

def save_file(f):
    with open('./media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def dump_to_pkl(var_dict, filename):
    filename = filename.split('.')[0]
    out_file = open('./calc/json_dumps/pkl_file', 'wb')
    pickle.dump(var_dict, out_file)
    out_file.close()

def load_pkl():
    infile = open('./calc/json_dumps/pkl_file', 'rb')
    obj = pickle.load(infile, encoding = 'bytes')
    infile.close()
    return obj


def addCell(cellName):
    opList = []
    print(cellName)
    with open('./calc/json_dumps/oplist.json', 'r') as json_file:
        opList = json.load(json_file)

    if len(opList) != 0:
        opList.append(cellName + '.html')
    else:
        opList = [cellName + '.html']

    with open('./calc/json_dumps/oplist.json','w') as json_file:
        json.dump(opList, json_file)




# cant load pickle file if saved according to name
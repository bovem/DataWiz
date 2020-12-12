import pandas as pd
import pickle
import json
import os
# from .var_dict import VarDict

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

def dump_to_pkl(obj, filename):
    out_file = open('./calc/json_dumps/'+filename, 'wb')
    pickle.dump(obj, out_file)
    out_file.close()

def load_pkl(filename):
    try:
        with open('./calc/json_dumps/' + filename, 'rb') as infile:
            obj = pickle.load(infile, encoding = 'bytes')
    except EOFError as e:
        obj = None

    return obj

def dump_to_json(obj, filename):
    with open('./calc/json_dumps/'+ filename + '.json','w') as json_file:
        json.dump(obj, json_file)


def load_json(filename):
    try:
        with open('./calc/json_dumps/' + filename +'.json') as json_file:
            data = json.load(json_file)
    except EOFError as e:
        data = None
    
    return data


def addCell(cellName):
    opData = []        
    with open('./calc/json_dumps/opdata.json', 'r') as json_file:
        opData = json.load(json_file)

    add_cell_data(opData, cellName)

    with open('./calc/json_dumps/opdata.json','w') as json_file:
        json.dump(opData, json_file)


def getMediaFiles():
    path = "./media/"
    lst = os.listdir(path)
    lst.remove('downloads')
    return lst

def getContext():
    context = load_pkl('context')
    media_files = getMediaFiles()

    # for list of operations

    opdata = load_json('opdata')
    
    # for getting variable names
    vardict = load_pkl('vardict')
    if vardict != None:
        varList = vardict.get_var_list()
    else:
        varList = []

    context['files'] = media_files
    context['opdata'] = opdata
    context['varlist'] = varList

    return context

def setContext(key, value):
    context = load_pkl('context')
    context[key] = value 
    dump_to_pkl(context, 'context')
    return context

# Function not used outside util

def add_cell_data(opData, cellName):
      
    def splitName(cellData):
        cellType = cellData['name'].split('-')[0]
        if cellType == cellName:
            return True
        else:
            return False
    
    cells = list(filter(splitName, opData))
    new_cell_idx = str(len(cells))
    setContext('currentCell', cellName + "-" + new_cell_idx)
    opData.append({
        "type" : cellName+'.html',
        "name" : cellName + "-" + new_cell_idx,
        "data" : {}
    })

def set_cell_data(opData, cellName, key, value):

    for cell in opData:
        if cell['name'] == cellName:
            cell['data'][key] = value
    
    
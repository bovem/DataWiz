import pandas as pd

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

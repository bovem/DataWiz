import pandas as pd
from utils import find_in_vardict
class VarDict():
    def __init__(self):
        self.var_dict = []
    
    def add(self, data, var_name, data_type=pd.DataFrame):
        self.var_dict.append({
            "variable_name":var_name,
            "data":data,
            "type":type(data)
        })
    
    def show_data(self, var_name):
        return(find_in_vardict(self, var_name)["data"])
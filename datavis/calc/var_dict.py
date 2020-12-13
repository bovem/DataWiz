import pandas as pd
from .utils import find_in_vardict

class VarDict():
    def __init__(self):
        self.var_dict = []
    
    def add(self, data, var_name, data_type=pd.DataFrame):
        for i in range(len(self.var_dict)):
            if self.var_dict[i].get('variable_name') == var_name:
                del self.var_dict[i]
                break

        self.var_dict.append({
            "variable_name":var_name,
            "data": data,
            "type": type(data)
        })
    
    def show_data(self, var_name):
        return(find_in_vardict(self, var_name)["data"])

    def move_empty(self, var_name):
        self.add(find_in_vardict(self, "_")["data"], var_name)

    def get_var_list(self):
        var_list = []
        for var in self.var_dict:
            var_list.append(var['variable_name'])
        return var_list
    
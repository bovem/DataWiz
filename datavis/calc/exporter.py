from .var_dict import VarDict
from .utils import find_in_vardict

class Exporter():
    def __init__(self, vardict=VarDict()):
        self.vardict = vardict
    
    def export_csv(self, var_name, filename=""):
        var_data = find_in_vardict(self.vardict, var_name)["data"]
        if(filename == ""):
            filename = var_name
        return var_data.to_csv('./media/downloads/'+filename+'.csv')
    
    def export_json(self, var_name, filename="", orient="index"):
        var_data = find_in_vardict(self.vardict, var_name)["data"]
        if(filename == ""):
            filename = var_name
        return var_data.to_json('./media/downloads/'+filename+'.json',orient=orient)
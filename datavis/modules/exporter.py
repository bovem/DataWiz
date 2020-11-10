from var_dict import VarDict
from utils import find_in_vardict

class Exporter():
    def __init__(self, vardict=VarDict()):
        self.vardict = vardict
    
    def export_csv(self, var_name):
        var_data = find_in_vardict(self.vardict, var_name)["data"]
        return var_data.to_csv()
    
    def export_json(self, var_name, orient="index"):
        var_data = find_in_vardict(self.vardict, var_name)["data"]
        return var_data.to_json(orient=orient)
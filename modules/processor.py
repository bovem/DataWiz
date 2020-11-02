from utils import find_in_vardict
from var_dict import VarDict
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Processor():
    def __init__(self, vardict=VarDict()):
        self.vardict = vardict
    
    def standardize(self, var_name, new_var=True, new_var_name="_"):
        if((new_var==True) and (new_var_name=="_")):
            print("A null variable is created with name '_'.\n Please move it to some other variable name.")    

        scale = StandardScaler()
        
        var = find_in_vardict(self.vardict, var_name)
        var_data = var["data"].select_dtypes(include=['float64', 'int64'])
        scaled_data = scale.fit_transform(var_data.values)

        self.vardict.add(scaled_data, new_var_name)

    def normalize(self, var_name, new_var=True, new_var_name="_"):
        if((new_var==True) and (new_var_name=="_")):
            print("A null variable is created with name '_'.\n Please move it to some other variable name.")    
       
        scale = MinMaxScaler()
        
        var = find_in_vardict(self.vardict, var_name)
        var_data = var["data"].select_dtypes(include=['float64', 'int64'])
        scaled_data = scale.fit_transform(var_data.values)

        self.vardict.add(scaled_data, new_var_name)

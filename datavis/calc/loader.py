import pandas as pd
from .var_dict import VarDict

class Loader():
    def __init__(self, vardict=VarDict()):
        self.vardict =  vardict
    
    def load(self, data, data_name):
        df = pd.read_csv(data)
        self.vardict.add(df, data_name, "df")
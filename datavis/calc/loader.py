import pandas as pd
from .var_dict import VarDict

class Loader():
    def __init__(self, vardict=VarDict()):
        self.vardict =  vardict
    
    def load_csv(self, data, data_name):
        df = pd.read_csv(data)
        self.vardict.add(df, data_name, "df")

    def load_json(self, data, data_name):
        df = pd.read_json(data)
        self.vardict.add(df, data_name, "df")

    def load_html(self, data, data_name):
        df = pd.read_html(data, index_col=0)
        if type(df) == list:
           df = df[0]
        self.vardict.add(df, data_name, "df")

    def load_hdf(self, data, data_name):
        df = pd.read_hdf(data)
        self.vardict.add(df, data_name, "df")

    def load_excel(self, data, data_name):
        df = pd.read_excel(data)
        self.vardict.add(df, data_name, "df")
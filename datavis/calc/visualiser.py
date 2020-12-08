import pandas as pd

from .utils import find_in_vardict, check_for_df
from .var_dict import VarDict


class Visualiser():
    def __init__(self, vardict=VarDict()):
        self.vardict = vardict

    def get_values(self, varname, col_name, no_rows=-1):
        df = find_in_vardict(self.vardict, varname)
        df_list = []
        if(df != None):
            df = df['data']
            df_c = df[col_name][:no_rows]
            df_list = df_c.tolist()

        return df_list

    def get_columns(self, varname):
        df = find_in_vardict(self.vardict, varname)
        lst = []
        if df != None:
            df = df['data']
            lst = list(df.columns)
        return lst
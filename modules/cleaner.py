from utils import find_in_vardict, check_for_df
from var_dict import VarDict

class Cleaner():
    def __init__(self, vardict=VarDict()):
        self.vardict =  vardict

    def remove_null(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].dropna(), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].dropna(inplace=True)
            #print()
            print("Size after dropping nulls: {}".format(var["data"].shape))
    
    def mapper(self, var_name, col_name="", maping={}, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            if new_var:
                self.vardict.add(var["data"], new_var_name)
                var2 = find_in_vardict(self.vardict, new_var_name)
                print("Created Variable name: {}".format(new_var_name))
                var2["data"]["mapped_{}".format(col_name)] = var2["data"]["{}".format(col_name)].map(maping)
            else:
                var["data"]["mapped_{}".format(col_name)] = var["data"]["{}".format(col_name)].map(maping)
    
    def fill_mean(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna(var["data"].mean()), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna(var["data"].fillna(var_data.mean()), inplace=True)
            #print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))

    def fill_median(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna(var["data"].median()), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna(var["data"].fillna(var_data.median()), inplace=True)
            #print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))

    def fill_forward(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna("ffill"), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna(var["data"].fillna("ffill"), inplace=True)
            #print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))
    
    def fill_backward(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna("bfill"), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna(var["data"].fillna("bfill"), inplace=True)
            #print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))
    
    def joiner(self, var_name, var_name2, new_var=False, new_var_name=""):
        if (check_for_df(self.vardict, var_name) and check_for_df(self.vardict, var_name)):
            var = find_in_vardict(self.vardict, var_name)
            var2 = find_in_vardict(self.vardict, var_name2)
            if new_var:
                self.vardict.add(var["data"].join(var2["data"], lsuffix="_{}".format(var_name), 
                rsuffix="_{}".format(var_name2)), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"] = var["data"].join(var2["data"], lsuffix="_{}".format(var_name),
                 rsuffix="_{}".format(var_name2))

    """
    def merger(self, var_name_list, new_var=False, new_var_name=""):
        flag = 0
        for var_name in var_name_list:
            if ~(check_for_df(self.vardict, var_name)):
                flag=1
        if flag == 0:
            dfs = [find_in_vardict(self.vardict, v) for v in var_name_list]
            suffixes = ["_{}".format(v) for v in var_name_list]
            if new_var:
                self.vardict.add(pd.merge(dfs, suffixes=suffixes), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"] = pd.merge(dfs, suffixes=suffixes)  
    """      
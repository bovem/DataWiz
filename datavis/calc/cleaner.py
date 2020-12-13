from .utils import find_in_vardict, check_for_df
from .var_dict import VarDict


class Cleaner():
    def __init__(self, vardict=VarDict()):
        self.vardict = vardict

    def remove_null(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].dropna(), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].dropna(inplace=True)
            # print()
            print("Size after dropping nulls: {}".format(var["data"].shape))

    def mapper(self, var_name, col_name="", maping={}, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            if new_var:
                self.vardict.add(var["data"], new_var_name)
                var2 = find_in_vardict(self.vardict, new_var_name)
                print("Created Variable name: {}".format(new_var_name))
                var2["data"]["mapped_{}".format(
                    col_name)] = var2["data"]["{}".format(col_name)].map(maping)
            else:
                var["data"]["mapped_{}".format(
                    col_name)] = var["data"]["{}".format(col_name)].map(maping)

    def fill_mean(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna(
                    var["data"].mean()), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna(var_data.mean(), inplace=True)
            # print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))

    def fill_median(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna(
                    var["data"].median()), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna(var_data.median(), inplace=True)
            # print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))

    def fill_forward(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna("ffill"), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna("ffill", inplace=True)
            # print()
            #print("Size after dropping nulls: {}".format(var["data"].shape))

    def fill_backward(self, var_name, new_var=False, new_var_name=""):
        if check_for_df(self.vardict, var_name):
            var = find_in_vardict(self.vardict, var_name)
            #print("Size before dropping nulls: {}".format(var["data"].shape))
            if new_var:
                self.vardict.add(var["data"].fillna("bfill"), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"].fillna("bfill", inplace=True)
            # print()
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

    def merger(self, var_name_list, new_var=False, new_var_name=""):
        def multimerge(dflist, suffixlist):
            temp_df = dflist[0]
            temp_df.columns = ["{}_{}".format(
                t, suffixlist[0]) for t in temp_df.columns]

            for l, s in zip(dflist[1:], suffixlist[1:]):
                l.columns = ["{}_{}".format(t, s) for t in l.columns]
                temp_df = temp_df.join(l)
            return temp_df

        flag = 0
        for var_name in var_name_list:
            if not (check_for_df(self.vardict, var_name)):
                #print(not (check_for_df(self.vardict, var_name)))
                print("{} is Empty Dataframe".format(var_name))
                flag = 1
        if flag == 0:
            dfs = [find_in_vardict(self.vardict, v)["data"]
                   for v in var_name_list]
            suffixes = ["_{}".format(v) for v in var_name_list]
            if new_var:
                self.vardict.add(multimerge(dfs, suffixes), new_var_name)
                print("Created Variable name: {}".format(new_var_name))
            else:
                var["data"] = multimerge(dfs, suffixes)

from loader import Loader
l = Loader()
df = l.load("limestone_2020.csv", "limestone")
print(l.vardict.var_dict[0]["data"])

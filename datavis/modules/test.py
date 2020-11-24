from loader import Loader
from cleaner import Cleaner
from processor import Processor

import warnings
warnings.filterwarnings("ignore")

from utils import find_in_vardict

l = Loader()
# l.load("limestone_2020.csv", "limestone")
# l.load("iron.csv", "iron")
# l.load("iron.csv", "iron2")
l.load("MBSComtrade.csv", "mbs")
# print(l.vardict.var_dict)
c = Cleaner(l.vardict) 
#c.remove_null("limestone")
#c.mapper("limestone", "Year", {2020:"This_year"}, new_var=True, new_var_name="this_var")

#c.joiner("limestone", "iron")
# print(c.vardict.show_data("limestone"))

c.fill_backward("mbs")

#c.merger(["limestone", "iron", "iron2"], new_var=True, new_var_name="merged")
p = Processor(c.vardict)
#p.normalize("mbs","trade_flow_desc", new_var=True, new_var_name="mbs_scaled")
p.onehotencoder("mbs", "trade_flow_desc", new_var=True, new_var_name="mbs_encoded")

print(p.vardict.show_data("mbs_encoded"))
#print(p.vardict.show_data("merged"))

















# df = find_in_vardict(c.vardict, 'limestone')
# df = df['data']
# df_nan = df["Netweight (kg)"].isnull()
# df = df[df_nan]

# print(df["Netweight (kg)"])
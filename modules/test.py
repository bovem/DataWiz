from loader import Loader
from cleaner import Cleaner
from processor import Processor
import warnings
warnings.filterwarnings("ignore")
l = Loader()
l.load("limestone_2020.csv", "limestone")
l.load("iron.csv", "iron")
l.load("MBSComtrade.csv", "mbs")
#print(l.vardict.var_dict)
c = Cleaner(l.vardict)
c.remove_null("limestone")
#c.mapper("limestone", "Year", {2020:"This_year"}, new_var=True, new_var_name="this_var")
#c.fill_backward("limestone", new_var=True, new_var_name="some_var")
#c.joiner("limestone", "iron")
p = Processor(c.vardict)
p.normalize("mbs", new_var=True, new_var_name="mbs_scaled")
#print(p.vardict.show_data("mbs_scaled").info())
print(p.vardict.show_data("mbs_scaled"))


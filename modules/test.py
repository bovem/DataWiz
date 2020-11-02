from loader import Loader
from cleaner import Cleaner
l = Loader()
df = l.load("limestone_2020.csv", "limestone")
c = Cleaner(l.vardict)
#c.remove_null("limestone")
#c.mapper("limestone", "Year", {2020:"This_year"}, new_var=True, new_var_name="this_var")
#c.fill_backward("limestone", new_var=True, new_var_name="some_var")
print(c.vardict.show_data("some_var").info())


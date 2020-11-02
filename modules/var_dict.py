class VarDict():
    def __init__(self):
        self.var_dict = []
    
    def add(self, data, var_name, data_type="df"):
        self.var_dict.append({
            "variable_name":var_name,
            "data":data,
            "type":data_type
        })
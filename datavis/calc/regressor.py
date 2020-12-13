from .utils import find_in_vardict
from .var_dict import VarDict
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import pandas as pd

class Regressor():
    def __init__(self, var_name, target, vardict=VarDict()):
        self.vardict = vardict
        self.model = None
        self.var = find_in_vardict(self.vardict, var_name)["data"]
        self.features =  self.var.drop(target, axis=1).select_dtypes(include=['number']).values
        # print(self.features)
        self.target = self.var[target].values
    
    def linear_regressor(self):
        self.model = LinearRegression()
    
    def support_vector_regressor(self):
        self.model = SVR()

    def decision_tree_regressor(self):
        self.model = DecisionTreeRegressor()

    def random_forest_regressor(self):
        self.model = RandomForestRegressor()

    def score(self, pred_var_name="_"):
        csv = cross_val_score(self.model, self.features, self.target, scoring='neg_mean_squared_error', cv=10)
        self.model.fit(self.features, self.target)
        predictions = self.model.predict(self.features)

        pred_df = pd.DataFrame({
            "Predictions":predictions
        })

        self.vardict.add(pred_df, pred_var_name)

        return csv.mean()
    
    # TODO: Add best regressor method
    # def best_regressor(self):
    #     models = [linear_regressor, support_vector_regressor, decision_tree_regressor, random_forest_regressor]
    #     for model in models:
    #         self.score
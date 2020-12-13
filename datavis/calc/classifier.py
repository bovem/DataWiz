from .utils import find_in_vardict
from .var_dict import VarDict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import numpy as np
import pandas as pd

class Classifier():
    def __init__(self, var_name, target, vardict=VarDict()):
        self.vardict = vardict
        self.model = None
        self.var = find_in_vardict(self.vardict, var_name)["data"]
        self.features =  self.var.drop(target, axis=1).select_dtypes(include=['number']).values
        # print(self.features)
        self.target = self.var[target].values
    
    def knn_classifier(self):
        self.model = KNeighborsClassifier()

    def decision_tree_classifier(self):
        self.model = DecisionTreeClassifier()

    def random_forest_classifier(self):
        self.model = RandomForestClassifier()
    
    def logistic_classifier(self):
        self.model = LogisticRegression()

    def svm_classifier(self):
        self.model = SVC()

    def score(self, pred_var_name="_"):
        csv = cross_val_score(self.model, self.features, self.target, scoring='accuracy', cv=10)
        self.model.fit(self.features, self.target)
        predictions = self.model.predict(self.features)

        pred_df = pd.DataFrame({
            "Predictions":predictions
        })

        self.vardict.add(pred_df, pred_var_name)

        return np.round(csv.mean()*100, 2)
    
    # TODO: Add best regressor method
    # def best_regressor(self):
    #     models = [linear_regressor, support_vector_regressor, decision_tree_regressor, random_forest_regressor]
    #     for model in models:
    #         self.score
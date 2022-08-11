from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

param_grid = {
    "max_depth"        : [3, None],
    "max_features"     : [1, 3, 5],
    "min_samples_split": [2, 3, 10],
    "min_samples_leaf" : [1, 3, 10],
    "bootstrap"        : [True, False],
    "criterion"        : ["gini", "entropy"]
}

rf = RandomForestClassifier()
clf = GridSearchCV(rf, param_grid=param_grid, n_jobs=-1, scoring='roc_auc')

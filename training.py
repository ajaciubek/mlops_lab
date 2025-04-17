from sklearn.datasets import load_iris
from sklearn import tree
import joblib

X, y = load_iris(return_X_y=True)

model = tree.DecisionTreeClassifier()
model = model.fit(X, y)
joblib.dump(model, "model.pkl")

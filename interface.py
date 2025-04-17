import joblib

MODEL = None


def load_model():
    global MODEL
    MODEL = joblib.load("model.pkl")


def predict(data: dict) -> str:
    global MODEL
    return f"{MODEL.predict([[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]])}"

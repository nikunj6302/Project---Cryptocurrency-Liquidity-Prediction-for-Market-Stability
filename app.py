from flask import Flask,render_template,request
import pickle
import numpy as np

name = Flask(__name__)

model = pickle.load(open("Final Model.pkl","rb"))

@name.route('/')
def Home():
    return render_template("index.html")

@name.route('/predict', methods=["POST"])
def predict():
    float_features = [float(X) for X in list(request.form.values())[1:]]
    features = [np.array(float_features)]
    value = model.predict(features )
    results = ""
    if value == 0:
        results = "High"
    elif value == 1:
        results = "Medium"
    else:
        results = "Low"

    return render_template("result.html",result =results)


if __name__ == "__main__":
    name.run(debug=True)
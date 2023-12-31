import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("C:/Users/manya/PycharmProjects/Spotify_final/model.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = model.best_estimator_.predict(query_df)
    return jsonify({"Streams Prediction": list(prediction)})


if __name__ == "__main__":
    app.run(debug=True)

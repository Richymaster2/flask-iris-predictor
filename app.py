from flask import Flask, request, render_template, url_for, jsonify
from flask_bootstrap import Bootstrap
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from form import IrisDatasetForm
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] ="8n48mzuowxelNoezdawnufhui"
Bootstrap(app)

@app.route('/')
def index():
    form = IrisDatasetForm()
    return render_template('index.html', form=form)

@app.route('/predict')
def predict():
    

    return jsonify({"Output": "Predictions from pickled model"})


if __name__ == '__main__':
    app.run(debug=True)
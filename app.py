from flask import Flask, request, render_template, url_for, jsonify
from flask_bootstrap import Bootstrap
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from form import IrisDatasetForm
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from decimal import Decimal
import base64
import numpy as np
from io import BytesIO

import pickle
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
app.config['SECRET_KEY'] ="8n48mzuowxelNoezdawnufhui"
Bootstrap(app)

@app.route('/')
def index():
    form = IrisDatasetForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
     int_features = [float(x) for x in request.form.values()]
     final_features = [np.array(int_features)]
     prediction = model.predict(final_features)

     output =prediction[0]

     return render_template('index.html', predicted ='The predicted flower is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

clf=pickle.load(open('Impact_Prediction.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/impact',methods=['POST'])
def impact():
    if request.method == 'POST': 
     features=[val for val in request.form.values()]
     prediction = clf.predict(features)
     
     return render_template('index.html', prediction_text='Impact will be {}'.format(prediction))
    else:
        return render_template('index.html',Response ='Please enter Valid Input.')
 
if __name__ == "__main__":
    app.run(debug=True)

import numpy as np
from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
clf=pickle.load(open('Impact_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/impact',methods=['POST'])
def impact():
    if request.method == 'POST': 
     features=[val for val in request.form.values()]
     final_features = [np.array(features)]
     prediction = clf.predict(final_features)
     
     return render_template('index.html', prediction_text='Impact will be {}'.format(prediction))
 
if __name__ == "__main__":
    app.run(debug=True)

 
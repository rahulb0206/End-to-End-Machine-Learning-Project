import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
from mlmodel import marks
c=marks()
app = Flask(__name__)
UPLOAD_FOLDER = r"C:\Users\Admin\Desktop\project\gpa\csvfile"
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


#default page of our ML_Automation
@app.route('/')
def home():
    return render_template('page1.html')

#To use the predict button in our web-app
@app.route('/upload',methods=['POST'])
def uploadFiles():
      # get the uploaded file
      print("____________________")
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(UPLOAD_FOLDER, 'gpa_1'+uploaded_file.filename)
           uploaded_file.save(file_path)
           print(file_path)
           c.sat_gpa(file_path)
           print("uploaded succesfull")
      return "ok"


@app.route('/page2')
def page2():
    return render_template("page2.html")

@app.route('/enter_y',methods=['POST'])
def enter_y():
    print("Enter Y :")
    inputar = [str(x) for x in request.form.values()]
    inputar = [np.array(inputar)]
    print(inputar[0])
    c.y_value(inputar[0])
    enter_y.Yvalue=inputar[0]
    return render_template('page2.html')

@app.route('/page4')
def page4():
    return render_template("page4.html")

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("HIII")
    model = pickle.load(open('model.pkl', 'rb'))
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    X=enter_y.Yvalue
    return render_template('page4.html', prediction_text='{} of the student is :{}'.format(*X,prediction[0]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=107)
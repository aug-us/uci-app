#importing packages
from flask import Flask, render_template, jsonify, redirect, request
import pickle
import sqlite3
import os
#initializing the app
app = Flask(__name__)

#setting route for the home page/web form
@app.route('/')
@app.route("/home")
def home():
    return render_template("home.htm")

#setting app route for prediction
@app.route('/result', methods=['POST'])

def result():
    if request.method == 'POST':
        to_predict_list=request.form.to_dict()
        #getting all the variables from the form
        age = request.form['age']
        sex = request.form['sex']
        restbp = request.form['resting blood pressure']
        chol = request.form['cholestrol']
        fastbs = request.form['fasting blood sugar']
        max_heart = request.form['max heart rate']
        exina = request.form['exercise induced angina']
        blood_vessels = request.form['no of blood vessels']
        chest_pain_1 = request.form['chest pain type 1']
        chest_pain_4 = request.form['chest pain type 4']
        chest_pain_3 = request.form['chest pain type 3']
        chest_pain_2 = request.form['chest pain type 2']
        ST = request.form['ST depression']
        slope_3 = request.form['slope of ST segment 3']
        slope_2 = request.form['slope of ST segment 2']
        slope_1 = request.form['slope of ST segment 1']
        slope_9 = request.form['slope of ST segment -9']
        ecg_2 = request.form['resting ecg 2']
        ecg_0 = request.form['resting ecg 0']
        ecg_1 = request.form['resting ecg 1']
        ecg_9 = request.form['resting ecg -9']
        
        #converting it to a list
        uci_list=[age,sex,restbp,chol,fastbs,max_heart,exina,blood_vessels,chest_pain_1,
                  chest_pain_4,chest_pain_3,chest_pain_2,ST,slope_3,slope_2,slope_1,slope_9,
                  ecg_2,ecg_0,ecg_1,ecg_9]
        uci=[uci_list]
        #loading the serialized model
        loaded_model = pickle.load(open('model_sql_final2.pkl','rb'))
        #predicting the user values
        result=loaded_model.predict(uci)
        result=result[0]
        
        #establishing connection with the database
        #with sqlite3.connect('UCI_FLASK.db') as con:
         #   cur=con.cursor()
             
        #storing values in the table and calling the respective htm page
        if int(result)==0:
          #   cur.execute("INSERT INTO User_data (AGE,SEX,RESTING_BLOOD_PRESSURE,CHOLESTROL,FASTING_BLOOD_SUGAR,MAXIMUM_HEART_RATE,EXERCISE_INDUCED_ANGINA,NO_OF_BLOOD_VESSELS_IN_FLUOROSCOPY,CHEST_PAIN_TYPICAL_ANGINA,CHEST_PAIN_ASYMPTOMATIC_,CHEST_PAIN_NON_ANGINAL_PAIN,CHEST_PAIN_ATYPICAL_ANGINA,ST_DEPRESSION,DOWNSLOPING_OF_ST_SEGMENT, FLAT_ST_SEGMENT,UPSLOPING_OF_ST_SEGMENT,UNKNOWN_SLOPING_OF_ST_SEGMENT,RESTING_ECG_LEFT_VENTRICULAR_HYPERTROPY,RESTING_ECG_NORMAL,RESTING_ECG_ST_WAVE_ABNORMALITY,RESTING_ECG_UNKNOWN,RESULT) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(age,sex,restbp,chol,fastbs,max_heart,exina,blood_vessels,chest_pain_1,chest_pain_4,chest_pain_3,chest_pain_2,ST,slope_3,slope_2,slope_1,slope_9,ecg_2,ecg_0,ecg_1,ecg_9,0))
           #  cur.execute("COMMIT")
             return render_template("result_0.htm")
        else:
            # cur.execute("INSERT INTO User_data (AGE,SEX,RESTING_BLOOD_PRESSURE,CHOLESTROL,FASTING_BLOOD_SUGAR,MAXIMUM_HEART_RATE,EXERCISE_INDUCED_ANGINA,NO_OF_BLOOD_VESSELS_IN_FLUOROSCOPY,CHEST_PAIN_TYPICAL_ANGINA,CHEST_PAIN_ASYMPTOMATIC_,CHEST_PAIN_NON_ANGINAL_PAIN,CHEST_PAIN_ATYPICAL_ANGINA,ST_DEPRESSION,DOWNSLOPING_OF_ST_SEGMENT, FLAT_ST_SEGMENT,UPSLOPING_OF_ST_SEGMENT,UNKNOWN_SLOPING_OF_ST_SEGMENT,RESTING_ECG_LEFT_VENTRICULAR_HYPERTROPY,RESTING_ECG_NORMAL,RESTING_ECG_ST_WAVE_ABNORMALITY,RESTING_ECG_UNKNOWN,RESULT) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",(age,sex,restbp,chol,fastbs,max_heart,exina,blood_vessels,chest_pain_1,chest_pain_4,chest_pain_3,chest_pain_2,ST,slope_3,slope_2,slope_1,slope_9,ecg_2,ecg_0,ecg_1,ecg_9,1))
             #cur.execute("COMMIT")
             return render_template("result_1.htm")
         
@app.route("/insurances",methods=['POST'])
def insurances():
    if( request.form["Submit"] == 'Click to see insurances'):
        return render_template("test.htm")
    elif (request.form["Submit"] == 'Click to see cardiologists'):
        return render_template("doctors.htm")
    else:
        pass            
#running the app in default port 127.0.0.1:5000/      
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0',debug=True, port=port)

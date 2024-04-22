
from flask import Flask, render_template,request,redirect, url_for
from joblib import load 
from datetime import datetime
import pickle
import numpy as np


app = Flask(__name__)
main_list=[]
Hist_list=[]
user_details=[]
global i
i=0 

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100  # Convert height to meters
    bmi = weight_kg / (height_m * height_m)
    return bmi

def obse(BMI):
    x=0
    if(BMI>30):
        x=1 
    return x


def calculate_age_from_dob(date_of_birth):
    dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age



@app.route('/')
def index():
    return render_template('login.html')

@app.route('/newuser')
def newuser():
    return render_template('newuser.html')

@app.route('/submit_newsuser' ,methods=['POST'])
def submit_newsuser():
    username = request.form['name']
    gender = request.form['sex']
    email = request.form['email']
    phone = request.form['phone']
    date = request.form['date']
    age = calculate_age_from_dob(date)
    user_details.append([username,gender,email,phone,age])
    print(user_details)
    return redirect(url_for('newuserinfo'))

@app.route('/newuserinfo')
def newuserinfo():
    return render_template('newuserinfo.html')

@app.route('/submit_newuserinfo' ,methods=['POST'])
def submit_newuserinfo():
    smoke = request.form['smoke']
    drink = request.form['drink']
    problem = request.form['problem']
    Diabetes = request.form['Diabetes']
    History = request.form['History']
    Hist_list.append([smoke,drink,problem,Diabetes,History])
    print(Hist_list)
    return redirect(url_for('healthdetails'))

@app.route('/healthdetails')
def healthdetails():
    return render_template('health_details.html')

@app.route('/submit' ,methods=['POST'])
def submit():
        cholesterol_level = request.form['cholesterolLevel']
        heart_rate = request.form['heartRateInput']
        blood_pressure = request.form['bloodPressureInput']
        exercise_hours = request.form['exerciseHoursInput']
        triglycerides = request.form['triglyceridesInput']
        height = request.form['heightInput']
        weight = request.form['weightInput']
        BMI=calculate_bmi(float(height),float(weight))
        sedentary_hours = request.form['sedentaryHoursSelect']
        sleeping_hours = request.form['sleepingHoursSelect']
        stress_level = request.form['stresslevelSelect']
        physical_activity_hours = request.form['physicalActivitySelect']
        obesity=obse(BMI)
        Systolic,Diastolic= str(blood_pressure).split('/')
        main_list.append([cholesterol_level,heart_rate,exercise_hours,triglycerides,BMI,stress_level,sedentary_hours,sleeping_hours,physical_activity_hours,obesity,Systolic,Diastolic])
        print(main_list)
        return redirect(url_for('result')) 

@app.route('/result')
def result():
    model=load('random_forest_model.pkl') 
    data_test=[user_details[0][4],user_details[0][1],main_list[i][0],main_list[i][1],Hist_list[0][3],Hist_list[0][4],Hist_list[0][0],main_list[i][-3],Hist_list[0][1],main_list[i][2],Hist_list[0][2],main_list[i][5],main_list[i][6],main_list[i][4],main_list[i][3],main_list[i][-4],main_list[i][7],main_list[i][-2],main_list[i][-1]]
    data_test=np.array(data_test).reshape(1,-1)
    prediction=model.predict(data_test) 
    print(prediction)
    return render_template('result.html',prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

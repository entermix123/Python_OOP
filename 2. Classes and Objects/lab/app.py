from flask import Flask, request
from healthcare_program import HealthcareProgram

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <h1> Healthcare Program</h11>
        <form action="/result" method="post">
            <p>Name: <input type="text" name="name" /></P>
            <p>Age: <input type="number" name="age" /></P>
            <p>Weight (kg): <input type="number" name="weight" /></P>
            <p>Height (m): <input type="number" name="height" step="0.01"/></P>
            <p>Blood Pressure (mmgh): <input type="text" name="blood_pressure"/></P>
            <p>Activity:
                <select name="activity">
                    <option value="walking">Walking</option>
                    <option value="swimming">Swimming</option>
                    <option value="running">Running</option>
                </select>
            </p>
            <p><input type="submit" value="Submit" /></p>
        </form>
    
    '''


@app.route("/result", methods=['POST'])
def result():
    name = request.form['name']
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    blood_pressure = [int(bp) for bp in request.form['blood_pressure'].split('/')]
    activity = request.form['activity']

    hp = HealthcareProgram(name, age, weight, height, blood_pressure)
    bmi = hp.get_bmi()
    bp_status = hp.get_blood_pressure()
    max_hr = hp.get_target_hearth_rate()
    target_hr = hp.get_target_hearth_rate()
    calories_burned = hp.get_calories_burned(activity)

    return f'''
        <h1> Healthcare Program - Results:</h>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
        <p>Weight: {weight}</p>
        <p>Height: {height}</p>
        <p>BMI: {bmi}</p>
        <p>Blood pressure: {blood_pressure[0]} / {blood_pressure[1]} ({bp_status}) </p>
        <p>Max Heart Rate: {max_hr}</p>
        <p>Target Heart Rate: {target_hr[0]} - {target_hr[1]}</p>
        <p>Calories Burned ({activity}): {calories_burned} </p>
    '''


if __name__ == '__main__':
    app.run()


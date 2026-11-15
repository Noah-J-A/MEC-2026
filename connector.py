from flask import Flask, render_template, request
import json
import time 

app = Flask(__name__)

with open('currentHealth.json', 'r') as file:
    json_data = json.load(file)
file.close()

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])

def update_site():
    newBP = request.form.get('bp')
    newBDDecay = request.form.get('bdDecay')
    newRestHR = request.form.get('restHR')
    newBodyTemp = request.form.get('bodyTemp')
    newWeightChange = request.form.get('weightChange')
    newSleepTime = request.form.get('sleep')
    person = next(iter(json_data))

    new_json = {
        person: {
            "current blood pressure" : newBP, 
            "bone density decay" : newBDDecay, 
            "heart rate rest" : newRestHR,
            "body temp" : newBodyTemp,
            "weight gain/loss" : newWeightChange,
            "sleep mins" : newSleepTime
        } 
    }   

    with open('currentHealth.json', 'w') as file:
        json.dump(new_json, file, indent=4)
    file.close()

    return render_template('index.html', test=newBP)

if __name__ == '__main__':
    app.run(debug=True)

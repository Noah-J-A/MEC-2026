import json
from pathlib import Path
from flask import Flask, render_template, request
from health_test_functions import overall_health


app = Flask(__name__)
BASE = Path(__file__).parent

problems= []

with open(BASE / "currentHealth.json", "r") as f:
        health = json.load(f)
for name in list(health.keys()):
     problems.append(overall_health(name))
f.close()



if len(problems) == 0:
    with open(BASE / "schedule.json", "r") as file:
        data = json.load(file)
    file.close()
else:
    with open(BASE / "schedule.json", "r") as file:
        data = json.load(file)
    file.close()


with open('currentHealth.json', 'r') as file:
    json_data = json.load(file)
file.close()




def time_to_minutes(time): # 6am is considered time 0 to avoid issues when moving past midnight
    hours, mins = time.split(":")
    return (60 * (int(hours) - 6) + int(mins)) % 1440


def minutes_to_time(minutes):
    total = (minutes + 6 * 60) % 1440
    return f"{(total // 60):02d}:{(total % 60):02d}"


name = 'Zack Short'


@app.route("/")


def show_schedule():


    people = list(data.keys())
    schedule = data[name]["daily schedule"]
    for item in schedule:
        end = time_to_minutes(item["start_time"]) + item["duration"]
        item["end_time"] = minutes_to_time(end)
    return render_template("schedule.html", schedule = schedule, people=people, name=name)


@app.route("/choose", methods=['POST'])


def choose_schedule():
    if request.method == "POST":
        name = (list(request.form))[0]


    people = list(data.keys())
    schedule = data[name]["daily schedule"]
    for item in schedule:
            end = time_to_minutes(item["start_time"]) + item["duration"]
            item["end_time"] = minutes_to_time(end)


    return render_template('schedule.html', schedule=schedule, people=people, name = name)


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


    return render_template('schedule.html', test=newBP)


if __name__ == '__main__':
    app.run(debug=True)


 

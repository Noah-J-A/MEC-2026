import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
BASE = Path(__file__).parent

with open(BASE / "schedule.json", "r") as file:
    data = json.load(file)

schedule = data["daily schedule"]

def time_to_minutes(time): # 6am is considered time 0 to avoid issues when moving past midnight
    hours, mins = time.split(":")
    return (60 * (int(hours) - 6) + int(mins)) % 1440

def minutes_to_time(minutes):
    total = (minutes + 6 * 60) % 1440
    return f"{(total // 60):02d}:{(total % 60):02d}"

for item in schedule:
    end = time_to_minutes(item["start_time"]) + item["duration"]
    item["end_time"] = minutes_to_time(end)


@app.route("/")
def show_schedule():
    return render_template("schedule.html", schedule = schedule)
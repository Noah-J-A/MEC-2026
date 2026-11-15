import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
BASE = Path(__file__).parent

with open(BASE / "schedule.json", "r") as file:
    data = json.load(file)

schedule = data["daily schedule"]

@app.route("/")
def show_schedule():
    return render_template("output.html", schedule=schedule)
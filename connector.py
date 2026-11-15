from flask import Flask, render_template, request, redirect, url_for
from connector import db, Item
import json
import time 

interval = 15 #seconds for sleep timer

with open('tasks.json', 'r') as file:
    json_data = json.load(file)

app = Flask(__name__)

tasks = list(json_data.keys())

@app.route('/', methods=["GET", 'POST'])

def index():
    task = json_data[tasks[0]]['name']
    return render_template('index.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)


def update_site(id):
    test = ''

    if request.method == "POST":
        test = request.form.get("test")
    try
        db.session.commit




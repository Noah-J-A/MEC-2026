from flask import Flask, render_template, request
import json
import time 

app = Flask(__name__)

with open('tasks.json', 'r') as file:
    json_data = json.load(file)

tasks = list(json_data.keys())

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])

def update_site():
    new_name = request.form.get('test')
    return render_template('index.html', test=new_name)

if __name__ == '__main__':
    app.run(debug=True)


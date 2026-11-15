from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import json
import time 

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///connector.db"
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

with open('tasks.json', 'r') as file:
    json_data = json.load(file)

tasks = list(json_data.keys())

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])

def update_site():
    new_name = request.form.get('test')
    print(new_name)
    return render_template('index.html', test=new_name)

if __name__ == '__main__':
    app.run(debug=True)


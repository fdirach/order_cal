from flask import Flask, render_template, request
from ddl import * 
from data import *
import sqlite3
import os

app = Flask(__name__)

# Get the path to the database file
dir = os.path.dirname(__file__)
db = os.path.join(dir, 'ordercal.db')

# Connect to db
conn = sqlite3.connect('ordercal.db')
cursor = conn.cursor()

@app.route("/", methods=['GET'])
def base():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(debug=True)
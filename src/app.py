import sqlite3
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/journal.db'

@app.route('/')
def begin():
    return "<3"

db.init_app(app)

app.run(debug=True, host='0.0.0.0', port=5000)

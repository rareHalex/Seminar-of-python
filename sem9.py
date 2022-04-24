from flask import Flask
from work_service.database import list_works

app = Flask(__name__)

"""
@app.route("/")
@app.route('/hello')
def hello():
    return "world"
"""

@app.route("/")
@app.route("/works")
def list_worker():
    return list_works(3)
    
import sqlite3

def dict_factory(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_connection() -> sqlite3.Connection:
    con = sqlite3.connect('works.sqlite')
    con.row_factory = dict_factory
    return con

def list_works(limit:int):
    con = create_connection()
    res = con.execute(f'select * from works limit{limit};')
    return res
    
from work_service.app import app

if __name__ == '__main__':
    app.run()

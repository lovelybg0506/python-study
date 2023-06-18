from flask import Flask, render_template, redirect, url_for, request
# from flask_sqlalchemy import SQLAlchemy
import psycopg2 # postgreSQL
from databasesCRUD import *

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = psycopg2.connect(host='localhost',dbname='todolist',user='postgres',password=1,port=5432)

cursor=db.cursor()

@app.route('/')
def index():
    db = CRUD()
    todo_list = db.readDB(schema='public',table='todolist',column='*')
    # print(todo_list[0][1])
    return render_template('dashboard/index.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    db = CRUD()
    db.insertDB(schema='public',table='todolist',column='title',data=title)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    db = CRUD()
    db.deleteDB(schema='public',table='todolist',condition=f'id={id}')
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    db = CRUD()
    todo_list = db.readDB(schema='public',table='todolist',column='*')
    print(todo_list[id+1][2]) # 이부분 하다가 중단...
    if todo_list[id+1][2] == 'True':
        TrueOrFalse = 'False'
    else:
        TrueOrFalse = 'True'

    db.updateDB(schema='public',table='todolist',column='complete',value=TrueOrFalse,condition=f'id={id}')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('dashboard/about.html')

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, redirect, url_for, request
import psycopg2 # postgreSQL
from databasesCRUD import *

app = Flask(__name__)
db = psycopg2.connect(host='localhost',dbname='todolist',user='postgres',password=1,port=5432)
DBcrud = CRUD()

@app.route('/')
def index():
    todo_list = DBcrud.readDB(schema='public',table='todolist',column='*',condition='order by id asc')
    total_todo = DBcrud.readDB(schema='public',table='todolist',column='count(*)',condition='')
    completed_todo = DBcrud.readDB(schema='public',table='todolist',column='count(*)',condition='where complete = true')
    uncompleted_todo = DBcrud.readDB(schema='public',table='todolist',column='count(*)',condition='where complete = false')
    # return render_template('dashboard/index.html', todo_list=todo_list, total_todo=total_todo,completed_todo=completed_todo,uncompleted_todo=uncompleted_todo)
    return render_template('dashboard/index.html', **locals()) # **locals() : 지역변수 다가져오기,  / **globals() : 전역변수 다가져오기

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    DBcrud.insertDB(schema='public',table='todolist',column='title',data=title)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    DBcrud.deleteDB(schema='public',table='todolist',condition=f'id={id}')
    return redirect(url_for('index'))

@app.route('/update/<int:id>')
def update(id):
    
    todo_list = DBcrud.readDB(schema='public',table='todolist',column='*',condition='order by id asc')

    if todo_list[id-1][2]:
        TrueOrFalse = 'false'
    else:
        TrueOrFalse = 'true'

    DBcrud.updateDB(schema='public',table='todolist',column='complete',value=TrueOrFalse,condition=f'id={id}')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('dashboard/about.html')

if __name__ == "__main__":
    app.run(debug=True)


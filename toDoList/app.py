from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

# Create Models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default=False)

# with app.app_context(): # 찾아보니 이거 추가하라는데 그래도안됨
#     db.create_all()

@app.route('/')
def index():
    return render_template('dashboard/index.html')

@app.route('/about')
def about():
    return render_template('dashboard/about.html')

if __name__ == "__main__":
    app.run(debug=True)


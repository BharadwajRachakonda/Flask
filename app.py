from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        todo = ToDo(title = request.form['title'], desc = request.form['desc'])
        db.session.add(todo)
        db.session.commit()
    allToDo = ToDo.query.all()
    return render_template('index.html', allToDo = allToDo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = ToDo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    allToDo = ToDo.query.all()
    return render_template('index.html', allToDo = allToDo)



if __name__ == "__main__":
    app.run(debug=True, port=8000)

import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    gender=db.Column(db.String(64))
    films = db.relationship('Film', backref='director', cascade="delete")


class Film(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(256))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    film_id = db.Column(db.Integer, db.ForeignKey('directors.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    return render_template('about-members.html')

@app.route('/directors')
def show_all_directors():
    directors = Director.query.all()
    return render_template('director-all.html', directors=directors)

@app.route('/films')
def show_all_films():
    films = Film.query.all()
    return render_template('film-all.html', films=films)


if __name__ == '__main__':
    app.run()

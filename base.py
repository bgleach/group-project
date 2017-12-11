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

@app.route('/director/add', methods=['GET', 'POST'])
def add_directors():
    if request.method == 'GET':
        return render_template('director-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']

        # insert the data into the database
        director = Director(name=name, age=age, gender=gender)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))

@app.route('/director/edit/<int:id>', methods=['GET', 'POST'])
def edit_director(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('director-edit.html', director=director)
    if request.method == 'POST':
        # update data based on the form data
        director.name = request.form['name']
        director.age = request.form['age']
        director.gender = request.form['gender']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_directors'))

@app.route('/director/delete/<int:id>', methods=['GET', 'POST'])
def delete_director(id):
    director= Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('director-delete.html', director=director)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))

@app.route('/films')
def show_all_films():
    films = Film.query.all()
    return render_template('film-all.html', films=films)

@app.route('/film/add', methods=['GET', 'POST'])
def add_films():
    if request.method == 'GET':
        directors = Director.query.all()
        return render_template('film-add.html', directors=directors)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        description = request.form['description']
        director_name = request.form['director']
        director = Director.query.filter_by(name=director_name).first()
        # insert the data into the database
        film = Film(name=name, year=year, description=description, director=director)
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('show_all_films'))

@app.route('/film/edit/<int:id>', methods=['GET', 'POST'])
def edit_song(id):
    film = Film.query.filter_by(id=id).first()
    directors = Director.query.all()
    if request.method == 'GET':
        return render_template('film-edit.html', film=film, directors=directors)
    if request.method == 'POST':
        # update data based on the form data
        film.name = request.form['name']
        film.year = request.form['year']
        film.description = request.form['description']
        director_name = request.form['director']
        director = Director.query.filter_by(name=director_name).first()
        film.director = director
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_films'))

@app.route('/film/delete/<int:id>', methods=['GET', 'POST'])
def delete_course(id):
    film = Film.query.filter_by(id=id).first()
    directors = Director.query.all()
    if request.method == 'GET':
        return render_template('film-delete.html', film=film, directors=directors)
    if request.method == 'POST':
        # delete the artist by id
        # all related songs are deleted as well
        db.session.delete(film)
        db.session.commit()
        return redirect(url_for('show_all_films'))



if __name__ == '__main__':
    app.run()

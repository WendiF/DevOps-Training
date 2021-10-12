from re import L
from flask import Flask, render_template, request, redirect
import csv

from flask.helpers import url_for

def get_films():
    with open('films.txt') as filmsFile:
        reader = csv.DictReader(filmsFile, fieldnames = ('name', 'rating'))
        return [film for film in reader]

def get_filtered_films_by_rating(rating):
    films = get_films()
    return [film for film in films if film["rating"] == rating]
    
def submit_film_review(film_name, stars):
    with open('films.txt', 'a', newline='') as filmsFile:
        csv_writer = csv.writer(filmsFile)
        csv_writer.writerow([film_name, stars])

app = Flask(__name__)

@app.route('/films/list')
def list_films():
    films = get_films()
    return render_template('app.html', films=films)

@app.route('/films/table')
def filter_by_rating():
    rating = request.values.get('stars', '')
    return render_template('app.html', films = get_filtered_films_by_rating(rating))

@app.route('/films/submit')
def submit_review():
    film_name = request.values.get('film_name')
    stars = request.values.get('stars')
    submit_film_review(film_name, stars)
    return redirect(url_for('list_films'))
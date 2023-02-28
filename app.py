from flask import Flask
from flask import render_template, request, redirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils import FirebaseUtils

app = Flask(__name__)

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

utils = FirebaseUtils(db)


@app.route('/')
def index():
    movies = utils.getAllMovies()
    return render_template('index.html', movies=movies)


@app.route('/view/<string:id>')
def view(id):
    movie = utils.getMovie(id)
    if movie is not None:
        return render_template('view.html', movie=movie)
    
    return redirect("/")
    

@app.route('/add', methods=['POST'])
def addNewMovie():
    if request.method == 'POST':
        data = dict(request.form)
        utils.addNewMovie(data)
        
    return redirect('/')


@app.route('/update/<string:id>')
def update(id):
    movie = utils.getMovie(id)
    if movie is not None:
        return render_template('update.html', movie=movie)
    
    return redirect("/")


@app.route('/update/<string:id>', methods=['POST'])
def updateMovie(id):
    if request.method == 'POST':
        data = dict(request.form)
        utils.updateMovie(id, data)
        
    return redirect('/')
    

@app.route('/delete/<string:id>')
def delete(id):
    utils.deleteMovie(id)
    
    return redirect('/')

# 1)import flask
# to render web page add template folder and an html file in that then render template
from flask import Flask,render_template
from data import Faculties

# initialise
app=Flask(__name__)

myFaculties=Faculties()

# declare routing
@app.route('/')
def index():
    return "<hi>Welcome Vineeth</h1>";
@app.route('/login')
def login():
    return render_template('index.html');
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/faculty')
def faculty():
    return render_template('faculty.html',facultyList=myFaculties)


# check
if(__name__=='__main__'):
    app.run(debug=True);
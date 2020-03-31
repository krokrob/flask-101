from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<name>')
def home(name=None):
    name = name.capitalize()
    stack = ['Python', 'Flask', 'Heroku']
    return render_template('home.html', name=name, stack=stack)

@app.route('/new')
def new():
    return render_template('new.html.jinja')

@app.route('/predict')
def predict(input=None):
    pass

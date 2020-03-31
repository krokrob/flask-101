from flask import Flask, render_template
from flask_assets import Environment, Bundle
app = Flask(__name__)
assets = Environment(app)
css = Bundle(
    'stylesheets/components/avatar.css',
    'stylesheets/components/navbar.css',
    output='packed.css'
    )
assets.register('css_all', css)

@app.route('/')
def hello():
    return render_template('hello.html')

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
    return "Work in progress..."

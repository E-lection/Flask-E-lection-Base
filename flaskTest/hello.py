from flask import Flask, render_template
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__)
AppConfig(app)
Bootstrap(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

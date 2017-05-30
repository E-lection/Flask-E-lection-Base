# $ pip install requirements.txt

from flask import Flask, render_template
from flask_appconfig import AppConfig

app = Flask(__name__)
AppConfig(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

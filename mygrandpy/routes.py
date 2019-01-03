from flask import Flask, render_template, request, jsonify

import requests

from .models import Parse

grand_app = Flask(__name__)


@grand_app.route('/')
def home():
    """ the homepage html """
    return render_template('index.html')


@grand_app.route('/answer', methods=['POST'])
def answer():
    """ the answer """
    rep = request.form['question']
    words = Parse(rep)
    return jsonify(words.select_word())

from flask import Flask, render_template, request, jsonify

from .models import Parse

grand_app = Flask(__name__)


@grand_app.route('/')
def home():
    """ the home page html """
    return render_template('index.html')


@grand_app.route('/answer', methods=['POST'])
def answer():
    """ the answer """
    rep = request.form['question']
    word_list = Parse(rep)
    return jsonify(word_list.select_word())

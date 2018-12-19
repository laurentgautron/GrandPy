from flask import Flask, render_template, request, url_for, jsonify
from mygrandpy.scripts.parser import Parse
from mygrandpy.scripts.add import Add

grand_app = Flask(__name__)


@grand_app.route('/')
def home():
    return render_template('index.html')


@grand_app.route('/answer', methods=['POST'])
def answer():
    rep = request.form['question']
    word_list = Parse(rep)
    return jsonify(word_list.select_word())


@grand_app.route('/wordcollection', methods=['POST'])
def word_collection():
    words = request.form['word']
    new_add = Add(words)
    new_add.add_word()
    print('alors quoi')
    return jsonify(words)

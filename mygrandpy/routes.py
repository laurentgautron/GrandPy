from flask import Flask, render_template, request, url_for, jsonify
# from parser import Parse

grand_app = Flask(__name__)


class Parse:

    def __init__(self, sentence):

        self.sentence = sentence.split(" ")

    def mot(self):

        return self.sentence[0]


@grand_app.route('/')
def home():
    return render_template('index.html')


@grand_app.route('/answer', methods=['POST'])
def answer():
    rep = request.form['question']
    print(rep)
    word_list = Parse(rep)
    print(word_list.mot())
    return jsonify("from server:" + word_list.mot())

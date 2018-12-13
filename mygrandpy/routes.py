from flask import Flask, render_template, request, url_for, jsonify

grandapp = Flask(__name__)


@grandapp.route('/')
def home():
    return render_template('index.html')


@grandapp.route('/answer', methods=['POST'])
def answer():
    rep = request.form['question']
    print(rep)
    return jsonify("from server:" + rep)

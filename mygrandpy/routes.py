""" routes used for application """

from flask import Flask, render_template, request, jsonify

from .models import Parse, Coord

APP = Flask(__name__)


@APP.route('/')
def home():
    """ the homepage html """
    return render_template('index.html')


@APP.route('/answer', methods=['POST'])
def answer():
    """ the answer """
    rep = request.form['question']
    words = Parse(rep)
    place = words.select_word()
    print('la place avant parser: ', place)
    if len(place) > 1:
        place = " ".join(place)
    local = Coord.setting_place(place)
    setting = {}
    if local:
        setting = local
        print("les setting", setting)
        return jsonify(setting)


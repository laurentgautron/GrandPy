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
    print(place)
    str = " "
    if len(place) > 1:
        place = str.join(place)
    print(place)
    local = Coord.number(place)
    return jsonify({"coord": local['geometry']['coordinates'], "place": local['place_name']})

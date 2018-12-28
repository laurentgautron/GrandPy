import json
import re
import requests


class Parse:
    """ methods to parse sentences: select_word """

    def __init__(self, sentence):

        self.sentence = (re.sub(r"[-,.;/:!_']", r" ", sentence))
        self.sentence = (re.sub(r"[' ']{2,}", r" ", self.sentence))
        self.sentence = self.sentence.split(" ")

    def select_word(self):
        """ select words which can be used in map API, return a list of words """

        with open('mygrandpy/datas/stopword.json', 'r') as stop_word:
            stop_word_dict = json.load(stop_word)
        retained_text = []
        for word in self.sentence:
            word = word.lower()
            print(word)
            if word not in stop_word_dict:
                retained_text.append(word)
        return retained_text

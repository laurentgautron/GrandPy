""" modules to parse sentences """
import json
import re


class Parse:
    """ methods to parse sentences: select_word """

    def __init__(self, sentence):

        sentence = re.sub(r"[-,.;/:\]!_'?\[()*<>=\"&°@+{}\/]|[0-9]+", r" ", sentence)
        sentence = re.sub(r"[\s]{2,}", r" ", sentence)
        self.sentence = sentence.strip().split(" ")

    def select_word(self):
        """ select words which can be used in map API, return a list of words """

        with open('mygrandpy/datas/stopword.json', 'r') as stop_word:
            stop_word_dict = json.load(stop_word)
        retained_text = []
        for word in self.sentence:
            word = word.lower()
            if word not in stop_word_dict:
                retained_text.append(word)
        return retained_text

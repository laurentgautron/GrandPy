import json
import re


class Parse:

    def __init__(self, sentence):

        self.sentence = (re.sub(r"[,.;/:!_']", r" ", sentence))
        self.sentence = (re.sub(r"[' ']{2,}", r" ", self.sentence))
        self.sentence = self.sentence.split(" ")

    def select_word(self):

        with open('mygrandpy/datas/stopword.json', 'r') as stop_word:
            stop_word_dict = json.load(stop_word)
        retained_text = []
        for word in self.sentence:
            word = word.lower()
            print(word)
            if word not in stop_word_dict:
                retained_text.append(word)
        return retained_text

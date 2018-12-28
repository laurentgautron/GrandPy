import json


class Parse:

    def __init__(self, sentence):

        self.sentence = sentence.split(" ")

    def select_word(self):

        with open('mygrandpy/datas/stopword.json', 'r') as stop_word:
            stop_word_dict = json.load(stop_word)
        retained_text = []
        for word in self.sentence:
            if word not in stop_word_dict:
                retained_text.append(word)
        return retained_text

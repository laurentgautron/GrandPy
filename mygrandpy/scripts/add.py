import json


class Add:

    def __init__(self, words):

        self.words = words

    def add_word(self):
        with open('mygrandpy/datas/stopword.json', 'a') as word_file:
            json.dump(self.words, word_file)

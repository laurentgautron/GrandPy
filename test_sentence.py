from mygrandpy.models import Parse


def test_sentence_uppercase_spaces():
    parse = Parse("OU EST DISNEYLAND")
    assert parse.select_word() == ["disneyland"]


def test_sentence_empty():
    parse1 = Parse("")
    assert parse1.select_word() == [""]


def test_sentence_severalword():
    parse3 = Parse("je veux savoir où se trouve la Tour Eiffel")
    assert parse3.select_word() == ["tour", "eiffel"]


def test_sentence_hypen_exclamation_interrogation():
    parse4 = Parse("!!, ?,-- ;:  , _()..[]@=}+*<< ,>> /{")
    assert parse4.select_word() == ['']

def test_sentence_numeral():
    parse4 = Parse("je veux le 23 et le 45 rue Monmartre")
    assert parse4.select_word() == ['monmartre']

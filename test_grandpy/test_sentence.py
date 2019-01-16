from mygrandpy.models import Parse


def test_sentence():
    parse = Parse("??? moi et disneyland !!!")
    assert parse.select_word() == ["disneyland"]
    parse1 = Parse("!")
    assert parse1.select_word() == [""]
    parse3 = Parse("je veux savoir, où se trouve la TOUR eiffel")
    assert parse3.select_word() == ["tour", "eiffel"]
    parse4 = Parse("connais-tu l'adresse d'OpenClassrom à paris")
    assert parse4.select_word() == ["openclassrooms", "paris"]

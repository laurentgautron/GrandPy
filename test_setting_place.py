from mapbox import Geocoder


def test_setting_place(monkeypatch):
    result = {"coord": [2.295, 48.874], "place": 'Arc de Triomphe, Place Charles de Gaulle, Paris, 75116, France'}

    def monkeyreturn(request):
        return result

    monkeypatch.setattr(Geocoder, 'forward', monkeyreturn)
    assert Geocoder.forward('arc triomphe') == result

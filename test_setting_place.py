"""here we test mapbox API: Geocoder.forward"""
from mapbox import Geocoder
from mygrandpy.models import Coord


def test_setting_place_one(monkeypatch):
    """ test for coordinates arc de triomphe """
    result = [{"coord": [2.295, 48.874], "place": 'Arc de Triomphe, Place Charles de Gaulle, Paris, 75116, France'}]

    def mockreturn(request, access):
        return

    monkeypatch.setattr(Geocoder, 'forward', mockreturn)
    assert Coord.setting_place('arc triomphe') == result

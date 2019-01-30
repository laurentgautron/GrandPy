"""here we test mapbox API: Geocoder.forward"""
from mapbox import Geocoder
from mygrandpy.models import Coord


class MyResponse:

    def __init__(self):
        self.content = {"type": "FeatureCollection", "query":["disneyland"],"features":[{"id":"poi.1511828531266","type":"Feature","place_type":["poi"],"relevance":1,"text":"Disneyland Hotel","place_name":"Disneyland Hotel, Disneyland® Paris, Chessy, Seine-et-Marne 77700, France","center":[2.779718,48.87031],"geometry":{"coordinates":[2.779718,48.87031],"type":"Point"},"context":[{"id":"postcode.8713036370381920","text":"77700"},{"id":"place.14012543432112880","wikidata":"Q1076338","text":"Chessy"},{"id":"region.15077538089479390","short_code":"FR-77","wikidata":"Q12753","text":"Seine-et-Marne"},{"id":"country.9759535382641660","short_code":"fr","wikidata":"Q142","text":"France"}]},{"id":"poi.257698037838","type":"Feature","place_type":["poi"],"relevance":1,"text":"Disneyland Resort Sign","place_name":"Disneyland Resort Sign, S Harbor Blvd, Anaheim, California 92802, United States","center":[-117.91556,33.809216],"geometry":{"coordinates":[-117.91556,33.809216],"type":"Point"},"context":[{"id":"neighborhood.294479","text":"Anaheim Resort"},{"id":"postcode.4074307310154980","text":"92802"},{"id":"place.7749226041161420","wikidata":"Q49247","text":"Anaheim"},{"id":"region.11319063928738010","short_code":"US-CA","wikidata":"Q99","text":"California"},{"id":"country.9053006287256050","short_code":"us","wikidata":"Q30","text":"United States"}]},{"id":"poi.1039382085963","type":"Feature","place_type":["poi"],"relevance":1,"text":"Disneyland Park","place_name":"Disneyland Park, 1313 Disneyland Dr, Anaheim, California 92802, United States","center":[-117.91899,33.810486],"geometry":{"coordinates":[-117.91899,33.810486],"type":"Point"},"context":[{"id":"neighborhood.294479","text":"Anaheim Resort"},{"id":"postcode.4074307310154980","text":"92802"},{"id":"place.7749226041161420","wikidata":"Q49247","text":"Anaheim"},{"id":"region.11319063928738010","short_code":"US-CA","wikidata":"Q99","text":"California"},{"id":"country.9053006287256050","short_code":"us","wikidata":"Q30","text":"United States"}]},{"id":"poi.1279900254454","type":"Feature","place_type":["poi"],"relevance":1,"text":"Disneyland® Paris","place_name":"Disneyland® Paris, Boulevard du Grand Fossé, Chessy, Seine-et-Marne 77700, France","center":[2.778511,48.870895],"geometry":{"coordinates":[2.778511,48.870895],"type":"Point"},"context":[{"id":"postcode.8713036370381920","text":"77700"},{"id":"place.14012543432112880","wikidata":"Q1076338","text":"Chessy"},{"id":"region.15077538089479390","short_code":"FR-77","wikidata":"Q12753","text":"Seine-et-Marne"},{"id":"country.9759535382641660","short_code":"fr","wikidata":"Q142","text":"France"}]},{"id":"poi.1340029846861","type":"Feature","place_type":["poi"],"relevance":1,"text":"Disneyland Dream Suite","place_name":"Disneyland Dream Suite, New Orleans Square, Anaheim, California 92802, United States","center":[-117.92076,33.811314],"geometry":{"coordinates":[-117.92076,33.811314],"type":"Point"},"context":[{"id":"neighborhood.294479","text":"Anaheim Resort"},{"id":"postcode.4074307310154980","text":"92802"},{"id":"place.7749226041161420","wikidata":"Q49247","text":"Anaheim"},{"id":"region.11319063928738010","short_code":"US-CA","wikidata":"Q99","text":"California"},{"id":"country.9053006287256050","short_code":"us","wikidata":"Q30","text":"United States"}]}],"attribution":"NOTICE: © 2018 Mapbox and its suppliers. All rights reserved. Use of this data is subject to the Mapbox Terms of Service (https://www.mapbox.com/about/maps/). This response and the information it contains may not be retained. POI(s) provided by Foursquare."}

    def json(self):
        return self.content


def test_setting_place_one(monkeypatch):
    """ test for coordinates arc de triomphe """
    result = {'coord': [2.779718, 48.87031], 'place': 'Disneyland Hotel, Disneyland® Paris, Chessy, Seine-et-Marne 77700, France'}

    def mockreturn(request, access):
        return MyResponse()

    monkeypatch.setattr(Geocoder, 'forward', mockreturn)
    assert Coord.setting_place('disneyland') == result

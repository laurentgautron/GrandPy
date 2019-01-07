""" modules for localise place """
from mapbox import Geocoder

class Coord:

    @staticmethod
    def number(place):

        geocoder = Geocoder(access_token='pk.eyJ1IjoidXNodWFuZ28iLCJhIjoiY2pxZ3Eyd2JmNTE5YjQ4ank5YzBqMG1neCJ9.DVSLrBIEeZzjU2e3GY17dQ')
        response = geocoder.forward('{}, Paris'.format(place))
        local = response.json()['features'][0]
        print(type(local['geometry']['coordinates']))
        return local['geometry']['coordinates']

""" modules for localise place """
from mapbox import Geocoder


class Coord:

    @staticmethod
    def setting_place(place):
        """ static method to find coordinates of the place """

        geocoder = Geocoder(access_token='pk.eyJ1IjoidXNodWFuZ28iLCJhIjoiY2pxZ3Eyd2JmNTE5YjQ4ank5YzBqMG1neCJ9.DVSLrBIEeZzjU2e3GY17dQ')
        response = geocoder.forward('{}'.format(place))
        print("la response", response)
        localise = response.json()
        print("le json", type(localise))
        print('les features: ', localise['features'][0])
        setting = {}
        if localise['features'][0]:
            setting = {"coord": localise['features'][0]['geometry']['coordinates'],
                       "place": localise['features'][0]['place_name']}
        return setting

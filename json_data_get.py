import json
import urllib.request

"""
This class processes json data from ourworldindata and generates x and y axis
"""


class CovidDataProcess(object):

    '''
    This class processes raw data from our world in data.
    '''

    def __init__(self, country, x_axis, y_axis):
        self.country = country
        self.x_axis = x_axis
        self.y_axis = y_axis

    def databuild(self):

        '''
        Returns raw_data which is a sliced json object from ourworldindata huge json
        '''

        with urllib.request.urlopen("https://covid.ourworldindata.org/data/owid-covid-data.json") as url:
            data = json.loads(url.read().decode())

        raw_data = data.get(self.country, {}).get('data')

        return raw_data

    def generate_x_axis(self):
        '''
        Almost self-explanatory, returns the values to be used as x-axis
        '''

        x_axis = []
        jsoned_data = CovidDataProcess.databuild(self)

        for values in jsoned_data:
            x_values = values.get(self.x_axis)
            x_axis.append(x_values)

        return x_axis

    def generate_y_axis(self):
        '''
        Return values to be used as y_axis
        '''
        y_axis = []
        jsoned_data = CovidDataProcess.databuild(self)

        for values in jsoned_data:
            y_values = values.get(self.y_axis)
            y_axis.append(y_values)

        return y_axis


class GraphConstructor(CovidDataProcess):

    def __init__(self, country, x_axis, y_axis):
        super().__init__(country, x_axis, y_axis)
        self.country = country
        self.x_axis = x_axis
        self.y_axis = y_axis



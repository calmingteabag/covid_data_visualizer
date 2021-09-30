from process_csv import ProcessCsv
import pandas as pd

class Csvgraphs(ProcessCsv):

    def __init__(self, index_column, file=None, x_axis=None, y_axis=None, values=None):
        super().__init__(index_column, file, x_axis)
        self.y_axis = y_axis
        self.values = values

    def generate_x_y(self):
        dataframe = ProcessCsv.csv_slicer(self)
        extract_x = dataframe.loc[self.values, self.x_axis]
        extract_y = dataframe.loc[self.values, self.y_axis]

        return extract_x, extract_y


# example: gen time graph for all 'gol' values using 'values_a' column in test_csv
mygraph = Csvgraphs('name', "C:\\Users\\Kamo\\PycharmProjects\\covid_data_visualizer\\data\\test_csv.CSV",
                    'time', 'values_a', 'gol')

x = mygraph.generate_x_y()
print(x)
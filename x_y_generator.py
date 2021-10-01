from process_csv import ProcessCsv
import pandas as pd


class Csvgraphs(ProcessCsv):

    def __init__(self, index_column, file=None, x_axis=None, y_axis=None, values=None, separator=None):
        super().__init__(index_column, file, x_axis, separator)
        self.y_axis = y_axis
        self.values = values
        self.separator = separator

    def generate_x_y(self):
        dataframe = ProcessCsv.csv_slicer(self)
        extract_x = dataframe.loc[self.values, self.x_axis]
        extract_y = dataframe.loc[self.values, self.y_axis]

        return extract_x, extract_y

import pandas as pd
import matplotlib.pyplot as plt

'''
Class to process csv files and return values for x-axis and y-axis.

index_column (str): Pandas read_csv() needs 'index_col' parameter to track which values to get from the
                    file. This class specifies its value because without it, pandas method creates its
                    own index starting from '0'. It may be ok for small files, but makes impossible sometimes
                    to retrieve certain values.
                    
file (str): file to read
x_axis (str): which column to use as x_axis
y_axis (str): which column to use as y_axis
values (str): which values from index_column to read from

Since the csv file is huge, we need to process it two times: First to get the columns we want (in this
case, dates and covid values) and another to select values from a country.
'''


class ProcessCsv:

    def __init__(
            self,
            index_column,
            file=None,
            x_axis=None,
            y_axis=None,
            country=None,
            separator=None,
            x_axis_spacing=None,
            plot_title=None,
            plot_y_label=None

    ):
        self.index_column = index_column
        self.file = file
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.country = country
        self.separator = separator
        self.x_axis_spacing = x_axis_spacing
        self.plot_title = plot_title
        self.plot_y_label = plot_y_label

    def __csv_slicer(self):
        # returns all data from selected columns

        sliced_csv = pd.read_csv(self.file, sep=self.separator, index_col=self.index_column)
        data_frame = pd.DataFrame(sliced_csv)

        return data_frame

    def country_csv(self):
        # returns dataframe from country

        full_dataframe = ProcessCsv.__csv_slicer(self)
        new_dataframe = full_dataframe.loc[self.country, [self.x_axis, self.y_axis]]
        new_dataframe = new_dataframe.set_index(self.x_axis)

        return new_dataframe





import pandas as pd

'''
Class to process csv files and return values for x-axis and y-axis.

index_column (str): Pandas read_csv() needs 'index_col' parameter to track which values to get from the
                    file. This class specifies its value because without it, this pandas method creates its
                    own index starting from '0' which makes impossible to locate which values from a column
                    pandas needs to get its values from. 
                    
file (str): file to read
x_axis (str): which column to use as x_axis
y_axis (str): which column to use as y_axis
values (str): which values from index_column to read from
'''


class ProcessCsv:

    def __init__(self, index_column, file=None, x_axis=None, separator=None):
        self.index_column = index_column
        self.file = file
        self.x_axis = x_axis
        self.separator = separator

    def csv_slicer(self):
        """
        Returns
        """
        sliced_csv = pd.read_csv(self.file, sep=self.separator, index_col=self.index_column)
        data_frame = pd.DataFrame(sliced_csv)

        return data_frame

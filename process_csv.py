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

    def __init__(self, index_column, file=None, x_axis=None):
        self.index_column = index_column
        self.file = file
        self.x_axis = x_axis

        # self.y_axis = y_axis
        # self.values = values

    def name(self):
        pass

    def csv_slicer(self):
        """
        Returns x and y values
        """
        sliced_csv = pd.read_csv(self.file, sep=';', index_col=self.index_column)
        # maybe return only sliced_csv or only dataframe
        # and process each axis separately own its own class
        data_frame = pd.DataFrame(sliced_csv)

        # x_values = data_frame.loc[self.values, self.x_axis]
        # y_values = data_frame.loc[self.values, self.y_axis]

        return data_frame


# mygraph = ProcessCsv('name', "C:\\Users\\Kamo\\PycharmProjects\\covid_data_visualizer\\data\\test_csv.CSV",
# 'var_init', 'var_end', 'gol')
# mygraph_values = mygraph.csv_slicer()

'''
Steps to be taken for each graph type (as it is - subject to change)
1 - instantiate processing class with specific x, y values of the desired graph
2 - untuple x and y into two lists (containing x, and y values)
3 - call matplotlib to plot
4 - call matplot again to label
5 - save matplot result on a file

Still have to decide to just do it raw by just running a single class
or create specific classes for each graph

'''

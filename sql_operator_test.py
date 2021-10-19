import mysql.connector as msqlc
from json_x_y_generator import GraphConstructor
import json
import urllib.request


class SqlOperator:

    def __init__(
            self,
            table_name,
            country_code,
            dbase=msqlc.connect(
                host='127.0.0.1',
                user='root',
                password='12345',
                database='kamodb'),
    ):
        self.table_name = table_name
        self.country_code = country_code
        self.dbase = dbase
        self.cursor = dbase.cursor()
        self.data = json.loads(urllib.request.urlopen("https://covid.ourworldindata.org/data/owid-covid-data.json")
                               .read().decode())

    def create_table(self, id_column_name):
        """
        Creates a mySQL table.

        :param id_column_name: name of primary key column
        """

        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS {} ({} INT AUTO_INCREMENT PRIMARY KEY)'.format(
                self.table_name, id_column_name
            )
        )
        self.dbase.commit()

    def __get_keys(self, data_get):
        """
        Returns a list of column names.

        :param 'data_get': Parameter to get data from 'data' dict.
        :return: 'column_names', which is a list of column names.

        For this class, self.country_code is passed as a parameter for data_get because of how
        'data' is organized - Inside 'data', all relevant data is organized within  'country-code'.
        """

        country_data = self.data.get(data_get, {}).get('data')
        temp_dict = country_data[15]  # picks a random dict entry just to get keys
        column_names = list(temp_dict.keys())

        return column_names

    def add_columns(self, col_def):
        """
        Creates columns based on what __get_keys() method returns as values.

        :param col_def: mySQL column definitions, as in VARCHAR, DATE, INT, etc


        """

        for values in self.__get_keys(self.country_code):
            if values == 'date':
                self.cursor.execute(
                    'ALTER TABLE {} ADD {} {}'.format(self.table_name, values, 'DATE')
                )
                self.dbase.commit()
            else:
                self.cursor.execute(
                    'ALTER TABLE {} ADD {} {}'.format(self.table_name, values, col_def)
                )
                self.dbase.commit()

    def set_primary(self):  # populates first data column with dates BUT DOESN'T WORK
        full_data = self.data.get(self.country_code, {}).get('data')
        date_list = []
        for values in full_data:
            key_values = values.get('date')
            date_list.append(key_values)

        # return date_list[0]
        prepared_list = [list([item]) for item in date_list]
        insert_date = list(prepared_list[0])
        self.cursor.execute('INSERT INTO {} ({}) VALUES ({})'.format(self.table_name, 'date', insert_date))
        self.dbase.commit()


    def insert_data(self):
        # ok this method kind of works
        # problem is it creates a single row for each column value but what we need is the next
        # set of values starting from where the previous set started.
        # example:
        #
        # id_col    col_a       col_b
        #       1   value_1     value_1
        #       2   value_2     value_2
        #       3   value_3     value_3
        #
        # instead, it is doing this
        #
        # id_col    col_a       col_b
        #       1   value_1     null
        #       2   value_2     null
        #       3   value_3     null
        #       4   null        value_1
        #       5   null        value_2
        #       6   null        value_3


        col_list_names = self.__get_keys(self.country_code)
        processed_data = self.data.get(self.country_code, {}).get('data')

        for col_name in col_list_names:

            '''
            What this does is, for each name in 'col_name'
            Iterate over values in processed_data that MATCHES current 'col_name' and
             append values to a temporary list (called 'temp_list')
            
            Then prepare data to the weird way mysql cursor uses with list([item])
            and execute cursor to insert data
            '''

            temp_list = []
            for values in processed_data:
                temp_values = values.get(str(col_name))
                temp_list.append(temp_values)

            prepared_list = [list([item]) for item in temp_list]
            self.cursor.executemany(u'INSERT IGNORE INTO {} ({}) VALUES (%s)'.format(self.table_name, col_name),
                                    prepared_list)
            self.dbase.commit()

    def del_data(self, column_name, data):
        self.cursor.execute(
            'DELETE FROM {} WHERE {} = {}'.format(self.table_name, column_name, data)
        )

    def update_data(self, column_name, data, cond_column, cond_value):
        self.cursor.execute(
            'UPDATE {} SET {} = {} WHERE {} = {} '.format(self.table_name, column_name, data, cond_column, cond_value)
        )

    def delete_column(self, column_name):
        pass

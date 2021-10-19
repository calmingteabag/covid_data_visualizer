import mysql.connector as msqlc
from json_x_y_generator import GraphConstructor
import json
import urllib.request

'''
This class creates and modifies a single SQL table.

'mysql.connector' uses something called 'cursor' to do sql operations and for that to work it 
needs to be instantiated inside class constructor
'''


class SqlOperator:

    def __init__(
            self,
            table_name=None,
            dbase=msqlc.connect(
                host='127.0.0.1',
                user='root',
                password='12345',
                database='kamodb'
            ),

    ):
        self.table_name = table_name
        self.dbase = dbase
        self.cursor = dbase.cursor()
        self.datalist = []

    # operator functions
    def create_table(self):
        # As the method name suggests, creates a new sql table if it doesn't already exists

        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS {} ( \
                covid_id INT AUTO_INCREMENT PRIMARY KEY, \
                covid_date VARCHAR(10), \
                total_cases VARCHAR(10), \
                new_cases VARCHAR(10), \
                new_cases_smoothed VARCHAR(10), \
                total_deaths VARCHAR(10), \
                new_deaths VARCHAR(10), \
                new_deaths_smoothed VARCHAR(10) \
            )'.format(self.table_name)
        )

    def get_data(self, country, get_values):
        # Gets specific json data and adds into a list

        with urllib.request.urlopen("https://covid.ourworldindata.org/data/owid-covid-data.json") as url:
            data = json.loads(url.read().decode())

        process_data = data.get(country, {}).get('data')

        for values in process_data:
            temp_values = values.get(get_values)
            self.datalist.append(temp_values)

    def insert_data(self, column_name):
        # Insert values from list and resets it

        values = [list([item]) for item in self.datalist]

        self.cursor.executemany(u'INSERT IGNORE INTO {} ({}) VALUES (%s)'.format(self.table_name, column_name), values)
        self.dbase.commit()
        self.datalist = []

    def del_data(self, column_name, data):
        self.cursor.execute(
            'DELETE FROM {} WHERE {} = {}'.format(self.table_name, column_name, data)
        )

    def update_data(self, column_name, data, cond_column, cond_value):
        self.cursor.execute(
            'UPDATE {} SET {} = {} WHERE {} = {} '.format(self.table_name, column_name, data, cond_column, cond_value)
        )

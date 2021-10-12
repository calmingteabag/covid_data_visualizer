import mysql.connector as msqlc

'''
This class creates and modifies a single SQL table.

Before using this class, you should frst use json_x_y_generator class to create
some arrays with data or create some mock list so there is some data to be
worked with.

After that, a cursor needs to be instantiated since it's how 'mysql.connector' 
works to execute operations on mysql tables. Also don't forget to 'cursor_name.commit()' to
apply any changes'

Finally methods are available to use. SQL works by specifying a table, column and values to be
worked with. So table argument is automatically given by 'self.country' (SqlOperator uses 
'self.country' as a table name), 'column_data' and 'data' refers to a column (self explanatory) and 
values to be modified/added/etc.
'''


class SqlOperator:

    def __init__(
            self,
            host,
            user,
            password,
            dbase,
            cursor_name,
            connector_name,
            country,
    ):
        self.host = host
        self.user = user
        self.password = password
        self.dbase = dbase
        self.cursor_name = cursor_name
        self.connector_name = connector_name
        self.country = country

    def create_table(self):

        self.cursor_name.execute(
            'CREATE TABLE IF NOT EXISTS {} ( \
                covid_id INT AUTO_INCREMENT PRIMARY KEY, \
                covid_date VARCHAR(10), \
                total_cases VARCHAR(10), \
                new_cases VARCHAR(10), \
                new_cases_smoothed VARCHAR(10), \
                total_deaths VARCHAR(10), \
                new_deaths VARCHAR(10), \
                new_deaths_smoothed VARCHAR(10) \
            )'.format(self.country)
        )

    def insert_data(self, column_name, data):

        self.cursor_name.execute(
            'INSERT IGNORE INTO {}({}) VALUES ({}) '.format(self.country, column_name, data)
        )

    def del_data(self, column_name, data):

        self.cursor_name.execute(
            'DELETE FROM {} WHERE {} = {}'.format(self.country, column_name, data)
        )

    def update_data(self, column_name, data, cond_column, cond_value):

        self.cursor_name.execute(
            'UPDATE {} SET {} = {} WHERE {} = {} '.format(self.country, column_name, data, cond_column, cond_value)
        )

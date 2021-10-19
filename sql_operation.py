from sql_operator_class_test import SqlOperator

operator = SqlOperator('brazil')

# operator.get_data('BRA', 'new_cases')
# print(operator.datalist)
# operator.insert_data('new_cases')

# operator.create_table()
operator.get_data('BRA', 'new_cases')
operator.insert_data()
# operator.del_data('new_cases', '242142')
# operator.updata_data('total_cases', 14214124, 'covid_od',)

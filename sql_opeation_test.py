from sql_operator import SqlOperator


bra = SqlOperator('fucker', 'BRA')
bra.create_table('table_id')
# bra.add_columns('VARCHAR(15)')

x = bra.set_primary()
print(x)


# bra.insert_data()






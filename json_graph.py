from json_x_y_generator import GraphConstructor
import matplotlib.pyplot as plt
import matplotlib.pyplot as ticker
import mysql.connector

brasil = GraphConstructor('BRA', 'date', 'new_cases_smoothed')
br_data = brasil.databuild()

dates = brasil.generate_x_axis()
cases = brasil.generate_y_axis()

fig, ax = plt.subplots()
ax.plot(dates, cases)
ax.tick_params(rotation=90, axis='x')
ax.set_ylabel('Casos')
ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

fig.subplots_adjust(bottom=0.3)
plt.title('Média movel casos covid')
plt.xticks(rotation=90)
plt.show()

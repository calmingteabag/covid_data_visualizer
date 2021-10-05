import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from process_csv import ProcessCsv

br_dataf = ProcessCsv('location',
                      "C:\\Users\\Kamo\\PycharmProjects\\covid_data_visualizer\\data\\owid-covid-data.csv",
                      'date',
                      'new_cases_smoothed',
                      'Brazil',
                      ',',
                      60,
                      'Covid Data BR',
                      'Casos')


sliced_csv = br_dataf.country_csv()

br_dataf_2 = ProcessCsv('location',
                        "C:\\Users\\Kamo\\PycharmProjects\\covid_data_visualizer\\data\\owid-covid-data.csv",
                        'date',
                        'new_deaths_smoothed',
                        'Brazil',
                        ',',
                        60,
                        'Covid Data BR',
                        'Deaths')

sliced_csv_2 = br_dataf_2.country_csv()

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.plot(sliced_csv, color=color)
spacing = br_dataf.x_axis_spacing
ax1.tick_params(labelcolor=color, axis='y')
ax1.set_ylabel("Casos")
ax1.tick_params(rotation=90, axis='x')
ax1.grid()
ax1.xaxis.set_major_locator(ticker.MultipleLocator(spacing))

ax2 = ax1.twinx()

color2 = 'tab:red'
ax2.plot(sliced_csv_2, color=color2)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(spacing))
ax2.set_ylabel("Mortes")
ax2.tick_params(labelcolor=color2)


fig.subplots_adjust(bottom=0.3)
plt.title('Covid BR')
plt.xticks(rotation=90)

plt.show()

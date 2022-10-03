import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

years = df['Year']
temps = df['Value']

x = []
y = []
for year in years:
    x.append(year)
for temp in temps:
    y.append(temp)

plt.plot(x, y, color='r', marker='o', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.title('Global temperature')
plt.show()

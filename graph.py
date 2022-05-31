import plotly.graph_objects as go
import matplotlib.pyplot as plt
from datetime import datetime
import json

list_temp = list()
list_date = list()

def parse():
    with open("D:\Python\Temp-Humidity-RPI-Sensor\data.json", "r") as f:
        data = json.load(f)

    data_inner = data["data"]
    for x in data_inner:
        n = x['temperature']
        list_temp.append(n)
        #list_date.append(datetime.strptime(x['date'], "%d/%m/%y %H:%M:%S.%f"))

parse()

plt.plot(list_temp)
print(list_temp)
plt.show()







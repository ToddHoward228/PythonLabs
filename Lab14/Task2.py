import matplotlib.pyplot as plot
import csv

data_base = open("Primary_Education.csv", "r") 
values = list(csv.DictReader(data_base, delimiter = ";"))

y = list()
x_1 = list()
x_2 = list()

for year in range(2004, 2015):
    y.append(str(year))
    x_1.append(float(values[0][str(year)]))
    x_2.append(float(values[1][str(year)]))

plot.plot(y, x_1, x_2)
plot.grid(True)
plot.title("Відсток початкової школи")
plot.ylabel("Відсоток")
plot.xlabel("Рік")

plot.show()
    

def plot_bar_chart(country, data):
    plot.bar(range(1, len(data)+1), data, color='darkblue')
    plot.xlabel('Рік')
    plot.ylabel('Відсоток')
    plot.title(country)
    plot.xticks(range(1, len(data)+1))
    plot.grid(True)
    plot.show()

country_input = input("Введіть назву країни (Україна або Південна Корея): ")

if country_input.lower() == 'україна':
    plot_bar_chart("відсоток по Україні", x_1)
elif country_input.lower() == 'південна корея':
    plot_bar_chart("відсоток Південної Кореї", x_2)
else:
    print("Країна не знайдена.")

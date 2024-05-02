import matplotlib.pyplot as function_plot
import numpy
from module import f

x = numpy.linspace(-5, 5, 100)

y = x.copy()

for i in range(0, len(x)):
    y[i] = f(x[i])

function_plot.plot(x, y, label = "значення y", linestyle = "-", color = "darkred", linewidth = 1)

#Налаштування графіка
function_plot.grid(True)
function_plot.title("Графік функції")
function_plot.legend()
function_plot.ylabel("f(x)", color = "darkblue")
function_plot.xlabel("x", color = "darkblue")

#Вивід графіка
function_plot.show()

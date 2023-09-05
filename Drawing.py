import numpy
import matplotlib.pyplot as plt
import Colors

def drawPieChart(labels, sizes, colors):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%',
       pctdistance=1.25, labeldistance=.6)
    plt.show()


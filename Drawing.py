import numpy
import matplotlib
import Colors

def drawPieChart(labels, sizes):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)


import numpy
import matplotlib.pyplot as plt
import Colors
from matplotlib.ticker import MaxNLocator


def drawPieChart(labels, sizes, colors):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors = colors, autopct='%1.1f%%',
       pctdistance=1.25, labeldistance=.6)
    plt.show()

def drawBarGraph(xlabel, ylabel, xval, yval):
    ax = plt.figure().gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.bar(xval, yval)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_xlim(left=-0.5, right=max(xval)+0.5, auto=False)
    ax.set_ylim(bottom=0, top=max(yval)+1, auto=False)
    plt.show()


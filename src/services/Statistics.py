from interface import Colors, Drawing
from mathematics import MathOp


class Stats:
    def __init__(self, n):
        self.cols = [Colors.Colors(), []]
        mvs = []
        self.mv = []
        self.size = n

    def getColors(self):
        l = [self.cols[0].copy(), self.cols[1].copy()]
        return l

    def getMv(self):
        return self.mv.copy()

    def getSize(self):
        return self.size

    def setColors(self):
        self.cols[0].setCols()

    def setMv(self):
        mx = int(input('What is the maximum mana value? '))
        mvs = []
        done = False
        while not done:
            for val in range(mx+1):
                if val == 0:
                    i = int(input('How many cards of mana value ' + str(val) + ' does your deck contain? (Lands '
                                                                               'excluded) '))
                    mvs.append(i)
                else:
                    i = int(input('How many cards of mana value ' + str(val) + ' does your deck contain? '))
                    mvs.append(i)
            if sum(mvs) > self.getSize():
                print('More cards than allowed, try again')
                mvs = []
                self.setMv()
            else:
                self.mv = mvs
                done = True

    def setDevotion(self):
        done = False
        cols = []
        while not done:
            for col in self.getColors()[0].getCols():
                i = int(
                    input('How many mana symbols of ' + col.upper() + ' does your deck contain in all mana costs? '))
                cols.append(i)
            if sum(self.cols[1]) > self.totMv():
                print('More mana symbols than total mana value, try again')
                cols = []
            else:
                done = True
                self.cols[1] = cols

    def totMv(self):
        som = 0
        for i in range(len(self.mv)):
            if self.mv[i] != 0:
                som = som + i * self.mv[i]
        return som

    def averageMv(self):
        n = 0
        som = 0
        for i in range(len(self.mv)):
            if self.mv[i] != 0:
                n = n + self.mv[i]
                som = som + i*self.mv[i]
        if n > 0:
            return som / n
        else:
            return 0

    def landsNeeded(self):
        av = self.averageMv()
        k = round(av)
        N = self.getSize()
        n = 7
        K = 20
        while 0.5 > Elementary_Operations.hypGemProb(k, N, K, n) and K <= self.getSize()-sum(self.getMv()):
            K = K+1
        return K

    def colorManaPercentage(self):
        freqs = MathOp.frequency(self.getColors()[1])
        labels = self.getColorMTGNames()
        colors = self.getColorNameLst()
        Drawing.drawPieChart(labels, freqs, colors)

    def getColorNameLst(self):
        names = []
        for col in self.getColors()[0].getCols():
            if col.lower() == 'u':
                names.append('blue')
            elif col.lower() == 'r':
                names.append('red')
            elif col.lower() == 'g':
                names.append('green')
            elif col.lower() == 'w':
                names.append('#F3CF89')
            elif col.lower() == 'b':
                names.append('#A2998A')
        return names

    def getColorMTGNames(self):
        names = []
        for col in self.getColors()[0].getCols():
            if col.lower() == 'u':
                names.append('Island')
            elif col.lower() == 'r':
                names.append('Mountain')
            elif col.lower() == 'g':
                names.append('Forest')
            elif col.lower() == 'w':
                names.append('Plains')
            elif col.lower() == 'b':
                names.append('Swamp')
        return names

    def mvDistribution(self):
        xlabel = 'Mana Value'
        ylabel = 'Amount of cards'
        xval = [i for i in range(0, len(self.getMv()))]
        yval = self.getMv()
        Drawing.drawBarGraph(xlabel, ylabel, xval, yval)


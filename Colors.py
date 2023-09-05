class Colors:
    def __init__(self):
        self.colors = []

    def addCol(self, col):
        if col in ['u', 'b', 'w', 'r', 'g'] and col not in self.colors:
            self.colors.append(col.upper())
        else:
            raise ValueError('Invalid input')

    def setCols(self):
        added = []
        print('Use the abbreviations W,U,B,R,G')
        col = input("Which colors do you play? (Type 0 to stop) ")
        if col == '0':
            cont = False
        else:
            cont = True
        while cont:
            try:
                if col == '0':
                    cont = False
                else:
                    self.addCol(col.lower())
                    added.append(col.lower())
                    if ('w' in added and 'u' in added and 'r' in added and 'g' in added and 'b' in added):
                        cont = False
                    else:
                        col = input("Which other colors do you play? (Type 0 to stop) ")
            except ValueError:
                print('Invalid input, try again')
                col = input("Which other colors do you play? (Type 0 to stop) ")


    def setCol2(self, lst):
        self.colors = lst

    def getCols(self):
        return self.colors.copy()

    def copy(self):
        cols = self.getCols().copy()
        newColors = Colors()
        newColors.setCol2(cols)
        return newColors

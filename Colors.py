class Colors:
    def __init__(self):
        self.colors = []

    def addCol(self, col):
        if col in ['u', 'b', 'w', 'r', 'g'] and col not in self.colors:
            self.colors.append(col)
        else:
            raise ValueError('Invalid input')

    def setCols(self):
        print('Type 0 to stop')
        print('Use the abbreviations W,U,B,R,G')
        col = input("Which colors do you play? ").lower()
        if col == '0':
            cont = False
        else:
            cont = True
        while cont:
            try:
                self.addCol(col)
                col = input("Which other colors do you play? ").lower()
                if col == '0':
                    cont = False
                else:
                    cont = True
            except ValueError:
                print('Invalid input, try again')
                col = input("Which other colors do you play? ").lower()
                if col == '0':
                    cont = False
                else:
                    cont = True

    def setCol2(self, lst):
        self.colors = lst

    def getCols(self):
        return self.colors.copy()

    def copy(self):
        cols = self.getCols().copy()
        newColors = Colors()
        newColors.setCol2(cols)
        return newColors

from matplotlib.lines import Line2D

class pltS:
    def __init__(self, x, y, line: Line2D, patch):
        self.x = x
        self.y = y
        self.line = line
        self.patch = patch

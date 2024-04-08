import PyQt6.QtGui as gui

def parseQt(colVal: str, alpha):
    colVal = colVal[1:len(colVal - 1)]
    colVal = int(colVal, 16)
    return gui.QColor(colVal)
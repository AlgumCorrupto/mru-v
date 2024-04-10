import PyQt6.QtGui as gui
import json
import os

# alpha here goes from 0 to 255
def parseQt(colVal: str, alpha: int):
    colVal = colVal[1:len(colVal)]
    colVal = int(colVal, 16)
    return gui.QColor((colVal >> 8*2) & 0xFF, (colVal >> 8*1) & 0xFF, (colVal >> 8*0) & 0xFF, alpha)

# ya pass string here
def parseMat(colVal: str, alpha: str):
    return colVal + alpha

class color:
    def __init__(self):
        file = open("assets/colors.json", "r")
        buffer = json.loads(file.read())
        self.qtNormal = []
        self.qtBg = []
        self.qtGrayDim = parseQt(buffer["gray_dim"], 255)
        self.qtFg = parseQt(buffer["fg"], 255)
        self.qtDiff = []

        self.matNormal = []
        self.matBg = []
        self.matGrayDim = parseMat(buffer["gray_dim"], 'FF')
        self.matFg = parseMat(buffer["fg"], 'FF')
        self.matDiff = []

        buffNormal = buffer["normal"]
        for normal in buffNormal:
            self.qtNormal.append(parseQt(buffNormal[normal], 255))
            self.matNormal.append(parseMat(buffNormal[normal], "FF"))

        buffBg = buffer["bg"]
        for bg in buffBg:
            self.qtBg.append(parseQt(buffBg[bg], 255))
            self.matBg.append(parseMat(buffBg[bg], "FF"))

        buffDiff = buffer["diff"]
        for diff in buffDiff:
            self.qtDiff.append(parseQt(buffDiff[diff], 255))
            self.matDiff.append(parseMat(buffDiff[diff], "FF"))
            
clr = color()
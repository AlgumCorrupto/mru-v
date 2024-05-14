import sys
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor, QFont
from colorParser import clr
from runner import Runner

class scene(QGraphicsScene):
    def __init__(self, parent, view, sim):
        super().__init__(parent)
        self.elapsedTime = 0
        self.setSceneRect(0, 0, 400, 175)
        self.view = view
        self.view.setScene(self)
        self.text = self.addText("T={}, A={}, S={}, V={}".format(self.elapsedTime, 
                                                                       0, 
                                                                       0,
                                                                       0))
        self.text.setFont(QFont("Cursiv"))
        self.text.setDefaultTextColor(clr.qtFg)
        self.text.setScale(5)
        self.runners = [Runner(self, clr.qtNormal[3], sim, 0), None]
        self.addItem(self.runners[0])
        self.isRunning = False

    def run(self):
         self.text.setPos((self.view.width()/2) - ((self.text.boundingRect().width()*5)/2), ((self.height()/2)) - ((self.text.boundingRect().height()) * 5)/2)
         self.text.setPlainText("T={}, a={}, S={}, V={}".format(self.elapsedTime if self.elapsedTime > 0 else 0, 
                                                                self.runners[0].sim.dataArr[self.runners[0].index].acce, 
                                                                round(self.runners[0].sim.dataArr[self.runners[0].index].pos, 2),
                                                                self.runners[0].sim.dataArr[self.runners[0].index].vel))                  
         if self.isRunning:
            print("renderer: {}".format(str(self.elapsedTime)))
            for runner in self.runners:
                if runner != None:
                    runner.update(self.elapsedTime)
            self.elapsedTime+= 1

         for runner in self.runners:
             if runner != None:
                 runner.setY((self.height()/2) - runner.scl/2)

    def createRunner(self, sim, index):
         self.runners[index] = Runner(self, clr.qtNormal[4], sim, 1)

    def pauseSim(self):
        self.isRunning = False

    def playSim(self):
        self.isRunning = True if not self.isRunning else False

    def resetSim(self):
        for runner in self.runners:
            runner.reset()
        self.elapsedTime = 0

    def findRunner(self, id):
        for runner in self.runners:
            if runner.id  == id:
                return runner    
        
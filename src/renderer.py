import sys
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor, QFont
from colorParser import clr

class scene(QGraphicsScene):
    def __init__(self, parent, view, sim):
        super().__init__(parent)
        self.elapsedTime = 0
        self.setSceneRect(0, 0, 400, 175)
        self.sim = sim
        self.view = view
        self.view.setScene(self)
        self.text = self.addText("T={}, A={}, S={}, V={}".format(self.elapsedTime, 
                                                                       self.sim.acce, 
                                                                       self.sim.dataArr[0].pos,
                                                                       self.sim.dataArr[0].vel))
        self.text.setFont(QFont("Cursiv"))
        self.text.setDefaultTextColor(clr.qtFg)
        self.text.setScale(5)
        self.runner = QGraphicsEllipseItem(0, 0, 100, 100)
        brush = QBrush(clr.qtNormal[3])
        self.runner.setBrush(brush)
        self.vel = self.sim.startVel
        self.addItem(self.runner)
        self.timer = QTimer()
        # i guess 100ms in qt and matplotlib are not the same thing :/
        self.timer.setInterval(62)
        self.timer.timeout.connect(self.run)
        self.isRunning = False
        self.timer.start()

    def run(self):
         self.text.setPos((self.view.width()/2) - ((self.text.boundingRect().width()*5)/2), ((self.height()/2)) - ((self.text.boundingRect().height()) * 5)/2)
         index = int(self.elapsedTime - self.sim.Time0) if int(self.elapsedTime - self.sim.Time0) >= 0 else 0
         self.text.setPlainText("T={}, a={}, S={}, V={}".format(self.elapsedTime, 
                                                                self.sim.acce, 
                                                                self.sim.dataArr[index].pos,
                                                                self.sim.dataArr[index].vel))
         if self.isRunning and self.elapsedTime < self.sim.TimeF:
            print("renderer: {}".format(str(self.elapsedTime)))
            if self.elapsedTime >= self.sim.Time0:
                pos = (self.runner.x() + (self.vel))
                self.runner.setX(pos)
                self.vel += self.sim.acce
            self.elapsedTime+= 1
         self.runner.setY((self.height()/2) - 100/2)


    def pauseSim(self):
        self.isRunning = False

    def playSim(self):
        self.isRunning = True if not self.isRunning else False

    def resetSim(self):
        self.runner.setPos(0, self.runner.y())
        self.vel = self.sim.startVel
        self.elapsedTime = 0
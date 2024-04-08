import sys
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QBrush, QColor, QFont

class scene(QGraphicsScene):
    def __init__(self, parent, view, sim):
        super().__init__(parent)
        self.setSceneRect(0, 0, 400, 175)
        self.sim = sim
        self.view = view
        self.view.setScene(self)
        self.text = self.addText("Representação")
        self.text.setScale(5)
        self.runner = QGraphicsEllipseItem(0, 0, 100, 100)
        brush = QBrush(QColor(255, 255, 0, 255))
        self.runner.setBrush(brush)
        self.vel = self.sim.startVel
        self.addItem(self.runner)
        self.elapsedTime = self.sim.Time0
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.run)
        self.isRunning = False
        self.timer.start()

    def run(self):
         self.text.setPos((self.view.width()/2) - ((self.text.boundingRect().width()*5)/2), ((self.height()/2)) - ((self.text.boundingRect().height()) * 5)/2)
         self.runner.setPos(self.runner.x(), (self.height()/2) - 100/2)
         if self.isRunning and self.elapsedTime < self.sim.TimeF:
            self.elapsedTime+=1
            pos = self.runner.x() + (self.vel)
            self.runner.setPos(pos, (self.height()/2) - 100/2)
            self.vel += self.sim.acce
            self.text.setPlainText("T={}, A={}, S={}, V={}".format(self.elapsedTime, 
                                                                   self.sim.acce, 
                                                                   self.sim.dataArr[int(self.elapsedTime - self.sim.Time0) - 1].pos,
                                                                   self.sim.dataArr[int(self.elapsedTime - self.sim.Time0) - 1].vel))

    def pauseSim(self):
        self.isRunning = False

    def playSim(self):
        self.isRunning = True if not self.isRunning else False

    def resetSim(self):
        self.runner.setPos(0, self.runner.y())
        self.vel = self.sim.startVel
        self.elapsedTime = self.sim.Time0
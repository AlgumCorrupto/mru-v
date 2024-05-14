from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene
from PyQt6.QtGui import QColor, QBrush, QPainter
from sim import Simulation

class Runner(QGraphicsEllipseItem):
    def __init__(self, parent: QGraphicsScene, color: QColor, sim: Simulation, id):
        super().__init__(sim.dataArr[0].pos, 0, 88, 88)
        brush = QBrush(color)
        self.setBrush(brush)
        self.scl = 88
        self.sim = sim
        self.id = id
        self.index = 0

    def update(self, elapsedTime):
        self.index = int(elapsedTime - self.sim.Time0) if int(elapsedTime - self.sim.Time0) < self.sim.TimeF else self.sim.TimeF
        if self.index < 0:
             self.index = 0
        if elapsedTime > self.sim.Time0 and elapsedTime < self.sim.TimeF:
                self.setX(self.sim.dataArr[self.index].pos)

        
    def reset(self):
         self.setPos(self.sim.startPos, self.y())        
    
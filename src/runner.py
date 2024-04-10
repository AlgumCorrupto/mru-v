from PyQt6.QtWidgets import QGraphicsEllipseItem, QGraphicsScene
from PyQt6.QtGui import QColor, QBrush

class Runner(QGraphicsEllipseItem):
    def __init__(self, parent: QGraphicsScene, color: QColor, vel: float, acce: float, position: float):
        super().__init__(parent)
        brush = QBrush(color)
        self.vel = vel
        self.acce = acce
        self.position = position
    
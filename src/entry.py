import sim
import window
import sys
import colorParser
from PyQt6.QtGui import QFont, QFontDatabase
from matplotlib import font_manager

import numpy as np

fontFiles = font_manager.fontManager.addfont('assets/CURSIV.TTF')

id = QFontDatabase.addApplicationFont("assets\CURSIV.TTF")

window.app.show()
window.app.activateWindow()
window.app.raise_()
window.qapp.exec()
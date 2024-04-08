import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QGraphicsView, QMenu, QLabel, QPushButton, QGroupBox
import PyQt6.QtWidgets as widgets
from graph import g
import sim
from configDialog import ConfigDialog

import numpy as np

#muito import ayy cabron
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
import renderer

class ApplicationWindow(QMainWindow):
    # devo modularizar esse construtor
    # feito :thumbs_up:
    def __init__(self):
        super().__init__()
        #self.setBaseSize(500, 1500)
        self._setupWindow()
        self._setupQGraphics()
        self._setupMenuBar()
        self._setupUtils()
        self._setupGraphs()
        self._setupConfigWidget()


    def contextMenuEvent(self, event):
        # Show the context menu
        self.context_menu.exec(event.globalPos())

    #setup window
    def _setupWindow(self):
        app_icon = QIcon()
        app_icon.addFile('assets/svt2.png', QSize(512, 512))
        self.setWindowIcon(app_icon)
        #self.setFixedHeight(500)
        self.setWindowTitle("Visualizador MRU")
        
        self._main = QtWidgets.QWidget()

        self.mainLayout = QtWidgets.QHBoxLayout(self._main)
        self.setCentralWidget(self._main)

        self.viewWidget = QtWidgets.QWidget()
        self.viewLayout = QtWidgets.QVBoxLayout(self.viewWidget)
        self.mainLayout.addWidget(self.viewWidget)

        self.rightWidget = QtWidgets.QWidget()
        self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
        self.mainLayout.addWidget(self.rightWidget)

        self.graph = QtWidgets.QWidget()
        self.graphLayout = QtWidgets.QHBoxLayout(self.graph)

        self.bottomWidget = QtWidgets.QWidget()
        self.bottomLayout = QtWidgets.QHBoxLayout(self.bottomWidget)

        self.viewLayout.addWidget(self.graph)
        
        self.viewLayout.addWidget(self.bottomWidget)
        self.viewLayout.setStretch(0, 6)
        self.viewLayout.setStretch(1, 4)


        self.viewLayout.setContentsMargins(0,0,0,0)
        

    def _setupUtils(self):
        self.utils = QWidget(self)
        utilsLayout = QVBoxLayout()
        self.utils.setLayout(utilsLayout)
        self.rightLayout.addWidget(self.utils)
        playBtn = QPushButton(self.bottomWidget)
        playBtn.setText("Pausar/Continuar")
        playBtn.clicked.connect(self.start)
        resetBtn = QPushButton(self.bottomWidget)
        resetBtn.setText("Resetar")
        resetBtn.clicked.connect(self.reset)

        utilsLayout.addWidget(playBtn)
        utilsLayout.addWidget(resetBtn)

    def _setupConfigWidget(self):
        self.ConfigWidget = QWidget(self)
        configLayout = widgets.QVBoxLayout(self.ConfigWidget)
        self.rightLayout.addWidget(self.ConfigWidget)

        alterarBtn = QPushButton(self.ConfigWidget)
        alterarBtn.setText("Alterar Params")
        self.configDialog = ConfigDialog(self) 
        configLayout.addWidget(alterarBtn)

        alterarBtn.clicked.connect(self.invokeCfgDialog)

    #setup QGraphics
    def _setupQGraphics(self):
        gView = QGraphicsView()
        gView.setAlignment(Qt.AlignmentFlag(1))
        gView.setMinimumWidth(1000)
        gView.setFixedHeight(176)
        self.gScene = renderer.scene(parent=self, view=gView, sim=sim.obj)
        self.bottomLayout.addWidget(self.gScene.view)
        self.gScene.view.show()

    def _setupGraphs(self):
        t = []
        s = []
        a = []
        v = []

        for dat in sim.obj.dataArr:
            t.append(dat.time)
            s.append(dat.pos)
            a.append(dat.acce)
            v.append(dat.vel)
        #gráfico S x T
        self.SGraph = g("S x T", t, "Tempo", s, "Distância", self)
        self.SGraph.plot()
        #gráfico A x T
        self.AGraph = g("A x T", t, "Tempo", a, "Aceleração", self)
        self.AGraph.plot()
        #gráfico V x T
        self.VGraph = g("V x T", t, "Tempo", v, "Velocidade", self)
        self.VGraph.plot()

    def _setupMenuBar(self):
        menuBar = self.menuBar()
        actionsMenu = QMenu("&Ações", self)
        menuBar.addMenu(actionsMenu)
        resetAct = actionsMenu.addAction("Resetar")
        playAct  = actionsMenu.addAction("Pausar/Tocar")

        resetAct.triggered.connect(self.reset)
        playAct.triggered.connect(self.start)

    def start(self):
        self.gScene.playSim()
        self.SGraph.play()
        self.AGraph.play()
        self.VGraph.play()

    def reset(self):
        self.gScene.resetSim()
        self.SGraph.reset()
        self.AGraph.reset()
        self.VGraph.reset()

    def invokeCfgDialog(self):
        self.configDialog.show()


qapp = QtWidgets.QApplication(sys.argv)
app = ApplicationWindow()
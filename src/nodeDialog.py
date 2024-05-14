import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
from data import Data
import graph

class NodeDialog(widgets.QDialog):
    def __init__(self, parent, simu):
        super().__init__()
        self._main = widgets.QWidget(self)
        self.mainLayout = widgets.QFormLayout(self._main)
        self.sim = simu
        self.parent = parent
        self.setWindowTitle("Noder 3000")
        self.initForms()

    def initForms(self):
        self.figLabel  = widgets.QLabel()
        self.figLabel.setText("Figura (começa do 0)")
        self.figIn     = widgets.QLineEdit()
        self.figIn.setText("0")

        self.acceLabel  = widgets.QLabel()
        self.acceLabel.setText("Aceleração")
        self.acceIn     = widgets.QLineEdit()
        self.acceIn.setText("0")

        self.timeFLabel = widgets.QLabel()
        self.timeFLabel.setText("Intervalo")
        self.timeFIn    = widgets.QLineEdit()
        self.timeFIn.setText(self.sim.TimeF.__str__())

        self.submitBtn  = widgets.QPushButton()
        self.submitBtn.setText("Atualizar")


        self.mainLayout.addWidget(self.acceLabel)
        self.mainLayout.addWidget(self.acceIn)

        self.mainLayout.addWidget(self.timeFLabel)
        self.mainLayout.addWidget(self.timeFIn)

        self.mainLayout.addWidget(self.submitBtn)

        self.submitBtn.clicked.connect(self.updateStuff)

        self.setFixedSize(165, 150)

    def updateStuff(self):
        self.parent.timer.stop()
        
        self.sim.addNode(int(self.timeFIn.text()), int(self.acceIn.text()))

        if not self.parent.gScene.findRunner(int(self.figIn.text())):
            msg = widgets.QMessageBox()
            
            msg.setWindowTitle("Erro ao processar formulário")
            msg.setText("Figura não encontrada.")
            msg.exec()
            return

        t = []
        s = []
        a = []
        v = []

        for dat in self.sim.dataArr:
            t.append(dat.time)
            s.append(dat.pos)
            a.append(dat.acce)
            v.append(dat.vel)
        
        self.parent.SGraph.setPlot(t, s)
        self.parent.AGraph.setPlot(t, a)
        self.parent.VGraph.setPlot(t, v)
        self.parent.gScene.sim = self.sim
        self.parent.reset()
        self.parent.timer.start()
        self.close()
        
    
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
from sim import obj, Simulation
from data import Data
import graph

class ConfigDialog(widgets.QDialog):
    def __init__(self, parent):
        super().__init__()
        self._main = widgets.QWidget(self)
        self.mainLayout = widgets.QFormLayout(self._main)
        self.parent = parent
        self.setWindowTitle("Configurator 3000")
        self.initForms()

    def initForms(self):
        self.velLabel = widgets.QLabel()
        self.velLabel.setText("Velocidade")
        self.velIn    = widgets.QLineEdit()
        self.velIn.setText(obj.startVel.__str__())

        self.acceLabel  = widgets.QLabel()
        self.acceLabel.setText("Aceleração")
        self.acceIn     = widgets.QLineEdit()
        self.acceIn.setText(obj.acce.__str__())

        self.time0Label = widgets.QLabel()
        self.time0Label.setText("Tempo Inicial")
        self.time0In    = widgets.QLineEdit()
        self.time0In.setText(obj.Time0.__str__())

        self.timeFLabel = widgets.QLabel()
        self.timeFLabel.setText("Tempo Final")
        self.timeFIn    = widgets.QLineEdit()
        self.timeFIn.setText(obj.TimeF.__str__())

        self.pos0Label  = widgets.QLabel()
        self.pos0Label.setText("Posição Inicial")
        self.pos0In     = widgets.QLineEdit()
        self.pos0In.setText(obj.startPos.__str__())

        self.submitBtn  = widgets.QPushButton()
        self.submitBtn.setText("Atualizar")

        self.mainLayout.addWidget(self.velLabel)
        self.mainLayout.addWidget(self.velIn)

        self.mainLayout.addWidget(self.acceLabel)
        self.mainLayout.addWidget(self.acceIn)

        self.mainLayout.addWidget(self.time0Label)
        self.mainLayout.addWidget(self.time0In)

        self.mainLayout.addWidget(self.timeFLabel)
        self.mainLayout.addWidget(self.timeFIn)

        self.mainLayout.addWidget(self.pos0Label)
        self.mainLayout.addWidget(self.pos0In)

        self.mainLayout.addWidget(self.submitBtn)

        self.submitBtn.clicked.connect(self.updateStuff)

        self.setFixedSize(165, 300)

    def updateStuff(self):
        if int(self.time0In.text() > self.timeFIn.text()):
            msg = widgets.QMessageBox()
            msg.setWindowTitle("Erro ao processar formulário")
            msg.setText("Tempo final não pode ser menor que o tempo inicial.\nTempo não pode conter casas decimais")
            msg.exec()
            return
        try:
            obj =  Simulation(
            float(self.velIn.text()),
            float(self.pos0In.text()),
            float(self.acceIn.text()),
            int(self.time0In.text()),
            int(self.timeFIn.text())
            )
        except:
            msg = widgets.QMessageBox()
            msg.setWindowTitle("Erro ao processar formulário")
            msg.setText("Use ponto final (.) para informar casas decimais ao invés da vírgula (,).\nNão é permitido caracteres alfabéticos.\nTempo só pode ser expressado em números inteiros")
            msg.exec()
            return

        t = []
        s = []
        a = []
        v = []

        for dat in obj.dataArr:
            t.append(dat.time)
            s.append(dat.pos)
            a.append(dat.acce)
            v.append(dat.vel)
        
        self.parent.SGraph.setPlot(t, s)
        self.parent.AGraph.setPlot(t, a)
        self.parent.VGraph.setPlot(t, v)
        self.parent.gScene.sim = obj
        self.parent.reset()

        
    
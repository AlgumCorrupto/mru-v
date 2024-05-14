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

        self.figWid = widgets.QWidget()
        self.figLay = widgets.QHBoxLayout()

        self.fig1 = widgets.QPushButton("Fig 1")
        self.fig1.setCheckable(True)
        self.fig2 = widgets.QPushButton("Fig 2")
        self.fig1.setCheckable(True)
    

        self.velLabel = widgets.QLabel()
        self.velLabel.setText("Velocidade")
        self.velIn    = widgets.QLineEdit()
        self.velIn.setText(obj.startVel.__str__())

        self.figLabel = widgets.QLabel()
        self.figLabel.setText("N da figura (começa do 0)")
        self.figIn    = widgets.QLineEdit()
        self.figIn.setText("0")

        self.acceLabel  = widgets.QLabel()
        self.acceLabel.setText("Aceleração")
        self.acceIn     = widgets.QLineEdit()
        self.acceIn.setText(sum(obj.acce).__str__())

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

        self.mainLayout.addWidget(self.figLabel)
        self.mainLayout.addWidget(self.figIn)

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

        self.setFixedSize(165, 350)

    def updateStuff(self):
        self.parent.timer.stop()
        index = int(self.figIn.text())
        if index > 1:
            msg = widgets.QMessageBox()

            msg.setWindowTitle("Erro ao processar formulário")
            msg.setText("Figura não encontrada.")
            msg.exec()
            return
                         
        if int(self.time0In.text()) > int(self.timeFIn.text()) or int(self.time0In.text()) < 0:
            msg = widgets.QMessageBox()

            msg.setWindowTitle("Erro ao processar formulário")
            msg.setText("Tempo final não pode ser menor que o tempo inicial.\nTempo não pode conter casas decimais.\nTempo não pode ser negativo.")
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
        
        self.parent.SGraph.setPlot(t, s, index)
        self.parent.AGraph.setPlot(t, a, index)
        self.parent.VGraph.setPlot(t, v, index)
        #self.parent.gScene.runners[int(self.figIn.text())].sim = obj
        self.parent.gScene.createRunner(obj, index)
        self.parent.nodeDialog.sim = obj
        self.parent.reset()
        self.parent.timer.start()
        self.close()
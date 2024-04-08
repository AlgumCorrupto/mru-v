import matplotlib.pyplot as plt
import matplotlib.patches as pt
import matplotlib.animation as anm
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvas
from sim import obj, Simulation
import gc

class g():
    def __init__(self, title, x, labelX, y,  labelY, par):
        self.x = x
        self.y = y
        self.labelX = labelX
        self.labelY = labelY
        self.title = title
        self.parent = par

    # overriding abstract method
    def setPlot(self, x, y):
        self.x = x
        self.y = y
        self.ani.__del__()
        self.ani.pause()
        self.circle.remove()
        del self.ani
        gc.collect()

        if len(self.ax.lines) > 0:
            for line in list(self.ax.lines):
                line.remove()
        if len(self.ax.patches) > 0:
            for patch in list(self.ax.patches):
                patch.remove() 
        self.ax.plot(self.x, self.y, linewidth=2.0)
        yl = max(self.y)
        if self.y[0] == self.y[len(self.y)-1]:
            yl *= 1.5
        #self.ax.relim()
        self.ax.set(xlim=(0, max(self.x)),
        ylim=(0, yl))
        self.circleW =  max(self.x)*0.1 if max(self.x) >= 1 else 0.015
        self.circleH = yl*0.1333 if yl >= 1 else 0.015
        self.circle = pt.Ellipse((self.x[0],self.y[0]),self.circleW, self.circleH, fc='yellow',ec='black')
        self.ax.add_patch(self.circle)
        self.ani = anm.FuncAnimation(self.fig, self.update, frames=len(self.x), blit=True, interval=100)
        plt.subplots_adjust(top=0.85, bottom=0.18, left=0.20, right=0.80, hspace=0.25,
                    wspace=0.35)
        
    def plot(self):
        plt.style.use('_mpl-gallery')
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setMinimumSize(364, 224)
        self.parent.graphLayout.addWidget(self.canvas)

        self.ax.plot(self.x, self.y, linewidth=2.0)
        yl = max(self.y)
        if self.y[0] == self.y[len(self.y)-1]:
            yl *= 1.5
        self.ax.set(xlim=(0, max(self.x)), xticks=np.arange(0, 0),
        ylim=(0, yl), yticks=np.arange(0, 0))
        #self.circleW =  max(self.x)*0.1 if max(self.x) >= 1 else 1.0
        self.circleW =  max(self.x)*(self.canvas.height()/ self.canvas.width())*0.1 if max(self.x) >= 1 else 1.0
        #self.circleH =  yl*0.13333 if yl >= 1 else 1.0
        self.circleH =  yl*(self.canvas.height()/ self.canvas.width())*0.1 if yl >= 1 else 1.0
        self.circle = pt.Ellipse((self.x[0],self.y[0]),self.circleW, self.circleH, fc='yellow',ec='black')
        self.ax.add_patch(self.circle)
        self.i = 0
        self.isRunning = False
        self.ani = anm.FuncAnimation(self.fig, self.update, frames=len(self.x), blit=True, interval=100)

        plt.ylabel(self.labelY)
        plt.xlabel(self.labelX)
        plt.title(self.title)
        plt.yscale('linear')
        plt.xscale('linear')
        plt.subplots_adjust(top=0.85, bottom=0.11, left=0.20, right=0.80, hspace=0.25,
                    wspace=0.5)
        #amém
        #plt.show()

    def update(self, frame):
        hMod = 0.175 if max(self.y) == min(self.y) else 0.070
        self.circleW =  max(self.x)*(0.1+(self.canvas.height()/self.canvas.width()*0.1)) if max(self.x) >= 1 else 0.018
        self.circleH =  max(self.y)*(hMod+(self.canvas.width()/self.canvas.height()*0.1)) if max(self.y) >= 1 else 0.018
        self.circle.remove()
        #isso é do SATANÁS, AMIGO!!!!1!
        #ainda bem que não precisei usar 
        #reze por mim, quem estiver vendo esse código
        #gc.collect()
        if self.i < len(self.x) - 1 and self.isRunning == True:
            self.i+= 1
            self.circle = pt.Ellipse((self.x[self.i],self.y[self.i]),self.circleW, self.circleH, fc='yellow',ec='black')
        else:
            self.circle = pt.Ellipse((self.x[self.i],self.y[self.i]),self.circleW, self.circleH, fc='yellow',ec='black')
        self.ax.add_patch(self.circle)
        
        return [self.circle]
    
    def play(self):
        self.isRunning = True if not self.isRunning else False
    def reset(self):
        self.i = 0
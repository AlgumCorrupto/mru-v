import matplotlib.pyplot as plt
import matplotlib.patches as pt
import matplotlib.animation as anm
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvas
from sim import obj, Simulation
import gc
from colorParser import clr
from matplotlib import cycler
from matplotlib.font_manager import FontProperties

class g():
    def __init__(self, title, x, labelX, y,  labelY, par):
        self.x = x
        self.y = y
        self.labelX = labelX
        self.labelY = labelY
        self.title = title
        self.parent = par
        self.dTime = 0

    # overriding abstract method
    def setPlot(self, x, y):
        plt.style.use('_mpl-gallery')
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
        ym = min(self.y)
        if yl == ym:
            yl *= 1.5
            ym *= 2/3
        
        xl = max(self.x)
        xm = min(self.x)
        if xl == xm:
            xl *= 1.5
            xm *= 2/3

        self.ax.set(xlim=(xm, xl),ylim=(ym, yl))
        #hMod = 0.175 if abs_max(max(self.y)) == abs_max(min(self.y)) else 0.070
        #self.circleW =  abs_max(max(self.x))*(0.1+(self.canvas.height()/self.canvas.width()*0.1)) if abs_max(max(self.x)) >= 1 else 0.018
        #self.circleH =  abs_max(max(self.y))*(hMod+(self.canvas.width()/self.canvas.height()*0.1)) if abs_max(max(self.y)) >= 1 else 0.018
        self.circle = pt.Ellipse((self.x[0],self.y[0]),self.circleW, self.circleH, fc='yellow',ec='black')
        self.ax.add_patch(self.circle)
        self.ani = anm.FuncAnimation(self.fig, self.update, frames=len(self.x), blit=True, interval=100)
        #plt.subplots_adjust(top=0.85, bottom=0.18, left=0.20, right=0.80, hspace=0.25,
        #            wspace=0.35)

    def plot(self):
        self.style()
        plt.style.use('_mpl-gallery')
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setMinimumSize(364, 224)
        self.parent.graphLayout.addWidget(self.canvas)

        self.ax.plot(self.x, self.y, linewidth=2.0)
        yl = max(self.y)
        ym = min(self.y)
        if yl == ym:
            yl *= 1.5
            ym *= 2/3
        
        xl = max(self.x)
        xm = min(self.x)
        if xl == xm:
            xl *= 1.5
            xm *= 2/3

        self.ax.set(xlim=(xm, xl), xticks=np.arange(0, 0),
        ylim=(ym, yl), yticks=np.arange(0, 0))
        #self.circleW =  max(self.x)*0.1 if max(self.x) >= 1 else 1.0
        self.circleW =  max(self.x)*(self.canvas.height()/ self.canvas.width())*0.1 if max(self.x) >= 1 else 1.0
        #self.circleH =  yl*0.13333 if yl >= 1 else 1.0
        self.circleH =  yl*(self.canvas.height()/ self.canvas.width())*0.1 if yl >= 1 else 1.0
        self.circle = pt.Ellipse((self.x[0],self.y[0]),self.circleW, self.circleH, fc='yellow',ec='black')
        self.ax.add_patch(self.circle)
        self.i = 0
        self.isRunning = False
        self.ani = anm.FuncAnimation(self.fig, self.update, frames=len(self.x), blit=True, interval=100)
        Cursiv = FontProperties('Cursiv')
        plt.ylabel(self.labelY, font=Cursiv, fontsize=14).set_color(clr.matFg)
        plt.xlabel(self.labelX, font=Cursiv, fontsize=14).set_color(clr.matFg)
        plt.title(self.title,   font=Cursiv, fontsize=20)
        plt.yscale('linear')
        plt.xscale('linear')
        plt.subplots_adjust(top=0.85, bottom=0.11, left=0.20, right=0.80, hspace=0.25,
                    wspace=0.5)
        #amém
        #plt.show()

    def style(self):
        plt.rc('figure', facecolor=clr.matBg[0])
        plt.rc('axes', facecolor=clr.matFg, edgecolor='none',
        axisbelow=True, grid=True)
        plt.rc('xtick', direction='out', color=clr.matFg)
        plt.rc('ytick', direction='out', color=clr.matFg)
        plt.rc('text',  color=clr.matFg)
        plt.rc('lines', linewidth=2, color=clr.matGrayDim)

    def abs_max(self, list):
        maximum = -1
        for value in list:
            if abs(value) > maximum:
                maximum = abs(value)
        return maximum
    def abs_min(self, list):
        minimum = 0xFFFFFF
        for value in list:
            if abs(value) < minimum:
                minimum = abs(value)
        return minimum
    
    def update(self, frame):
        hMod = 0.030 if self.abs_max(self.y) == self.abs_min(self.y) else 0.070
        self.circleW =  self.abs_max(self.x)*(0.1+(self.canvas.height()/self.canvas.width()*0.1))   if self.abs_max(self.x) != 0 else  0.13 * (0.1+(self.canvas.height()/self.canvas.width()*0.1))
        self.circleH =  self.abs_max(self.y)*(hMod+(self.canvas.width()/self.canvas.height()*0.1))  if self.abs_max(self.y) != 0 else  0.13 * (hMod+(self.canvas.width()/self.canvas.height()*0.1))
        self.circle.remove()
        #isso é do SATANÁS, AMIGO!!!!1!
        #ainda bem que não precisei usar 
        #reze por mim, quem estiver vendo esse código
        #gc.collect()
        self.dTime += 1
        if self.i < len(self.x) - 1 and self.isRunning == True:
            self.i+= 1
            self.circle = pt.Ellipse((self.x[self.i],self.y[self.i]),self.circleW, self.circleH, fc=clr.matNormal[3],ec='black')
        else:
            self.circle = pt.Ellipse((self.x[self.i],self.y[self.i]),self.circleW, self.circleH, fc=clr.matNormal[3],ec='black')
        self.ax.add_patch(self.circle)
        
        return [self.circle]
    
    def play(self):
        self.isRunning = True if not self.isRunning else False
    def reset(self):
        self.i = 0
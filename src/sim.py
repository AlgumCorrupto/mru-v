import data

class Simulation(): 
    #variable declaration
    currTime = 0
    Time0 = 0
    TimeF = 0 

    startVel = 0 
    currVel = 0
    acce = 0 

    startPos = 0 
    pos = 0

    dataArr = []

    #constructor
    def __init__(self, vel, pos, acce, time0, timeF):
        self.startVel = vel
        self.startPos = pos
        self.acce = acce
        self.Time0 = time0
        self.TimeF = timeF
        self.dataArr = []
        self.reset()
        self.run()
    
    # devo criar uma única função?? nahhhhh
    def setVel(self, vel):
        self.startVel = vel
    def setAcce(self, acce):
        self.acce = acce
    def setTime(self, time0, timeF):
        self.Time0 = time0
        self.TimeF = timeF
    def setPos(self, pos):
        self.startPos = pos
    
    #run simulation
    def run(self):
        while self.currTime < self.TimeF:
            self.currTime+=1
            vel = self.startVel + self.acce*self.currTime
            pos = self.startPos + self.startVel * self.currTime + (self.acce*pow(self.currTime, 2)) * 0.5
            #Amém
            self.dataArr.append(data.Data(pos, self.currTime, vel, self.acce))

    #reset the simulation
    def reset(self):
        self.currVel = self.startVel
        self.pos = self.startPos
        self.currTime = self.Time0



obj = Simulation(0, 0, 1, 0, 50)
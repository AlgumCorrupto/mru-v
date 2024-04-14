import data

class Simulation(): 
    #variable declaration
    currTime = 0
    Time0 = 0
    TimeF = 0 

    startVel = 0 
    currVel = 0
    acce = []

    startPos = 0 
    pos = 0

    dataArr = []

    #constructor
    def __init__(self, vel, pos, acce, time0, timeF):
        self.startVel = vel
        self.startPos = pos
        self.vel = vel
        self.pos = pos
        self.acce = []
        self.acce = [acce]
        self.Time0 = time0
        self.TimeF = timeF
        print("TimeF= {}".format(self.TimeF))
        self.currTime = 0
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
        self.dataArr.append(data.Data(self.startPos, self.currTime + self.Time0, self.startVel, self.acce[0]))
        while self.currTime + self.Time0 < (self.TimeF):
            self.currTime+=1
            self.vel = self.startVel + self.acce[0]*self.currTime
            self.pos = self.startPos + self.startVel * self.currTime + (self.acce[0]*pow(self.currTime, 2)) * 0.5
            #Amém
            self.dataArr.append(data.Data(self.pos, self.currTime + self.Time0, self.vel, self.acce[0]))
        print(self.dataArr[0].vel)

    #reset the simulation
    def reset(self):
        self.currVel = self.startVel
        self.pos = self.startPos
        self.currTime = 0

    def addNode(self, deltaT, acce):
        self.acce.append(acce)
        print("TimeF= {}".format(self.TimeF))
        print("deltaT= {}".format(deltaT))
        while self.currTime < (deltaT + self.TimeF):
            self.currTime+=1
            self.vel += acce
            self.pos += self.vel
            self.dataArr.append(data.Data(self.pos, self.currTime, self.vel, acce))  
        self.TimeF += deltaT

obj = Simulation(0, 0, 1, 0, 50)
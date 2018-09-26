#ETGG 1803 Lab4, by. Thomas Gilman
#2/26/16 2:19AM
import math3d
import pygame
import random
import time
import math

class Tank(object):
    def __init__(self):
        #loads the tank image, that I cut out
        self.image= pygame.image.load("turret.png")
        self.turret = self.image
        self.turretState=[]
        self.turretState.append(True)
        self.turretState.append(False)
        self.x=random.randint(10,790)
        self.y=random.randint(10,590)
        self.angle=random.randint(0,360)
        self.pos=math3d.VectorN(self.x,self.y,0)
        self.Vec= math3d.Ray(self.pos,self.pos)
        self.Timer=time.time()
        self.State=0
        self.StatePeriod=5
    def update(self):
        self.AngleFacing=math3d.VectorN(math.cos(math.radians(self.angle)),math.sin(math.radians(self.angle)), 0)
        self.Vec=math3d.Ray(self.pos,self.AngleFacing)
        VecDist=self.pos-p.PlayerPos
        PassTime=time.time()-self.Timer
        if PassTime> self.StatePeriod:
            self.State+=1
            self.Timer=time.time()
            if self.State>1:
                self.State=0
        if VecDist.cross(self.Vec.destination)[2]<0:
            self.angle-=1 * deltaTime
        else:
            self.angle+=1 * deltaTime
        self.turret = pygame.transform.rotate(self.image,-int(self.angle+90))
        if self.Vec.getDistanceToPoint(p.PlayerPos)==None:
            pass
        elif self.Vec.getDistanceToPoint(p.PlayerPos)<20 and self.State==0:
            print("pain train")
    def render(self,screen):
        if self.State== 0:
            self.Vec.drawPygame(screen,(240,135,255),8)
        screen.blit(self.turret,(self.pos[0]-self.turret.get_width()/2,self.pos[1]-self.turret.get_height()/2))
        #print(str(self.angle))

class Player(object):
    def __init__(self,mPos):
        self.player=pygame.image.load("link.png")
        self.PlayerPos=mPos
        #self.PlayerAngle=random.randint(0,360)
        self.animList=[]
        self.animList.append((0,0,32,50))
        self.animList.append((32,0,32,50))
        self.animList.append((64,0,32,50))
        self.animList.append((96,0,32,50))
        self.Timer=time.time()
        self.animFrame=0
        self.animPeriod=0.5
        #self.PVec= math3d.Ray(self.PlayerPos,self.PlayerPos)
    def render(self):
        curFrame=self.animList[self.animFrame]
        screen.blit(self.player,(self.PlayerPos[0] - 16, self.PlayerPos[1] - 30),(curFrame[0],curFrame[1],curFrame[2],curFrame[3]))
    def update(self):
        #self.PlayerAngle=math3d.VectorN(math.cos(math.radians(self.PlayerAngle)),math.sin(math.radians(self.PlayerAngle)), 0)
        #self.PVec=math3d.Ray(self.PlayerPos,self.PlayerAngle)
        passTime=time.time()-self.animPeriod
        if passTime>self.animPeriod:
            self.animFrame+=1
            self.Timer=time.time()
            if self.animFrame>3:
                self.animFrame=0


done=False
Clock=pygame.time.Clock()
mPos=math3d.VectorN(600,400)
win_width=800
win_height=600
screen=pygame.display.set_mode((win_width,win_height))
pygame.mouse.set_visible(False)
TankList=[]
p=Player(mPos)

while done!= True:
    #append Tanks to a list
    if len(TankList)<4:
        TankList.append(Tank())
    #Time
    deltaTime= Clock.tick()/100.0
    #Event Polling
    event= pygame.event.poll()
    #Get Key
    key = pygame.key.get_pressed()
    #Get mouse Pos
    mX, mY = pygame.mouse.get_pos()
    p.PlayerPos= math3d.VectorN(mX,mY, 0)
    #Escape
    if key[pygame.K_ESCAPE]:
        done = True
    #Fill Screen
    screen.fill((255,255,255))
    #blit tank to screen
    for tank in TankList:
        tank.update()
        tank.render(screen)
    p.render()
    p.update()
    #Draw
    pygame.display.flip()
pygame.quit()
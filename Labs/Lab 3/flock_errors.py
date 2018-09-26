import pygame
import math3d
import random
class Boid(object):
    def __init__(self,x,y):
        self.mPos=math3d.VectorN(x,y)
        self.mVel=math3d.VectorN(15,10)
        self.AccelMag=50
    def appAccel(self,deltaTime,mpos):
        if mpos:
            Vel=mpos-self.mPos
        self.mVel+=Vel.normalized()*self.AccelMag*deltaTime
    def update(self,deltaTime,mpos):
        self.boidOffset=self.mVel*deltaTime
        self.mPos+=self.boidOffset
        if mpos:
            Vec=mpos-self.mPos
            self.mVel+=Vec.normalized()*self.AccelMag*deltaTime
        if self.mPos[0]<=0:
            self.mPos[0]=0
        if self.mPos[0]>=800:
            self.mPos[0]=800
        if self.mPos[1]<=0:
            self.mPos[1]=0
        if self.mPos[1]>=600:
            self.mPos[1]=600
    def render(self,screen):
        self.boid=pygame.draw.polygon(screen,(255,0,0),((self.mPos[0],self.mPos[1]),(self.mPos[0]+4,self.mPos[1]+4),(self.mPos[0]+3,self.mPos[1]+7),(self.mPos[0]-3,self.mPos[1]+7),(self.mPos[0]-4,self.mPos[1]+4)),0)
        #self.boid=pygame.draw.circle(screen,(255,0,0),self.mPos.int(),5)


class Flock(object):
    def __init__(self,screen,num,obs):
        self.boidList=[]
        self.screen=screen
        self.num=num
        self.obs=obs
        self.create()
    def render(self,screen):
        for boid in self.boidList:
            boid.render(screen)
    def create(self):
        for i in range(0,self.num):
            self.boidList.append(Boid(random.randint(0,800),random.randint(0,600)))
        for i in self.boidList:
            for obstacle in self.obs:
                while colliding(i.mPos[0], i.mPos[1], 5, obstacle[0][0], obstacle[0][1], obstacle[1]):
                    i.mPos[0] = random.randint(0,800)
                    i.mPos[1] = random.randint(0,600)
    def update(self,deltaTime,mpos):
        bavg=math3d.VectorN(0,0)
        if not mpos:
            for i in self.boidList:
                bavg+=i.mPos
            bavg/=len(self.boidList)
            Boid.boidOffset=bavg
        else:
            bavg+=mpos
        #for i in self.boidList:
        #    i.appAccel(bavg,deltaTime)
        #for i in self.boidList:
        #    i.update(deltaTime)
    def collision(self,deltaTime,obsList):
        for obs in obsList:
            for boid in self.boidList:
                if colliding(boid.mPos[0], boid.mPos[1], 10, obs[0][0], obs[0][1], obs[1]):
                    boid.mPos += -boid.boidOffset
                    boid.mVel*=-1
            #Vec=obs-Boid.mPos
            #Vec=Vec/Vec.magnitude()
            #Vec_dist=((self.obs[0]-Boid.mPos[0])**2+(self.obs[1]-Boid.mPos[1])**2)**.5
            #if Vec_dist<=self.obs[1]+20:
            #    Boid.mVel+=-Vec.normalized()*Boid.AccelMag*deltaTime
            #if Vec_dist<=self.obs[1]:
            #    Boid.mVel*=-1


def colliding(c1x, c1y, c1r, c2x, c2y, c2r):
    if (int(c1x)-int(c2x))** 2+(int(c1y)-int(c2y))**2<=(int(c1r)+int(c2r))**2:
        return True
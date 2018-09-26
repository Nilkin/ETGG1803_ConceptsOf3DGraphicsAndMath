import pygame
import math3d
import random
class Boid(object):
    def __init__(self,x,y):
        self.mPos=math3d.VectorN(x,y)
        self.mVel=math3d.VectorN(15,10)
        self.AccelMag=50
        self.TerVel=200
    def appAccel(self,deltaTime,mpos):
        """this allows the boid to accelerate based on which direction its going"""
        if mpos:
            eVel=mpos-self.mPos
            self.mVel+=eVel.normalized()*self.AccelMag*deltaTime
    def update(self,deltaTime):
        """this allows the boid to move, and keeps it on the screen"""
        self.boidOffset=self.mVel*deltaTime
        self.mPos+=self.boidOffset
        if self.AccelMag>=self.TerVel:
            self.AccelMag=self.TerVel
        if self.mPos[0]<=0:
            self.mPos[0]=0
        if self.mPos[0]>=800:
            self.mPos[0]=800
        if self.mPos[1]<=0:
            self.mPos[1]=0
        if self.mPos[1]>=580:
            self.mPos[1]=580
    def render(self,screen):
        """This draws the boid and turns it baised on which direction its going."""
        VelHat=self.mVel.normalized()
        forward=self.mPos+VelHat*10
        self.mVelHatPerpen=math3d.VectorN(-VelHat[1],VelHat[0])
        left=self.mPos-self.mVelHatPerpen*5
        right=self.mPos+self.mVelHatPerpen*5
        bottRight=self.mPos+self.mVelHatPerpen*10
        bottLeft=self.mPos-self.mVelHatPerpen*10
        self.boid=pygame.draw.polygon(screen,(255,0,0),(forward.int(),bottRight.int(),right.int(),left.int(),bottLeft.int()),0)
        #self.boid=pygame.draw.circle(screen,(255,0,0),self.mPos.int(),5)



class Flock(object):
    def __init__(self,screen,num,obs):
        self.boidList=[]
        self.screen=screen
        self.num=num
        self.obs=obs
        self.create()
    def render(self,screen):
        """This Function shows each boid on the screen"""
        for boid in self.boidList:
            boid.render(screen)
    def create(self):
        """This function appends boids to the boidList depending on the amount of boids requested."""
        for i in range(0,self.num):
            self.boidList.append(Boid(random.randint(0,800),random.randint(0,600)))
    def update(self,deltaTime,mpos):
        """This Function updates the position of each boid in the flock, if the
        Mouse button isnt pressed, the poids head to the center of the flock."""
        if not mpos:
            bavg=math3d.VectorN(0,0)
            for i in self.boidList:
                bavg+=i.mPos
            bavg/=len(self.boidList)
            Boid.boidOffset=bavg
        else:
            bavg=mpos
        for i in self.boidList:
            i.appAccel(deltaTime,bavg)
        for i in self.boidList:
            i.update(deltaTime)
    def collision(self,boid):
        for obs in self.obs:
            #Vec=obs-boid.mPos
            #Vec=Vec/Vec.magnitude()
            Vec_dist=((obs[0]-boid.mPos[0])**2+(obs[1]-boid.mPos[1])**2)**.5
            return Vec_dist<=self.obs[1]+5
def colliding(c1x, c1y, c1r, c2x, c2y, c2r):
    """This is to check to see if two objects are colliding"""
    if (int(c1x)-int(c2x))** 2+(int(c1y)-int(c2y))**2<=(int(c1r)+int(c2r))**2:
        return True
    return False

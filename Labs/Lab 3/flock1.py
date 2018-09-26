import random
import math3d
import pygame

class Boid(object):
    def __init__(self,x,y):
        """creating the beginning values for the boid"""
        self.mPos=math3d.VectorN(x,y)#VectorN
        self.mVel=math3d.VectorN(15,10) #VectorN
        self.AccelMag=100
        #self.mLastOrientation

    def update(self,deltaTime):
        """updates the movement of the boid without the mouse button clicked"""
        self.new_mPos=self.mVel*deltaTime
        self.mPos+=self.new_mPos
        
        if self.mPos[0]<0:
            self.mPos[0]=0
            
        if self.mPos[1]<0:
            self.mPos[1]=0

        if self.mPos[0]>799:
            self.mPos[0]=799

        if self.mPos[1]>599:
            self.mPos[1]=599

    def accel(self,deltaTime,mpos):
        if formation(self,40,mpos):
            acceleration=self.AccelMag/10

        else:
            acceleration=self.AccelMag
            
        if mpos:
            eVel=mpos-self.mPos
            self.mVel+=eVel.normalized()*acceleration*deltaTime

    def render(self,screen):
        """draw a circle for practice before I made the actual bird"""
        #self.boid=pygame.draw.circle(screen,(255,0,0),self.mPos.int(),5)
        """ this is the actual bird for the program, draws the boid to the screen"""
        VelHat=self.mVel.normalized()
        fwd = self.mPos + VelHat  * 10
        self.mVelHatPerp = math3d.VectorN(-VelHat[1],VelHat[0])
        right = self.mPos + self.mVelHatPerp * 5
        left = self.mPos - self.mVelHatPerp*5
        self.boid=pygame.draw.polygon(screen, (255,0,0), (fwd.int(), left.int(), right.int()))
        #self.boid=pygame.draw.polygon(screen,(255,0,0),((self.mPos[0],self.mPos[1]),(self.mPos[0]+4,self.mPos[1]+4),(self.mPos[0]+2,self.mPos[1]+7),(self.mPos[0]-2,self.mPos[1]+7),(self.mPos[0]-4,self.mPos[1]+4)),0)


class Flock(object):
    def __init__(self,screen,num,obs):
        self.screen=screen
        self.num=num
        self.obs=obs
        self.boid_list=[]
        self.creation()
        
    def render(self,screen):
        """draws the whole flock to the screen"""
        for boid in self.boid_list:
            boid.render(screen)
        
    def creation(self):
        """adds the boids to a list so they can be rendered"""
        for i in range(0,self.num):
            self.boid_list.append(Boid(random.randint(0,800),random.randint(0,600)))
            
    def update(self,deltaTime,mpos):
        """updates the movement of each of the boids in the flock"""

        if not mpos:
            avg=math3d.VectorN(0,0)
            for boid in self.boid_list:
                avg+=boid.mPos
            avg/=len(self.boid_list)
            Boid.new_mPos=avg
        else:
            avg = mpos

        """moves the flock based on the mouse button being clicked down"""
        for i in self.boid_list:
            i.accel(deltaTime,avg)

        """this is the update method from boid that does not have the mouse clicking
           I did not know if this was the way you wanted it to be set up"""
        for b in self.boid_list:
            b.update(deltaTime)

        
def collide(self,c1x,c1y,c1r,c2x,c2y,c2r):
    if (int(c1x)-int(c2x))**2+(int(c1y)-int(c2y))**2<= (int(c1r)+int(c2r))**2:
        return True
    return False

def formation(boid,distance,spot):
    return collide(boid.mPos[0],boid.mPos[1],distance,spot[0],spot[1],1)
        

def collide_obstacles(self):
    for i in self.obs:
        eVel=i-Boid.mPos
        eVel=eVel/eVel.magnitude()
        eVel_dist=((self.obs[0]-Boid.mPos[0])**2+(self.obs[1]-Boid.mPos[1])**2)**0.5
        if eVel_dist<=self.obs[1]+20:
            Boid.mVel+=-eVel.normalized()*Boid.AccelMag*deltaTime

import math3d
import pygame

#Initilization
pygame.init()
Screen=pygame.display.set_mode((1000,800))
done=False


Objects=[]

#Color
Color=(0,0,0)

#Objects
#Sun object and material
Sun=("sun.obj")
SunMTL=("sun.mtl")
#Saturn object and material
Saturn=("saturn.obj")
SaturnMTL=("saturn.mtl")
#Ship object and material
Ship=("ship.obj")
ShipMTL=("ship.mtl")

#SunHeirarchy
SunObjects=[]
SaturnObjects=[]
ShipObjects=[]
#Matrix
Matrix=math3d.MatrixN(4,4,(1,0,0,0,0,1,0,0,0,0,1,0,Screen.get_width()/2,Screen.get_height()/2,0,1))
#Transformation Matrix
Transform=math3d.MatrixN(4,4,(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1))
#Scaler
Scale=math3d.MatrixN(4,4,(100,0,0,0,0,100,0,0,0,0,100,0,0,0,0,1))
#append objects to objects list
#Appending a Polymesh's to lists
#This is the Rocket Poly that orbits the saturn
SaturnObjects.append(math3d.Polymesh(Ship,Screen,ShipMTL,Transform*math3d.Scale(.1,.1,.1)*math3d.RotateX(90)*math3d.RotateY(90)*math3d.Translate(0,0,3),ShipObjects,"Rocket"))
#This is the Saturn Poly that orbits the sun
SunObjects.append(math3d.Polymesh(Saturn,Screen,SaturnMTL,Transform*math3d.Scale(.35,.35,.35)*math3d.RotateX(45)*math3d.Translate(-3,0,0),SaturnObjects,"Saturn"))
#This is the Rocket Poly that orbits the sun
SunObjects.append(math3d.Polymesh(Ship,Screen,ShipMTL,Transform*math3d.Scale(.1,.1,.1)*math3d.RotateX(-90)*math3d.Translate(3,0,0),ShipObjects,"Rocket"))
#This is the Sun poly and it is the center/root of all the other polymeshes/objects
Objects.append(math3d.Polymesh(Sun,Screen,SunMTL,Transform,SunObjects,"Sun"))
#angle
angle=0
RotationAngle=0
#Rotation
rotateX=math3d.RotateX(angle+90)
rotateY=math3d.RotateY(angle)
rotateZ=math3d.RotateZ(angle+180)
Rotation=rotateX*rotateY*rotateZ
while not done:
    # Input
    pygame.event.pump()
    #Mouse
    (MLeft,MMiddle,MRight)=pygame.mouse.get_pressed()
    #This is to get the mouse's velocity/direction dragged
    mX=pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    #Rotate
    RotationAngle+=4
    if MLeft:
        #This resets the angle back to 0 after a full rotation
        if angle>360:
            angle=0
        #This sets the angle to 360 if angle dragged is less than angle 0
        if angle<0:
            angle=360
        #This adds to the angle based on which direction you drag the mouse
        if mX[0]>0:
            angle+=6
        if mX[0]<0:
            angle-=6
        rotateY=math3d.RotateY(angle)
        Rotation=rotateX*rotateY*rotateZ
    NewMatrix=Scale*Rotation*Matrix
    # Draw
    Screen.fill(Color)
    #Render polymesh to screen
    #for Poly in Object:
    #    Poly.render(Trans)
    for object in Objects:
        object.render(NewMatrix,RotationAngle)
    pygame.display.flip()
#Quit
pygame.display.quit()
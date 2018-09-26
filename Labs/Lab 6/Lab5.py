import math3d
import pygame





pygame.init()
screen=pygame.display.set_mode((300,2000))
done= False

#create a amera
camPos=math3d.VectorN(5,7,-20)
camUP=math3d.VectorN(2,5,3)
camFOV=60
camNear=1.5
cam=math3d.Camera(camPos,camUP,camFOV,camNear,screen)
object=[]


while not done:
    #update
    #render one line of pixels in the screen (if we havnt rendered all of them yet)
    #Do it this way so we give the user a chance to press escape while we're rendering
    if y<screen.get_height():
        #render one line
        for x in range(screen.get_width()):
            pos3d=cam.getPixelPos(x,y)
            dir3d= pos3d-cam.mPos                          #the rays direction away from camera
            R= math3d.Ray(pos3d,dir3d)
        #see what the ray hits. get color of closest hit
        #You will need to add some code to make this happen
        for o in object:
            result=o.rayIntersection(R)
        y+=1

    #input
    pygame.event.pump()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done=True

#This closes the program efficially
pygame.quit()
import math3d
import pygame

#Pygame setup
pygame.init()
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
done=False

circlePos=math3d.VectorN(400,300) #The POSITION of the circle
circleVel=math3d.VectorN(200,100) #The OFFSET to move circle every SECOND

circleAccelMag=100  #Attraction to mouse

#Game Loop
while not done:
    #Non-input related updates
    deltaTime=clock.tick()/1000.0

    circleOffset=circleVel*deltaTime

    circlePos+=circleOffset

    circleVelHat=circleVel.normalized()
    circleVelHatPerp=math3d.VectorN(-circleVelHat[1],circleVelHat[0])
    fwd=circlePos+circleVelHat*100
    right=circlePos+circleVelHatPerp*50
    
    #Input-related updates
    event=pygame.event.poll()
    #...event-handling
    if event.type==pygame.QUIT:
        done=True
    #...device-polling
    keys=pygame.key.get_pressed()
    mx,my=pygame.mouse.get_pos()
    mbuttons=pygame.mouse.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done=True
    if mbuttons[0]:
        #Left-clicking. Make circleVel point towards
        #the mouse, but stay at the same speed
        mousePos=math3d.VectorN(mx,my)
        #circleSpeed=circleVel.magnitude()
        e=mousePos-circlePos
        circleVel+=e.normalized()*circleAccelMag*deltaTime

        
    #Drawing code (based on current variable values)
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0),circlePos.int(),50)
    pygame.draw.line(screen,(255,255,255),circlePos,fwd)
    pygame.draw.line(screen,(255,255,255),circlePos,right)
    pygame.display.flip()


pygame.quit()

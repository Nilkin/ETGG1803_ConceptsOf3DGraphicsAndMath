import math3d
import pygame

#Shadow Test
def Shadows(Ray,Light,objects):
    NotHit=True
    distance=(Ray.mOrigin-Light.Point).magnitude()
    for o in objects:
        result=o.rayIntersection(Ray)
        if result!=None and result[0]<distance:
            NotHit=False
    return NotHit



# Pygame window
pygame.init()
screen = pygame.display.set_mode((300, 200))        # Look at test #3
done = False

# Create a camera (use one of the camera test values)
camPos = math3d.VectorN(-15, 19, -30)
camCOI= math3d.VectorN(2, 5, 3)
camUp = math3d.VectorN(0,1,0)
camFOV = 60
camNear = 1.5
cam = math3d.Camera(camPos,camCOI, camUp, camFOV, camNear, screen)
Ambient_Light=math3d.VectorN(1,1,1)
objects = []      # See Phase III tester and the numbers on page 4 of the lab pdf
y = 0

#Shapes
objects.append(math3d.Sphere(math3d.VectorN(2, 5, 3), 7, math3d.Material(math3d.VectorN(1,0,0),math3d.VectorN(1,1,1),10,math3d.VectorN(.3,0,0))))
objects.append(math3d.Plane(math3d.VectorN(0,1,0), 5, math3d.Material(math3d.VectorN(0,1,0),math3d.VectorN(1,0,0),2.0,math3d.VectorN(0,0.5,0))))
objects.append(math3d.Plane(math3d.VectorN(0.1,1,0).normalized(), 4, math3d.Material(math3d.VectorN(0,0,1),math3d.VectorN(1,0,1),6.0,math3d.VectorN(0,0,0.1))))
objects.append(math3d.AABB(math3d.VectorN(2,9,-6),math3d.VectorN(8,15,0),math3d.Material(math3d.VectorN(1,1,0),math3d.VectorN(0.5,1,0.5),6.0,math3d.VectorN(0.5,0.3,0.1))))
objects.append(math3d.Polymesh("sword.obj",math3d.VectorN(-10,8,3),1.0,math3d.Material(math3d.VectorN(0.7,0,1),math3d.VectorN(1,1,1),50.0,math3d.VectorN(0.2,0,0.4))))

#LightSources
LightSources=[]
LightSources.append(math3d.LightSource(math3d.VectorN(0,50,0),math3d.VectorN(1,1,1),math3d.VectorN(1,1,1)))
LightSources.append(math3d.LightSource(math3d.VectorN(50,50,-50),math3d.VectorN(0.4,0,0),math3d.VectorN(0,0.6,0)))

# Game Loop
while not done:
    # Update
    # Render one line of pixels in the screen (if we haven't rendered all of them
    #  yet).  Do it this way so we give the user a chance to press escape
    # while we're rendering.
    if y < screen.get_height():
        # Render one line
        for x in range(screen.get_width()):
            pos3d=cam.getPixelPos(x, y)     # The ray's origin
            dir3d=pos3d-camPos          # The ray's direction (away from camera)
            R=math3d.Ray(pos3d,dir3d)

            color=(64,64,64)
            sep_distance=[]
            sep_objects=[]
            sep_norm=[]
            for o in objects:
                result = o.rayIntersection(R)
                if result!=None:
                    sep_objects.append(o)
                    sep_distance.append(result[0])
                    sep_norm.append(result[1])
            if len(sep_distance)==0:
                LightColor=math3d.VectorN(.2,.2,.2)
            else:
                minDistance=min(sep_distance)
                minIndex=sep_distance.index(minDistance)
                Norm=sep_norm[minIndex]
                o=sep_objects[minIndex]
                for i in range(len(sep_distance)):
                    if sep_distance[i]==minDistance:
                        amb_c=Ambient_Light.pairwise_mult(o.mColor.Ambient)
                        LightColor=amb_c
                        for i in LightSources:
                            T=R.getPoint(minDistance)
                            LightDirection=i.Point-T
                            LightHat=LightDirection/LightDirection.magnitude()
                            HitPoint=T+0.0001*Norm
                            RayHit=math3d.Ray(HitPoint,LightHat)
                            if Shadows(RayHit,i,objects):
                                RayVec=2*(LightHat.dot(Norm))*Norm-LightHat
                                VectorV=camPos-T
                                VecVHat=VectorV/VectorV.magnitude()
                                sStr=VecVHat.dot(RayVec)
                                dStr=LightHat.dot(Norm)
                                if dStr>0:
                                    DiffuseColor=dStr*(i.Diffuse.pairwise_mult(o.mColor.Diffuse))
                                    LightColor+=DiffuseColor
                                if sStr>0:
                                    SpecularColor=(sStr**o.mColor.Specular_Pow)*(i.Specular.pairwise_mult(o.mColor.Specular))
                                    LightColor+=SpecularColor
            color=LightColor.clamp()
            color=(color*255).int()
            screen.set_at((x, y), color)

        y += 1



    # Input
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True

    # Draw

    pygame.display.flip()

pygame.display.quit()
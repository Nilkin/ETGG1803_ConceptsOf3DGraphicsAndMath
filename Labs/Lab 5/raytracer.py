import math3d
import objects3d
import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 200))
done = False

camPos = math3d.VectorN(-5, 7, -30)
camCOI = math3d.VectorN(2, 5, 3)
camUp = math3d.VectorN(0, 1, 0)
camFOV = 60.0
camNear = 1.5
cam = objects3d.Camera(camPos, camCOI, camUp, camFOV, camNear, screen)

allShapes = []
allShapes.append(objects3d.Sphere(math3d.VectorN(2, 5, 3), 7, math3d.VectorN(1, 0, 0)))
allShapes.append(objects3d.Plane(math3d.VectorN(0,1,0), 5, math3d.VectorN(0,1,0)))
allShapes.append(objects3d.Plane(math3d.VectorN(0.1,1,0), 4, math3d.VectorN(0,0,1)))

y = 0

# Drawing code
for y in range(0, screen.get_height()):


# Game Loop
while not done:
    # Render one line of pixels IF we have more to render
    if y < screen.get_height():
        for x in range(0, screen.get_width()):
            # For this pixel, create a ray that starts on our view plane
            # and goes away from the camera.
            rayOrigin = cam.getPixelPos(x, y)
            rayDirection = rayOrigin - cam.mPos
            R = objects3d.Ray(rayOrigin, rayDirection)

            for obj in allObjects:
                result = obj.rayIntersection(R)

            # Find the closest object we hit and get it's color
            screen.set_at((x, y), color)
        y += 1

    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True


    pygame.display.flip()

pygame.quit()
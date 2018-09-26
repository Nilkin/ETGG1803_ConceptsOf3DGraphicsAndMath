import raytracer
import objects3d
import time
import pygame
import math3d

caseNum = 2

# Pygame setup
if caseNum == 1:
    win_width = 700;        win_height = 150;
elif caseNum == 2:
    win_width = 800;        win_height = 600;
else:
    win_width = 300;        win_height = 200;
pygame.display.init()
screen = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
done = False

# Raytracer setup
if caseNum == 1:
    cameraPos = math3d.VectorN(0, 0, -20)
    cameraUp = math3d.VectorN(0, 1, 0)
    cameraCoi = math3d.VectorN(0, 0, 0)
    cameraNear = 3.2
    cameraFov = 45.0
elif caseNum == 2:
    cameraPos = math3d.VectorN(5, 7, -20)
    cameraUp = math3d.VectorN(1, 10, 0).normalized()
    cameraCoi = math3d.VectorN(2, 5, 3)
    cameraNear = 1.5
    cameraFov = 60.0
elif caseNum == 3:
    cameraPos = math3d.VectorN(-5, 7, -30)
    cameraUp = math3d.VectorN(0, 1, 0)
    cameraCoi = math3d.VectorN(2, 5, 3)
    cameraNear = 1.5
    cameraFov = 60.0
camera = objects3d.Camera(cameraPos, cameraCoi, cameraUp, screen, cameraFov, cameraNear, True)

sphere1 = objects3d.Sphere(math3d.VectorN(2,5,3), 7.0, math3d.VectorN(1,0,0))
plane1 = objects3d.Plane(math3d.VectorN(0,1,0), 5.0, math3d.VectorN(0,1,0))
plane2 = objects3d.Plane(math3d.VectorN(0.1,1,0), 4.0, math3d.VectorN(0,0,1))
box1 = objects3d.AABB(math3d.VectorN(2, 9, -6), math3d.VectorN(8, 15, 0), math3d.VectorN(1,1,0))
#mesh1 = objects3d.Polymesh("sword.obj", math3d.VectorN(-10,8,3), 1.0, math3d.VectorN(1.0,0.3,0.8))
rt = raytracer.Raytracer(camera)
rt.addObject(sphere1)
rt.addObject(plane1)
rt.addObject(plane2)
rt.addObject(box1)
#rt.addObject(mesh1)
totalTime = 0.0
currentLine = 0

print("\n+==============================================+")
print("| PHASE II tests                               |")
print("+==============================================+")
if caseNum == 1:
    testPts = [(0, 0), (win_width - 1, win_height - 1), (win_width // 2, win_height // 2), (113, 23), (623,83)]
else:
    testPts = [(0, 0), (win_width - 1, win_height - 1), (win_width // 2, win_height // 2), (113, 542), (723,11)]
for pygamePos in testPts:
    camera.getViewplanePosition(pygamePos[0], pygamePos[1], True)

# Game Loop
while not done:
    # Update
    if currentLine < win_height:
        rt.renderOneLine(currentLine)
        currentLine += 1
        dt = clock.tick()
        totalTime += dt

    # Input
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        done = True

    # Draw (nothing to do!)
    pygame.display.flip()

# Pygame shutdown
pygame.display.quit()

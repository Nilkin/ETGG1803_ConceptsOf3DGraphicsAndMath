import pygame
import math3d

def triangleArea(a, b, c):
    v = a - b
    w = c - a
    result = v.cross(w)
    return result.magnitude()

pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("Courier New", 14)
done = False

va = math3d.VectorN(400, 100, 0)
vb = math3d.VectorN(200, 400, 0)
vc = math3d.VectorN(600, 350, 0)
m = math3d.VectorN(0,0,0)
verts = [va, vb, vc, m]

area = triangleArea(va, vb, vc)

while not done:



    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    m[0], m[1] = pygame.mouse.get_pos()
    bary = [triangleArea(m, vb, vc), triangleArea(va, m, vc), triangleArea(va, vb, m)]


    screen.fill((0,0,0))
    for v in verts:
        val = v.int()[0:2]
        pygame.draw.circle(screen, (200,200,200), val, 5)
        tempS = font.render(str(val), False, (128,128,128))
        screen.blit(tempS, (v[0] - tempS.get_width() // 2, v[1] - tempS.get_height() - 5))
    pygame.draw.polygon(screen, (64,64,64), (va.int()[0:2], vb.int()[0:2], vc.int()[0:2]), 1)
    screen.blit(font.render("Tri-area = " + str(round(area,1)), False, (200,255,200)), (0,0))
    msg = "Bary = (" + str(round(bary[0],1)) + ", " + str(round(bary[1],1)) + ", " + str(round(bary[2],1)) + ")"
    screen.blit(font.render(msg, False, (255,200,200)), (0,15))
    screen.blit(font.render("BaryTotal = " + str(round(bary[0] + bary[1] + bary[2], 1)), False, (200,200,255)), (0,30))
    pygame.display.flip()

pygame.display.quit()


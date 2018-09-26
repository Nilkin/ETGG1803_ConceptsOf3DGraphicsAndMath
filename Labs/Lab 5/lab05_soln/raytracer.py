import objects3d
import math3d

class Raytracer(object):
    def __init__(self, camera):
        self.mCamera = camera
        self.mRenderSurf = self.mCamera.mRenderSurf
        self.mBackgroundColor = math3d.VectorN(0.3, 0.3, 0.3)
        self.mObjects = []


    def addObject(self, o):
        self.mObjects.append(o)

    def castRay(self, R):
        closestObject = None
        closestDist = None
        for o in self.mObjects:
            result = o.rayIntersection(R)
            if result != None and (closestObject == None or result < closestDist):
                closestObject = o
                closestDist = result

        if closestObject == None:
            return self.mBackgroundColor
        else:
            return closestObject.mColor

    def renderOneLine(self, y):
        for x in range(self.mRenderSurf.get_width()):
            if x == self.mRenderSurf.get_width() // 2 and y == self.mRenderSurf.get_height() // 2:
                foo = 5
            rayOrigin = self.mCamera.getViewplanePosition(x, y)
            rayDirection = rayOrigin - self.mCamera.mPos
            #print(rayOrigin, rayDirection)
            ray = objects3d.Ray(rayOrigin, rayDirection)
            color = self.castRay(ray)
            self.mRenderSurf.set_at((x, y), (255 * color).int())
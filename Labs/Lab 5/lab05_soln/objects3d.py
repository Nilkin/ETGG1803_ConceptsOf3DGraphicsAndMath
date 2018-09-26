import math
import math3d
import pygame


class Camera(object):
    def __init__(self, pos, coi, upDir, renderSurf, fov, near, printResults = False):
        self.mPos = pos.copy()
        self.mZaxis = (coi - pos).normalized()
        self.mXaxis = upDir.cross(self.mZaxis).normalized()
        self.mYaxis = self.mZaxis.cross(self.mXaxis)               # No need to normalize result of perpendicular vectors
        self.mFOV = fov
        self.mNear = near
        self.mSurf = renderSurf

        self.mRenderSurf = renderSurf
        self.mAspectRatio = self.mRenderSurf.get_width() / self.mRenderSurf.get_height()

        self.mViewplaneHeight = 2 * near * math.tan(math.radians(fov / 2))
        self.mViewplaneWidth = self.mViewplaneHeight * self.mAspectRatio
        self.mViewplaneHHeight = self.mViewplaneHeight / 2
        self.mViewplaneHWidth = self.mViewplaneWidth / 2

        self.mViewplaneOrigin = self.mPos + near * self.mZaxis - self.mViewplaneHWidth * self.mXaxis +\
                                                                 self.mViewplaneHHeight * self.mYaxis
        self.mViewplaneDeltaX = self.mViewplaneWidth / (self.mRenderSurf.get_width() - 1)
        self.mViewplaneDeltaY = self.mViewplaneHeight / (self.mRenderSurf.get_height() - 1)


        if printResults:
            print("+==============================================+")
            print("| PHASE I tests                                |")
            print("+==============================================+")
            print("camera position:        " + str(self.mPos))
            print("camera coi:             " + str(coi))
            print("camera up:              " + str(upDir))
            print("camera x-axis:          " + str(self.mXaxis))
            print("camera y-axis:          " + str(self.mYaxis))
            print("camera z-axis:          " + str(self.mZaxis))
            print("screen dimensions:      " + str(self.mSurf.get_width()) + " x " + str(self.mSurf.get_height()) + " pixels")
            print("aspect ratio:           " + str(self.mAspectRatio))
            print("camera fov:             " + str(fov) + " degrees")
            print("camera near:            " + str(near) + " world units")
            print("viewplane dimensions:   " + str(self.mViewplaneWidth) + " x " + str(self.mViewplaneHeight) + " world units")
            print("viewplane origin:       " + str(self.mViewplaneOrigin))


    def getViewplanePosition(self, px, py, printResults = False):
        p = self.mViewplaneOrigin + px * self.mViewplaneDeltaX * self.mXaxis - \
                                    py * self.mViewplaneDeltaY * self.mYaxis
        if printResults:
            print("pixel (" + str(px) + ", " + str(py) + ") = world-space " + str(p))
        return p



class Ray(object):
    """ An n-dimensional ray [by definition a ray is an origin point and a direction """

    def __init__(self, origin, direction):
        """
        :param origin: the origin POSITION of the ray (a copy of the passed vector is created)
        :param direction: the DIRECTION of the ray (the vector passed in is normalized)
        :return: N/A
        """
        if not isinstance(origin, math3d.VectorN) or not isinstance(direction, math3d.VectorN) or len(origin) != len(direction):
            raise ValueError("You must pass two equal-dimension VectorN's for the origin and direction.")
        self.mOrigin = origin.copy()
        self.mDirection = direction.normalized()

    def getPoint(self, t):
        """
        :param t: A scalar distance along the ray
        :return: The point which is t units along the ray.
        """
        if not isinstance(t, int) and not isinstance(t, float):
            raise ValueError("t must be a scalar.")
        return self.mOrigin + t * self.mDirection

    def drawPygame(self, surf, color = (255,255,255), originRadius = None, endDistance = 1000, thickness=1):
        """
        Draws a 2d representation of this ray to the given pygame surface
        :param surf: a pygame surface
        :param color: a pygame color [defaults to white]
        :param originRadius: the radius of the "ball" to draw at the origin [defaults to None => don't draw the ball]
        :param endDistance: a true Ray doesn't have an end; but in pygame we are actually drawing a line segment.  This
                            value represents how far away from the origin the end point should be.
        :param thickness: the thickness (in pixels) of the line.
        :return: None
        """
        endPt = self.mOrigin + endDistance * self.mDirection
        pygame.draw.line(surf, color, self.mOrigin, endPt, thickness)
        if originRadius != None:
            pygame.draw.circle(surf, color, self.mOrigin.int(), originRadius)

    def getDistanceToPoint(self, p, returnParaPerp = False):
        """
        Returns the minimal distance from point p (which must be of the same dimension as this ray's origin and
           direction.
        :param p: a VectorN POSITION.
        :param returnParaPerp: if True, also return the (unit-length) parallel and perpendicular components created
                                  during this projection operation.  Otherwise, just return the distance.
        :return: If p is on the "front" side of the ray, this method returns the minimal distance to the point from
                 the ray (if you imagine a vector which is perpendicular to the ray, the minimal distance will be the
                 distance from the ray to the point along this perpendicular
        """
        if not isinstance(p, math3d.VectorN) or len(p) != len(self.mOrigin):
            raise ValueError("p must be a point of dimension " + str(len(self.mOrigin)))
        dirToP = p - self.mOrigin
        if dirToP.dot(self.mDirection) < 0:
            return None
        paraPart = dirToP.dot(self.mDirection) * self.mDirection
        perpPart = dirToP - paraPart
        if returnParaPerp:
            return (perpPart.magnitude(), paraPart, perpPart)
        else:
            return perpPart.magnitude()


class Sphere(object):
    """ A (probably 3d) spheroid """
    def __init__(self, center, radius, color):
        self.mCenter = center.copy()
        self.mRadius = radius
        self.mRadiusSquared = radius ** 2
        self.mColor = color

    def rayIntersection(self, R):
        if not isinstance(R, Ray) or len(R.mOrigin) != len(self.mCenter):
            raise ValueError("R must be a " + str(len(self.mCenter) + "-dimensional Ray"))

        dirToCenter = self.mCenter - R.mOrigin
        dist2 = dirToCenter.dot(dirToCenter)
        paraDist = dirToCenter.dot(R.mDirection)
        paraDist2 = paraDist ** 2
        perpDist2 = dist2 - paraDist2
        if perpDist2 > self.mRadiusSquared:
            return None

        paraOffset = (self.mRadiusSquared - perpDist2) ** 0.5

        # Good job for checking this!  If the ray is inside the spere, we *add* paraOffset.  If it's outside, we
        # subtract
        dirToCenter2 = dirToCenter.dot(dirToCenter)
        if dirToCenter2 <= self.mRadiusSquared:
            return paraDist + paraOffset
        elif dirToCenter.dot(R.mDirection) < 0:
            return None
        else:
            return paraDist - paraOffset


class Plane(object):
    """ A (probably 3d) infinite plane """

    def __init__(self, normalVec, d, color, isNormalNormalized = False):
        if isNormalNormalized:
            self.mNormal = normalVec.copy()
        else:
            self.mNormal = normalVec.normalized()
        self.mDistance = d                           # Distance from origin to plane (in direction of normal)
        self.mColor = color

    def rayIntersection(self, R):
        if not isinstance(R, Ray) or len(R.mOrigin) != len(self.mNormal):
            raise ValueError("R must be a " + str(len(self.mNormal) + "-dimensional Ray"))

        # If the ray is on the front of the plane and the plane normal and ray direction make an acute angle *OR*
        # If they ray is on the back of the plane and the plane normal and ray direction make an obtuse angle *OR*
        # If the ray direction and plane make a 90 degree angle,
        # The ray can't intersect the plane.
        rayOnFront = R.mOrigin.dot(self.mNormal) > self.mDistance
        rayDotNorm = R.mDirection.dot(self.mNormal)
        if rayDotNorm == 0.0 or (rayOnFront == (rayDotNorm >= 0.0)):
            # No hit possible!
            return None

        return (self.mDistance - R.mOrigin.dot(self.mNormal)) / R.mDirection.dot(self.mNormal)


class AABB(object):
    """ A axis-aligned bounding box """
    def __init__(self, ptA, ptB, color):
        self.mColor = color
        self.mMinPoint = ptA.copy()
        self.mMaxPoint = ptB.copy()
        for i in range(len(ptA)):
            if ptB[i] < self.mMinPoint[i]:       self.mMinPoint[i] = ptB[i]
            if ptA[i] > self.mMaxPoint[i]:       self.mMaxPoint[i] = ptA[i]
        self.mPlanes = []
        for i in range(len(ptA)):
            L = [0.0] * len(ptA)
            L[i] = 1
            posNorm = math3d.VectorN(*L)
            L[i] = -1
            negNorm = math3d.VectorN(*L)
            self.mPlanes.append(Plane(posNorm, posNorm.dot(self.mMaxPoint), color))
            self.mPlanes.append(Plane(negNorm, negNorm.dot(self.mMinPoint), color))

    def rayIntersection(self, R):
        minT = None
        epsilon = 0.0001
        for p in self.mPlanes:
            result = p.rayIntersection(R)
            if result != None:
                curDim = self.mPlanes.index(p) // 2
                hitPt = R.getPoint(result)
                for i in range(len(self.mMinPoint)):
                    if i == curDim:
                        continue
                    if hitPt[i] < self.mMinPoint[i] - epsilon or hitPt[i] > self.mMaxPoint[i] + epsilon:
                        hitPt = None
                        break
                if hitPt != None and (minT == None or result < minT):
                    minT = result
        return minT


class Polymesh(object):
    """ A 3d collection of triangles based on a wavefront obj file """
    def __init__(self, obj_fname, pos_offset, scale_factor, color = None):
        self.mVList = []          # A collection of 3d points (the 'v' lines in the file
        self.mFList = []          # A collection of 3-tuples which are the indices (the 'f' lines in the file)
        self.mFAreaSq = []
        self.mColor = color
        self.mPos = pos_offset
        self.mSFactor = scale_factor
        # This is an optimization -- if the aabb isn't hit (this test is cheap), we'll do the full test
        # to see which (if any) poly's are hit.
        self.mAABB = self.loadMesh(obj_fname, pos_offset, scale_factor)

    def triangleArea(self, a, b, c):
        v = a - b
        w = c - a
        result = v.cross(w)
        return result.magnitude()


    def loadMesh(self, fname, offset, sfactor):
        self.mPos = offset
        self.mSFactor = sfactor
        self.mVList = []
        self.mFList = []
        self.mFArea = []
        self.mFNorm = []
        self.mFDVal = []
        minPt = None
        maxPt = None

        fp = open(fname, "r")
        for line in fp:
            elem = line.strip().split(" ")
            if elem[0] == "v":
                v = math3d.VectorN(elem[1], elem[2], elem[3]) * sfactor + offset
                if minPt == None:
                    minPt = v.copy()
                    maxPt = v.copy()
                else:
                    if v[0] < minPt[0]:         minPt[0] = v[0]
                    if v[1] < minPt[1]:         minPt[1] = v[1]
                    if v[2] < minPt[2]:         minPt[2] = v[2]
                    if v[0] > maxPt[0]:         maxPt[0] = v[0]
                    if v[1] > maxPt[1]:         maxPt[1] = v[1]
                    if v[2] > maxPt[2]:         maxPt[2] = v[2]
                self.mVList.append(v)
            elif elem[0] == "f":
                if len(elem) != 4:
                    raise ValueError("Sorry -- I can only currently handle meshes with all triangles :-(")
                indicies = (int(elem[1]) - 1, int(elem[2]) - 1, int(elem[3]) - 1)
                va = self.mVList[indicies[0]]
                vb = self.mVList[indicies[1]]
                vc = self.mVList[indicies[2]]
                self.mFList.append(indicies)
                self.mFArea.append(self.triangleArea(va, vb, vc))
                self.mFNorm.append((va - vc).cross(vb - vc).normalized())
                self.mFDVal.append(va.dot(self.mFNorm[-1]))
        fp.close()

        return AABB(minPt, maxPt, self.mColor)

    def rayIntersection(self, R):
        minT = None
        # If the ray doesn't hit the AABB, it can't hit the triangles.  Bail out without the super-slow tests below
        if self.mAABB.rayIntersection(R) == None:
            return None
        epsilon = 0.0001
        for i in range(len(self.mFList)):
            # Don't consider back-faces
            if self.mFNorm[i].dot(R.mDirection) >= 0:
                continue
            # See where the ray hits the plane (if at all)
            p = Plane(self.mFNorm[i], self.mFDVal[i], self.mColor, True)
            result = p.rayIntersection(R)
            if result != None:
                hitPt = R.getPoint(result)
                # Calculate the barycentric coordinates of this hitPoint within the face
                ba = self.triangleArea(hitPt, self.mVList[self.mFList[i][1]], self.mVList[self.mFList[i][2]])
                bb = self.triangleArea(hitPt, self.mVList[self.mFList[i][0]], self.mVList[self.mFList[i][2]])
                bc = self.triangleArea(hitPt, self.mVList[self.mFList[i][0]], self.mVList[self.mFList[i][1]])
                if self.mFArea[i] - epsilon <= ba + bb + bc <= self.mFArea[i] + epsilon:
                    # See if this hit is closer than previous hits
                    if minT == None or result < minT:
                        minT = result
        return minT



import random
import pygame
import math

class VectorN(object):
    def __init__(self,*args):
        self.__mData=[]
        for i in args:
            self.__mData.append(float(i))
        self.__mDim=len(self.__mData)
    #returns a string containing the vector length, followed by the list
    def __str__(self):
        """returns the list as a string when it is printed"""
        String= "<Vector"+str(self.__mDim)+":"
        for i in range(len(self.__mData)):
            String+=str(self.__mData[i])
            if i<self.__mDim-1:
                String+=","
        String+=">"
        return String
    #returns the length of the list
    def __len__(self):
        """returns the length of the list"""
        return self.__mDim
    def __getitem__(self,index):
        """returns the requested item in the list"""
        return self.__mData[index]
    #sets the list objects to floats
    def __setitem__(self,index,new_Value):
        """similar to getitem, except it sets the items within the list to integers"""
        self.__mData[index] = float(new_Value)
    #Copies the list and returns it without the changes made
    def copy(self):
        """Copies and keeps the value even if the version that was copied from is changed"""
        return VectorN(*self.__mData)
    #checks to see if the vectors are equal to each other in length and values
    def __eq__(self,Vector_item):
        """Checks to see if the lists are equal and returns either True or False"""
        if isinstance(Vector_item,VectorN)==True and Vector_item.__mData == self.__mData:
            return True
        else:
            return False
    def int(self):
        """returns the list requested with each value in the list being converted to an integer"""
        New =[]
        for i in range(self.__mDim):
            New.append(int(self[i]))
        return tuple(New)
    def __add__(self,rhs):
        """takes each object in the first list and adds it by the object in the second list adding it to a new list"""
        New=self.copy()
        if isinstance(rhs,VectorN)==True:
            for i in range(len(self.__mData)):
                New[i] +=rhs[i]
            return New
        else:
            raise ValueError("You can only add another VectorN to this VectorN ")
            pass
    def __sub__(self,rhs):
        """subtracts each item in the first list by that object in the second list with the same position"""
        New=self.copy()
        if isinstance(rhs,VectorN)==True:
            for i in range(len(self.__mData)):
                New[i]-=rhs[i]
            return New
        else:
            raise ValueError("You can only subtract another VectorN from this VectorN")
            pass
    def __neg__(self):
        """takes the item in the list and returns the opposite value"""
        New=[]
        for i in range(self.__mDim):
            New.append(-1*(self[i]))
        return VectorN(*New)
    def __mul__(self,rhs):
        """scales the list by the scaler given"""
        New=[]
        if isinstance(rhs,int)==True or isinstance(rhs,float)==True:
            for i in range(self.__mDim):
                New.append(rhs*(self.__mData[i]))
            return VectorN(*New)
        else:
            raise ValueError("can only multiply VectorN by a scaler")
    def __rmul__(self,rhs):
        """does the same thing as __mul__ only it checks for if the given statment is reversed"""
        New=[]
        for i in range(self.__mDim):
            New.append(rhs*(self.__mData[i]))
        return VectorN(*New)
    def __truediv__(self, other):
        """This devides the VectorN"""
        New=[]
        for i in range(len(self.__mData)):
            New.append((self.__mData[i])/other)
        return VectorN(*New)
    def magnitude(self):
        """This is the length/distance of the VectorN"""
        New=0
        for i in self.__mData:
            New+=i**2
        return New**.5
    def magnitudeSquared(self):
        """Takes the length/magnitude of the VectorN and squares it"""
        New=0
        for i in self.__mData:
            New+=i**2
        return New
    def isZero(self):
        """Checks to see if their is a zero in the VectorN"""
        for i in self.__mData:
            if i!=0:
                return False

        return True
    def normalized(self):
        """The Normalize Method, takes the length of the vector and sets it to 1"""
        New=self/self.magnitude()
        return New
    def cross(self,V):
        """This is vector multiplication, returns a new vector of the two vectors given"""
        New=[]
        if isinstance(V,VectorN) and len(V)==3 and len(self.__mData)==3:
            for i in self.__mData:
                for i in V:
                    New=[(self.__mData[1]*V[2])-(self.__mData[2]*V[1]),(self.__mData[2]*V[0])-(self.__mData[0]*V[2]),(self.__mData[0]*V[1])-(self.__mData[1]*V[0])]
            return VectorN(*New)
        else:
            return ValueError("VectorN is either not VectorN, or not of equal length to other VectorN")
    def dot(self,V):
        """This multiplies both vectors by their positions and then adds up the values for a single value"""
        New=0
        if isinstance(V,VectorN) and len(V)==len(self.__mData):
            for i in range(len(self.__mData)):
                New+= self.__mData[i]*V[i]
            return New
        else:
            raise ValueError("VectorN is either not VectorN, or not of equal length to other VectorN")
    def pairwise_mult(self,V):
        """Similar to the dot method, instead of adding the numbers together, it leaves it as a new vector"""
        if isinstance(V,VectorN) and len(V)==len(self.__mData) and len(V)==3:
            New=[self.__mData[0]*V[0],self.__mData[1]*V[1],self.__mData[2]*V[2]]
            return VectorN(*New)
    def clamp(self,low=0,high=1):
        """The clamp method checks to see if the numbers are within range of the value between 0 and 1 and if they arnt,
        it sets it as the low or high if its above or below the set values to check for. """
        V=self.copy()
        for i in range(len(V.__mData)):
            if V[i] <low:
                V[i]=0
            if V[i] >high:
                V[i]=1
        return V

class MatrixN(object):
    def __init__(self,row,column,init_data=None):
        if init_data==None:
            pass
        elif len(init_data)!=row*column:
            raise ValueError("You need to the pass the correct amount of values in the matrix to equal the rows by the columns")
        else:
            self.init_data=init_data
            self.row=row
            self.column=column
            pass
        #for i in range(len(self.init_data):
        #    m=0
        #    [i]=[m:row+1]
        #    m+=row+1
        #    i=str(i)
    def __str__(self):
        pass

    def __mul__(self,rhs):
        if isinstance(rhs,MatrixN):
            pass
        elif isinstance(rhs, VectorN):
            pass
        else:
            return ValueError(rhs+": Is not a VectorN or MatrixN, check the list/values given.")

class Ray(object):
    def __init__(self,origin,direction):
        #This takes both vectors as points on the plain
        self.mOrigin=origin.copy()
        self.mDirection=direction.normalized()
        if isinstance(origin,VectorN) and isinstance(direction,VectorN) and len(self.mOrigin)==(len(direction)):
            pass
        else:
            return ValueError("One of the Vectors isnt a VectorN or isnt of equal length.")
    def getPoint(self,t):
        """This returns a point of an intersection along a ray and another ray, kind of like a collision"""
        N=self.mOrigin+(t*self.mDirection)
        return N
    def drawPygame(self,screen,color,width):
        """Draws a 2D projection of a ray on a surface given"""
        destPoint=self.getPt(1000)
        pygame.draw.line(screen,color,(self.mOrigin[0],self.mOrigin[1]),(destPoint[0],destPoint[1]),width)
    def getDistanceToPoint(self,Pos):
        """Para==Parallel, Perp==Perpendicular, Vector is the distance between the position and origin"""
        Vector=Pos-self.mOrigin
        VecPara=((Vector.dot(self.mDirection))/self.mDirection.dot(self.mDirection)*self.mDirection)
        VecPerp=Vector-VecPara
        if self.mDirection.dot(Vector)<0:
            return None
        return VecPerp.magnitude()

#This is my Camera Class
class Camera(object):
    def __init__(self,CameraPos,cameraObjInterest,up,fieldOfView,near,screen):
        #This is the 3d position of the camera in the world space
        if isinstance(CameraPos, VectorN):
            self.mPos= CameraPos
        else:
            raise ValueError("CameraPos given is not a VectorN")
        #This is the surface that is passed in for the Camera
        self.surf=screen
        #this is the surface width
        self.ScreenWidth= self.surf.get_width()
        #this is the surface hight
        self.ScreenHight= self.surf.get_height()
        #this is the AspectRatio for the camera
        self.AspectRatio=self.ScreenWidth/self.ScreenHight
        #this is the angle of the field of view(fov)
        self.fov=fieldOfView
        #this is the camera's object of Interest(coi) that it is looking at
        self.coi=cameraObjInterest
        #this is the indicated direction for the Camera's up direction
        self.up=up
        #this is how close the world sits to the Camera
        self.near=near
        #this is the view plane hight
        self.vph=2*self.near*math.tan(math.radians(self.fov/2))
        #this is the view plane width
        self.vpw=self.vph*self.AspectRatio
        #this is the z position for the camera
        self.z=(self.coi-self.mPos).normalized()
        #This is the x position for the camera
        self.x=(self.up.cross(self.z)).normalized()
        #This is the y position for the camera
        self.y=(self.z.cross(self.x)).normalized()
        A=self.near*self.z
        B=(self.vph/2)*self.y
        C=(self.vpw/2)*self.x
        self.vpo=self.mPos+(A+B-C)
        print(self.x)
        print(self.y)
        print(self.z)
        print(self.vpo)
        print(self.vph)
        print(self.vpw)
    def getPixelPos(self,x,y):
        C=((x/(self.surf.get_width()-1))*self.vpw)
        D=((y/(self.surf.get_height()-1))*self.vph)
        E=C*self.x
        F=-D*self.y
        G=self.vpo+E+F
        return G

#This is the plane Class
class Plane(object):
    def __init__(self,normal,distance,color):
        self.mNormal=normal.normalized()
        self.mDistance=distance
        self.mColor=color
    def rayIntersection(self,Ray):
        DirectionHat=Ray.mDirection
        Origin=Ray.mOrigin
        if self.mNormal.dot(DirectionHat)==0:
            return None
        N=(self.mDistance-Origin.dot(self.mNormal))/self.mNormal.dot(DirectionHat)
        if N<0:
            return None
        else:
            return (N,self.mNormal)

#This is the Sphere class
class Sphere(object):
    def __init__(self,mCenter,mRadius,color):
        self.mCenter=mCenter
        self.mRadius=mRadius
        self.mColor=color
    def rayIntersection(self,R):
        DirectionHat=R.mDirection
        Origin=R.mOrigin
        H=self.mCenter-Origin
        ParaDistance=H.dot(DirectionHat)
        PerpDistance=H.dot(H)-ParaDistance**2
        if PerpDistance>self.mRadius**2:
            return None
        Offset=(self.mRadius**2-PerpDistance)**.5
        Point=ParaDistance-Offset #Gets the point where the ray hits
        Norm=(R.getPoint(Point)-self.mCenter).normalized()
        if Point<0:
            return None
        else:
            return (Point,Norm)

#This is the Box class (AABB)
class AABB(object):
    def __init__(self, PointA, PointB, color):
        self.mColor=color
        self.mMinPoint=PointA.copy()
        self.mMaxPoint=PointB.copy()
        #This is to check to see if the points in min and max are correct
        for i in range(len(PointA)):
            if PointB[i] < self.mMinPoint[i]:
                self.mMinPoint[i]=PointB[i]
            if PointA[i]>self.mMaxPoint[i]:
                self.mMaxPoint[i]=PointA[i]
        self.mPlanes=[]
        for i in range(len(PointA)):
            L=[0.0]*len(PointA)
            L[i]=1
            posNorm=VectorN(*L)
            L[i]=-1
            negNorm=VectorN(*L)
            self.mPlanes.append(Plane(posNorm, posNorm.dot(self.mMaxPoint),color))
            self.mPlanes.append(Plane(negNorm, negNorm.dot(self.mMinPoint),color))
    def rayIntersection(self, R):
        minT = None
        Norm= None
        epsilon = 0.0001
        for p in self.mPlanes:
            result = p.rayIntersection(R)
            if result != None:
                curDim = self.mPlanes.index(p) // 2
                hitPt = R.getPoint(result[0])
                for i in range(len(self.mMinPoint)):
                    if i == curDim:
                        continue
                    if hitPt[i] < self.mMinPoint[i] - epsilon or hitPt[i] > self.mMaxPoint[i] + epsilon:
                        hitPt = None
                        break
                if hitPt != None and (minT == None or result[0] < minT):
                    minT = result[0]
                    Norm = result[1]
        if minT==None:
            return None
        else:
            return minT,Norm

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
                v = VectorN(elem[1], elem[2], elem[3]) * sfactor + offset
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
        Norm = None
        # If the ray doesn't hit the AABB, it can't hit the triangles.  Bail out without the super-slow tests below
        if self.mAABB.rayIntersection(R) == None:
            return None
        epsilon = 0.0001
        for i in range(len(self.mFList)):
            # Don't consider back-faces
            if self.mFNorm[i].dot(R.mDirection) >= 0:
                continue
            # See where the ray hits the plane (if at all)
            p = Plane(self.mFNorm[i], self.mFDVal[i], self.mColor)
            result = p.rayIntersection(R)
            if result != None:
                hitPt = R.getPoint(result[0])
                # Calculate the barycentric coordinates of this hitPoint within the face
                ba = self.triangleArea(hitPt, self.mVList[self.mFList[i][1]], self.mVList[self.mFList[i][2]])
                bb = self.triangleArea(hitPt, self.mVList[self.mFList[i][0]], self.mVList[self.mFList[i][2]])
                bc = self.triangleArea(hitPt, self.mVList[self.mFList[i][0]], self.mVList[self.mFList[i][1]])
                if self.mFArea[i] - epsilon <= ba + bb + bc <= self.mFArea[i] + epsilon:
                    # See if this hit is closer than previous hits
                    if minT == None or result[0] < minT:
                        minT = result[0]
                        Norm = result[1]
        if minT==None:
            return None
        else:
            return minT,Norm

#This gets the lightColor
def LightColor(self,AmbientColor,DiffuseColor,Specular):
    M=VectorN(0,0,0)
    for i in range(len(DiffuseColor)):
        M+=DiffuseColor[i]+Specular[i]
    lightColor=AmbientColor+M
    return LightColor

#Point Light Class
class LightSource(object):
    def __init__(self, Point, Diffuse, Specular):
        self.Point=Point
        self.Diffuse=Diffuse
        self.Specular=Specular
        #self.Attenuation=Attenuation

#Material Class
class Material(object):
    def __init__(self, Diffuse, Specular, Specular_Pow, Ambient):
        self.Diffuse=Diffuse
        self.Specular=Specular
        self.Specular_Pow=Specular_Pow
        self.Ambient=Ambient

if __name__=="__main__":
    import pygame
    v=VectorN(4,7,-3)
    w=VectorN(2,0,6)
    q=VectorN(5,9,-12)
    p=VectorN(0,0,0,0,0,0)
    print(v + w)                        # <Vector3: 6.0, 7.0, 3.0>
    print(v + w + q)                    # <Vector3: 11.0, 16.0, -9.0> #
    #print(v + 7)                        # ValueError: You can only add another Vector3 to this Vector3   (you passed '7').
    print(v - w)                        # <Vector3: 2.0, 7.0, -9.0> #
    #print(v - "abc")                    # ValueError: You can only subtract another Vector3 from this Vector3 (you passed 'abc').
    print(v * 2)                        # <Vector3: 8.0, 14.0, -6.0>
    print(3 * v)                        # <Vector3: 12.0, 21.0, -9.0>
    print(v / 2)                        # <Vector3: 2.0, 3.5, -1.5> #
    #print(v / w)                        # ValueError: You can only divide this Vector3 by a scalar.
    #  You attempted to divide by '<Vector3: 2.0, 0.0, 6.0>'. #
    #print(2 / v)                        # TypeError: unsupported operand type(s) for /: 'int' and 'VectorN'
    #print(v*w)
    print(-v)
    print(v.magnitude())
    print(v.magnitudeSquared())
    print(v.normalized())
    print(v.normalized().magnitude())
    print(q.isZero())
    print(p.isZero())
    print(v.dot(w))
    print(q.cross(v))
    print(v.pairwise_mult(w))
    print(v.clamp())
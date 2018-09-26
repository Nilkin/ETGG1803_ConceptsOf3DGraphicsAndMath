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
    def ReturnVector(self):
        return self.__mData
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
        """This statment checks to see if the List given is a Matrix and return it a as a new VectorN if it is
        Vector to Matrices multiplication."""
        if isinstance(rhs,MatrixN)==True:
            for column in range(rhs.column):
                AlternateValue=[]
                for row in range(rhs.row):
                    AlternateValue.append(rhs.Matrix[row][column])
                AlternateValue=VectorN(*AlternateValue)
                MatrixValue=self.dot(AlternateValue)
                New.append(MatrixValue)
            return VectorN(*New)
        elif isinstance(rhs,int)==True or isinstance(rhs,float)==True:
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
        self.row=row
        self.column=column
        self.init_data=init_data
        if self.init_data!=None:
            ListPosition=0
            self.MatrixData=init_data
            if len(self.MatrixData)!=self.row*self.column:
                raise ValueError("You do not have a long enough list of values equaling"+self.row*self.column+"positions")
            else:
                self.Matrix=[]
                for i in range(self.row):
                    AlternateList=[]
                    for c in range(self.column):
                        AlternateList.append(self.MatrixData[ListPosition])
                        ListPosition+=1
                    self.Matrix.append(AlternateList)
        else:
            self.Matrix=[]
            for i in range(self.row):
                AlternateList=[]
                for c in range(self.column):
                    AlternateList.append(0)
                self.Matrix.append(AlternateList)
    """This allows you to return the string format of the Matrix given, applying it in a row by column format"""
    def __str__(self):
        S=""
        for i in range(self.row):
            if i==0:
                S+="/"
            elif i==(self.row-1):
                S+="\\"
            else:
                S+="|"
            for c in range(self.column):
                if c==self.column-1:
                    S+=str(float(self.Matrix[i][c]))
                else:
                    S+=str(float(self.Matrix[i][c])) + "  "
            if i==0:
                S+="\\"+"\n"
            elif i==(self.row-1):
                S+="/"+"\n"
            else:
                S+="|"+"\n"
        return S
    """This makes a Copy of the Matrix you want to make a copy of and stores it as a new seperate Matrix"""
    def copy(self):
        NewList=[]
        for List in self.Matrix:
            for Index in List:
                NewList.append(Index)
        return MatrixN(self.row,self.column,NewList)
    """This allows you to get a certain value or index at the exact position given"""
    def __getitem__(self,IndexPosition):
        IndexRow=IndexPosition[0]
        IndexColumn=IndexPosition[1]
        return self.Matrix[IndexRow][IndexColumn]
    """This allows you to set a certain value to the exact position given"""
    def __setitem__(self,IndexPosition,ValueGiven):
        IndexRow=IndexPosition[0]
        IndexColumn=IndexPosition[1]
        self.Matrix[IndexRow][IndexColumn]=ValueGiven
    """The Multiply method checks to see if the matrix is full of ints and or floats
    then checks to see whether or not it is a VectorN or a MatrixN, then depending on which it is,
    it will multiply the values in the first Matrices columns, by the second Matrices rows.
    If the first Matrices columns is equal in length with the 2nd Matrices rows."""
    def __mul__(self,Matrix2):
        NewMatrix=[]
        if isinstance(Matrix2,int or float)==True:
            for row in range(self.row):
                for column in range(self.column):
                    NewMatrix.append(self.Matrix[row][column]*Matrix2)
            return MatrixN(self.row,self.column,NewMatrix)
        elif isinstance(Matrix2,VectorN)==True:
            for i in range(self.row):
                MatrixVec=VectorN(*self.Matrix[i])
                MatrixValue=MatrixVec.dot(Matrix2)
                NewMatrix.append(MatrixValue)
            return VectorN(*NewMatrix)
        else:
            return ValueError(Matrix2+": Is not a VectorN or MatrixN, check the list/values given.")
    """Allows you to pick out a certain index number by passing it a list of a row value and column value"""
    def __getitem__(self,IndexGiven):
        IndexRow= IndexGiven[0]
        IndexColumn= IndexGiven[1]
        return self.Matrix[IndexRow][IndexColumn]
    """Allows you to get the Vector tuple at the selected row"""
    def getRow(self,RowNum):
        Row=self.Matrix[RowNum]
        return VectorN(*Row)
    """The setRow function allows you to change all the Row numbers with the Vector Given"""
    def setRow(self,IndexPosition,Vec):
        if len(Vec)!=self.row+1:
            raise ValueError("must be a VectorN with the same size as:"+str(self.row))
        else:
            NewList=Vec.ReturnVector()
            self.Matrix[IndexPosition]=NewList
    """The setColumn function allows you to change the Column Numbers with the Vector Given"""
    def setColumn(self,IndexPosition,Vec):
        if len(Vec)!=self.column-1:
            raise ValueError("must be a VectorN with the same size as:"+str(self.column))
        else:
            NewList=Vec.ReturnVector()
            for i in range(len(Vec)):
                self.Matrix[i][IndexPosition]=NewList[i]
    """This is the True multiplication between two Matrixes"""
    def __rmul__(self, Matrix2):
        NewMatrix=[]
        if isinstance(Matrix2,int or float)==True:
            for row in range(self.row):
                for column in range(self.column):
                    NewMatrix.append(self.Matrix[row][column]*Matrix2)
            return MatrixN(self.row,self.column,NewMatrix)
    """The Transpose function flips the rows with the columns, so if its a 2x3, it will make it a 3x2"""
    def transpose(self):
        NewMatrix=[]
        for column in range(self.column):
            for row in range(self.row):
                NewMatrix.append(self.Matrix[row][column])
        return MatrixN(self.column,self.row,NewMatrix)


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
    a=MatrixN(4,3)
    b=MatrixN(2,3,(3.0145,7.2983,"2.314",1.9,-2,4.37562))
    print(a)
    MatrixN.sStrPrecision=2
    print(b)
    MatrixN.sStrPrecision=None
    print("b[0,0]="+str(b[0,0]))
    print("b[1,2]="+str(b[1,2])+"\n")
    c=a.copy()
    a[0,2]=99
    a[1,0]="100.2"
    a[3,1]=101.99999
    print(a)
    print(c)
    z=a.getRow(0)
    z[0]=123.4
    print("v="+str(v))
    print(a)
    b.setRow(0, VectorN(4,5,6))
    b.setColumn(2,VectorN(7,8))
    print(b.transpose())
    print(b)
    print(b*3)
    print(3*b)
    z=b*VectorN(5,4,2)
    print(v)
    z=VectorN(5,4)*b
    print(v)
    #print(b.inverse())
    #c=MatrixN(3,3,(0,1,2,1,0,3,4,-3,8))
    #print(c)
    #cI=c.inverse()
    #print(cI)
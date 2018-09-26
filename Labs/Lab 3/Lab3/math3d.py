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
        New=[]
        for i in range(len(self.__mData)):
            New.append((self.__mData[i])/other)
        return VectorN(*New)
    def magnitude(self):
        New=0
        for i in self.__mData:
            New+=i**2
        return New**.5
    def magnitudeSquared(self):
        New=0
        for i in self.__mData:
            New+=i**2
        return New
    def isZero(self):
        for i in self.__mData:
            if i!=0:
                return False

        return True
    def normalized(self):
        New=self/self.magnitude()
        return New
    def cross(self,VectorN):
        New=[]
        for i in self.__mData:
            for i in VectorN:
                New=[(self.__mData[1]*VectorN[2])-(self.__mData[2]*VectorN[1]),(self.__mData[2]*VectorN[0])-(self.__mData[0]*VectorN[2]),(self.__mData[0]*VectorN[1])-(self.__mData[1]*VectorN[0])]
        return VectorN(*New)
    def dot(self,VectorN):
        pass
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
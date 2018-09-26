import pygame

class VectorN(object):
    """ This class represents a general-purpose vector class.  We'll
        add more to this in later labs.  For now, it represents a
        position and/or offset in n-dimensonal space. """

    def __init__(self, *args):
        """
        The constructor
        :param args: This is a variable-length argument-list.  In reality, you create a VectorN like this:
               v = VectorN(1, 2, 3)
        :return: N/A for constructors
        """
        self.__mData = []
        for value in args:
            self.__mData.append(float(value))
        self.__mDim = len(self.__mData)

    def __add__(self, rightHandSide):
        """
        This method is called when you do:
            v + w       (where v is a VectorN)
        Note: Neither self nor rightHandSide are modified by this method.
        :param rightHandSide: Another VectorN (same dimension as this one, else an exception will be raised)
        :return: The vector sum of this vector and the rightHandSide
        """
        if not isinstance(rightHandSide, VectorN) or self.__mDim != rightHandSide.__mDim:
            raise ValueError("You can only add another Vector" + str(self.__mDim) +
                             " to this Vector" + str(self.__mDim) + " (you passed '" + str(rightHandSide) + "').")
        L = []
        for i in range(self.__mDim):
            L.append(self[i] + rightHandSide[i])
        return VectorN(*L)


    def __eq__(self, other):
        """
        Note: This method isn't normally called directly.  Instead, it is called indirectly when a VectorN
              is on the left-hand side of an ==.  It returns True if the values within the other vector
              are the same as those in this vector.
        :param other: any value
        :return: a boolean.  True if the other thing is a VectorN *and* has the same values as this VectorN.
        """
        if isinstance(other, VectorN) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        else:
            return False


    def __getitem__(self, index):
        """
        Note: You don't normally call this method directly.  It's called by using [] on a VectorN
            v = VectorN(1, 2, 3)
            print(v[0])                 # 1
            print(v[-1])                # 3
        :param index: An integer.  A python exception will be thrown if it's not a valid position in self.__mData
        :return: The float value at position index.
        """
        return self.__mData[index]


    def __len__(self):
        """
        Note: You don't normally call this method directly.  It's called by the built-in len function
            v = VectorN(1, 2, 4)
            print(len(v))           # 3
        :return: An integer indicating the dimension of this vector
        """
        return self.__mDim


    def __mul__(self, rightHandSide):
        """
        This method is called when you do:
            v * s       (where v is a VectorN)
        Note: Neither self nor rightHandSide are modified by this method.
        :param rightHandSide: A scalar (int / float, else an exception will be raised) multiplier
        :return: The vector product of this vector and the rightHandSide scalar
        """
        if not isinstance(rightHandSide, int) and not isinstance(rightHandSide, float):
            raise ValueError("You can only multiply this Vector" + str(self.__mDim) +
                             " and a scalar. You attempted to multiply by '" + str(rightHandSide) + "'.")
        L = []
        for i in range(self.__mDim):
            L.append(self[i] * rightHandSide)
        return VectorN(*L)



    def __neg__(self):
        """
        Returns the Vector negation of this Vector.  This is triggered when you do:
            -v      (where v is a VectorN)
        Note: self isn't modified
        :return: the Vector negation of this VectorN
        """
        L = []
        for i in range(self.__mDim):
            L.append(-self[i])
        return VectorN(*L)



    def __rmul__(self, leftHandSide):
        """
        This method is called when you do:
            s * v       (where v is a VectorN)
        Note: Neither self nor leftHandSide are modified by this method.
        :param leftHandSide: A scalar (int / float, else an exception will be raised) multiplier
        :return: The vector product of this vector and the leftHandSide scalar
        """
        # Note: I'm 'cheating' here -- just letting __mul__ do the hard work.
        return self * leftHandSide


    def __setitem__(self, index, newval):
        """
        This method is similar to __getitem__, but it is called when we assign something to an index
           v = VectorN(1, 2, 3)
           v[0] = 99
           print(v)                 # <Vector3: 1.0, 2.0, 99.0>
        :param index: An integer.  A python exception will be thrown if it's not a valid position in self.__mData
        :param newval: A value that can be converted to a float using the float function
        :return: None
        """
        self.__mData[index] = float(newval)


    def __str__(self):
        """
        Note: You don't normally call this directly.  It is called indirectly when you do something like:
            v = VectorN(1, 2, 3)
            x = str(v)               # Same as x = v.__str__()
            print(v)                 # print calls str internally
        :return: The string-representation of this VectorN
        """
        s = "<Vector" + str(self.__mDim) + ": "
        for i in range(len(self.__mData)):
            s += str(self.__mData[i])
            if i < self.__mDim - 1:
                s += ", "
        s += ">"
        return s



    def __sub__(self, rightHandSide):
        """
        This method is called when you do:
            v - w       (where v is a VectorN)
        Note: Neither self nor rightHandSide are modified by this method.
        :param rightHandSide: Another VectorN (same dimension as this one, else an exception will be raised)
        :return: The vector difference of this vector and the rightHandSide
        """
        if not isinstance(rightHandSide, VectorN) or self.__mDim != rightHandSide.__mDim:
            raise ValueError("You can only subtract another Vector" + str(self.__mDim) +
                             " from this Vector" + str(self.__mDim) + " (you passed '" + str(rightHandSide) + "').")
        L = []
        for i in range(self.__mDim):
            L.append(self[i] - rightHandSide[i])
        return VectorN(*L)


    def __truediv__(self, rightHandSide):
        """
        This method is called when you do:
            v / s       (where v is a VectorN)
        Note: Neither self nor rightHandSide are modified by this method.
        :param rightHandSide: A scalar (int / float, else an exception will be raised) divisor
        :return: The vector quotient of this vector and the rightHandSide
        """
        if not isinstance(rightHandSide, int) and not isinstance(rightHandSide, float):
            raise ValueError("You can only divide this Vector" + str(self.__mDim) +
                             " by a scalar. You attempted to divide by '" + str(rightHandSide) + "'.")
        L = []
        for i in range(self.__mDim):
            L.append(self[i] / rightHandSide)
        return VectorN(*L)



    def copy(self):
        """
        Creates a 'deep' copy of this VectorN and returns it
        :return: a new VectorN copy of this VectorN
        """
        return VectorN(*self.__mData)



    def magnitude(self):
        """
        :return: The scalar magnitude of this vector
        """
        m = 0.0
        for val in self.__mData:
            m += val ** 2
        return m ** 0.5



    def magnitudeSquared(self):
        """
        This is similar to the length method, but doesn't perform the square-root (which is slow and not
            needed in some applications)
        :return: The magnitude squared of this vector
        """
        m = 0.0
        for val in self.__mData:
            m += val ** 2
        return m



    def int(self):
        """
        :return: A tuple containing integer copies of the values in this VectorN.
        """
        L = []
        for i in range(self.__mDim):
            L.append(int(self[i]))
        return tuple(L)


    def isZero(self, tolerance = 0.0):
        """
        :param tolerance: an optional parameter.  If greater than zero, the vector is only considered non-zero
                      if the absolute value of one of its elements is greater than this tolerance
        :return: True if this is a zero vector, False if not
        """
        for val in self.__mData:
            if abs(val) > tolerance:
                return False
        return True



    def normalized(self):
        """
        Returns a normalized copy of this Vector (i.e. one which has a magnitude of 1.0)
            Note: This vector isn't modified by this operation
        :return: A normalized copy of this VectorN
        """
        m = self.magnitude()
        L = []
        for val in self.__mData:
            L.append(val / m)
        return VectorN(*L)


    def dot(self, rhs):
        """
        :param rhs: The other vector (must be of the same dimension as this vector)
        :return: The scalar dot product
        """
        if isinstance(rhs, VectorN) and len(self) == len(rhs):
            result = 0.0
            for i in range(len(self)):
                result += self[i] * rhs[i]
            return result
        else:
            raise ValueError("You can't take the dot product of this Vector" + str(self.__mDim) + " and '" + str(rhs) + "'")


    def cross(self, rhs):
        """
        :param rhs: The other vector (must be of the same dimension of this vector [which MUST be 3d or 2d])
        :return: The vector dot product (remember: it's not commutative)
        """
        if not isinstance(rhs, VectorN) or len(self) != len(rhs):
            raise ValueError("You can't take the cross product of this Vector" + str(self.__mDim) + " and '" + str(rhs) + "'")
        elif len(self) not in [2, 3]:
            raise ValueError("You can only do cross product in 2d or 3d, not " + str(self.__mDim) + "d.")
        elif len(self) == 3:
            return VectorN(self[1] * rhs[2] - self[2] * rhs[1], \
                           self[2] * rhs[0] - self[0] * rhs[2], \
                           self[0] * rhs[1] - self[1] * rhs[0])
        else:
            return VectorN(self[1] * rhs[0] - self[0] * rhs[1], \
                           self[0] * rhs[1] - self[1] * rhs[0])





if __name__ == "__main__":
    pass            # Nothing to test [here]:-)
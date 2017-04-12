'''Vector math'''
import math

class Vector(object):
    '''2D Vector'''
    def __init__(self, posxy):
        self.xpos = posxy[0]
        self.ypos = posxy[1]
        self.magnitude = 0

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector([self.xpos + other.xpos, self.ypos + other.ypos])
        else:
            return Vector([self.xpos + other, self.ypos + other])

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.xpos += other.xpos
            self.ypos += other.ypos
            return self
        else:
            self.xpos += other
            self.ypos += other
            return self

    def __sub__(self, other):
        if isinstance(other, int):
            return Vector([self.xpos - other, self.ypos - other])
        else:
            return Vector([self.xpos - other.xpos, self.ypos - other.ypos])


    def __mul__(self, rhs):
        '''multiply a Vector by another or by a scalar value'''
        if isinstance(rhs, Vector):
            return Vector([self.xpos * rhs.xpos, self.ypos + rhs.ypos])
        else:
            return Vector([self.xpos * rhs, self.ypos * rhs])

    def __div__(self, other):
        '''divide a Vector by a scalar value'''
        return Vector([self.xpos/float(other), self.ypos/float(other)])

    def __eq__(self, other):
        if self.xpos == other.xpos and self.ypos == other.ypos:
            return True
        return False

    def __str__(self):
        return "<" + str(self.xpos) + "," + str(self.ypos) + ">"

    @staticmethod
    def scalarmult(vec, scal):
        '''multiplies a Vector by a scalar'''
        tmp = Vector([(vec.xpos * scal), (vec.ypos * scal)])
        return tmp

    @staticmethod
    def mag(vec):
        '''gets the magnitude of a Vector'''
        vec.magnitude = float(math.sqrt((vec.xpos * vec.xpos) + (vec.ypos * vec.ypos)))
        return vec.magnitude

    @staticmethod
    def normal(vec):
        '''normalizes a Vector'''
        if Vector.mag(vec) == 0:
            return Vector([vec.xpos / (1), vec.ypos / (1)])
        return Vector([vec.xpos / vec.magnitude, vec.ypos / vec.magnitude])

    def dotprod(self, avector):
        '''gets the dot product'''
        return float((self.xpos * avector.xpos) + (self.ypos * avector.ypos))

    def print_info(self):
        '''Prints Vector coordinates'''
        print(str(self.xpos), str(self.ypos))
        
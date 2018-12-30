from __future__ import print_function
import math

class Shape(object):
    def __init__(self):
        self.color ="red"
        self.sides = 0

    def calArea(self):
        return 0

class Quadrilateral(Shape):
    def __init__(self,w,l,c):
        self.sides = 4
        self.width = w
        self.length = l
        self.color = c

    def calArea(self):
        return self.width*self.length

class Square(Quadrilateral):
    def __init__(self,w,c):
        super(Square,self).__init__(w,w,c)


class Circle(Shape):
    def __init__(self, r, c):
        super(Circle,self).__init__()
        self.radius = r
        self.color = c

    def calArea(self):
        return self.radius**2*math.pi

class Trinagle(Shape):
    def __init__(self,s1,s2,s3,c):
        Shape.__init__(self)
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.color = c

def printArea(s):
        print(s.calArea())

sq1 = Square(5,"Green")
sq2 = Square(9, "Black")
c1 = Circle(10,"Orange")
t1 = Trinagle(3,4,5,"Red")


print("Circle", c1.radius,c1.color)
print(sq1.calArea())
print(c1.calArea())
print(printArea(t1))



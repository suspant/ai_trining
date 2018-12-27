from __future__ import print_function
import math
import random

class Circle:

    #consturctor function
    def __init__(self):
        self.radius = random.uniform(1.1,9.5)

    def calCircumference(self):
        return math.pi * 2 * self.radius
    def calDiameter(self):
        return self.radius * 2
    def calArea(self):
        return math.pi * (self.radius **2)


circles = []
for i in range(0,10):
    c= Circle()
    #c.radius = random.uniform(1.1,9.5)
    #c.circumference = c.calCircumference()
    circles.append(c)

for c in circles:
    print("Radius:",c.radius, "Circumference:",c.calCircumference(), "Diameter:", c.calDiameter(),"calArea:",c.calArea() )

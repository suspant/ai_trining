from __future__ import print_function
import math
import random

class Circle:
    def calCircumference(self):
        return math.pi * 2 * self.radius

circles = []
for i in range(0,10):
    c= Circle()
    c.radius = random.uniform(1.1,9.5)
    #c.circumference = c.calCircumference()
    circles.append(c)

for c in circles:
    print("Radius:",c.radius, "Circumference:",c.calCircumference() )

from __future__ import print_function
import math
import random

class Circle:
    def calCircumference(radius):
        return math.pi * 2 * radius

circles = []

for i in range(0,10):
    c= Circle()
    c.radius = random.uniform(1.1,9.5)
    c.circumference = c.calCircumference(c.radius)
    circles.append(c)

for c in circles:
    print("Radius:",c.radius, "Circumference:", c. circumferences)

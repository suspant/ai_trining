from __future__ import print_function
import math

def circumference(radius):
    return math.pi * 2 * radius

circles = [["First circle",4.4,0],["Second Circle", 3.7,0],["Third Circle", 8.4,0]]
circles[0][2] = circumference(circles[0][1])
print(circles[0][2])
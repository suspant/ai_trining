from __future__ import print_function
import math

def circumference(radius):
    return math.pi * 2 * radius

## just define few different circle

circle1Name = "First Circle"
circle1Radius = 4.4

circle2Name = "Second Circle"
circle2Radius = 3.7

circle3Name = "Third Circle"
circle3Radius = 8.4

circumference1 = circumference(circle1Radius)
circumference2 = circumference(circle2Radius)
circumference3 = circumference(circle3Radius)

print(circumference1,circle1Name)
print(circumference2,circle2Name)
print(circumference3,circle3Name)


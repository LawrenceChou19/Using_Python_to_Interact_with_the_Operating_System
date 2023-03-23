#!/usr/bin/env python3
print("HELLO" *10)


#areas.py
import math
def triangle(base,height):
    return base * height/2
def rectangle(base,height):
    return base * height
def circle(radius):
    return math.pi*(radius**2)

print('Triangle is ',triangle(3,5))
print('Rectangle is ',rectangle(3,5))
print('Circle is ',circle(5))

def donut(outside_radius,inside_radius):
    return circle(outside_radius) - circle(inside_radius)
print('donut is ',donut(7,5))



#!/usr/bin/env python
# coding: utf-8


diameter = float(input("Enter Diameter: "))
angle_degrees = 45
pi = 3.1416

radius = (diameter / 2)

angle_radians = (pi / 180) * angle_degrees
arc_length = radius * angle_radians

print("Diameter of circle:", diameter)
print("Angle measure:", angle_degrees)
print("Arc Length is:", arc_length)

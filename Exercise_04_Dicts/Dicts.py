# -*- coding: utf-8 -*-
"""
Created on Thu May  1 01:03:27 2025

@author: saad saeed minhas
"""
students = [
     {'name': 'Alice', 'grades': [90, 85, 92]},
     {'name': 'Bob', 'grades': [70, 88, 80]},
     {'name': 'Charlie', 'grades': [95, 93, 97]}
]

# * Iterates through the list of dictionaries.
# * For each student, calculates their average grade.
# * It sorts the grade.
# * Adds a new key to the dictionary named 'average' that stores their average grade.
# * Returns a list of dictionaries with the students' names and their average grades.

for student in students:
    grades = student['grades']
    average = round(sum(grades)/len(grades),2)
    sorted_grades = sorted(grades)
    student['grades'] = sorted_grades
    student['average'] = average
    
print(students)
# -*- coding: utf-8 -*-
"""
Created on Thu May  1 00:39:45 2025

@author: saad saeed minhas
"""
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
vowels = 'aeiou'
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit.lower() if letter in vowels) > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
vowels = 'aeiou'
fruits_with_only_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit.lower() if letter in vowels) == 2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_five_chars)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_five_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_exactly_five_chars)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_five_chars)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
num_of_chars = [len(fruit) for fruit in fruits]
print(num_of_chars)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_letter_a)

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers
even_numbers = [number for number in numbers if number %2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number %2 != 0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
sorted_positive_numbers = sorted(positive_numbers)
print(sorted_positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
sorted_neg_num = negative_numbers
print(sorted_neg_num)

#When to use list comprehension and when to use for loops?
# Use list comprehensions for short, readable list transformations
# Use for loops when logic is complex, involves side effects, or have multiple steps.
















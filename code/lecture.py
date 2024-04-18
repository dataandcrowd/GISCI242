# Examples of Bad Coding
print("Python" > "R")
print("Python" < "R")

import string
print(string.ascii_lowercase)
print(string.ascii_lowercase[0:3])

# Simple Python Maths and Strings
print(1 + 1)
print("hello world")
print(len("hello world"))

# fun stuff
a = 1
b = 2
print(a + b)

# Facing Errors with maths
#sin(3)

import math
math.sin(3)
math.sqrt(4)

# Lists
top = ["socks", "underwear", "handkerchief"]
middle = ["T-shirts", "Pajamas", "Trousers", "Shorts"]
bottom = [30, 73, 100, 62]

print(top[0])
print(min(bottom))


import statistics as stats
print(stats.mean(bottom))


station_names = [
    "Britomart",
    "Ōrākei",
    "Meadowbank",
    "Purewa",
    "Glen Innes",
    "Tamaki",
    "Panmure",
    "Sylvia Park"
]

print(station_names)

station_names.append("new station")
print(station_names)




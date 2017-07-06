# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4192698630/concepts/48904185560923

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# Add your own code and notes here

# Variables Quiz
# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0 # 2.7 GHz
print speed_of_light / cycles_per_second

# Variables Can Vary

# Spirit Age
# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.
age = 24
days = age * 365
print days

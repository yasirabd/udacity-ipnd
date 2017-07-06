# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4180729266/concepts/49786550990923

print 3
print 1 + 1

# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
print 7 * 7 * 24 * 60

# Backus-Naur Form
# grammar for programming, it can describe the languange of programming

# example
# <non-terminal> -> replacement
#           sentece
#   subject     verb    object
#   noun        verb    object
#   I           like    noun
#                       Python

# Python Grammar for Arithmetic Expressions
# Expression    -> Expressions Operator Expressions
# Expression    -> Number
# Operator      -> +
# Operator      -> *
# Number        -> 0,1,2,..
# Expression    -> ( Expression )

# example
#               Expressions
#   Expressions    Operator     Expressions
#   Number         +            Number
#   2                           3

# in centimeters in one nanosecond.  Use the values
# defined below.
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second
print 299792458 * 100 * 1.0/1000000000

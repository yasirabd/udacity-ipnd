# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
# 1. Detect current time in PC as a start time
# 2. Determine the range time for the break (2 hrs)
# 3. Using loop to check range of current time and start time if equals range time (2 hrs)
#       - If so, play music

import webbrowser
import time

# Your code here.
breaks = 3
count = 0

print "This program started on " + time.ctime()
while count < breaks:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=vXQlYhLcQ2c")
    count += 1

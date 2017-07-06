# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4192698630/concepts/49819819440923

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Add your own code and notes here

# Augusta Ada King Countess of Lovelace

# Quiz Hello!!!
name = "Yasir"
print name

# This code shows some basic variable assignment and string printing.
# name = "Andy"
# print "Hello " + name
# print name * 4

# This code shows the difference between the string "4" and the number 4.
# Remove the four comment characters (#) on the lines below to see what happens.
# print 4
# print "4"
# print 4 + 4
# print "4" + "4"

# This code shows some of the different mistakes that are easy to make while
# working with strings. Remove one comment at a time and press Test Run to
# see what happens. Be sure to re-comment before moving on or the program
# will keep showing you an error.
#print 'hello"
#print hello
#print "hello

# This code will give you a peek at what you are about to learn! Uncomment
# all of the lines below to get a glimpse of "string indexing"
#name = "Andy"
#print name[0]
#print name[1]
#print name[2]
#print name[3]

# Same Value Quiz
# s = 'Andy'
# print s[3], s[1+1+1]
# print s[0], (s+s)[0]
# print s[0] + s[1], s[0+1]
# print s[1], (s + 'ity')[1]
# print s[-1], (s+s)[-1]

# Selecting Sub sequences
# word = 'assume'
# print word[3]
# print word[4:6]
# print word[4:]
# print word[:2]
# print word[:]

# Capital Udacity Quiz
# Write Python code that prints out Udacity (with a capital U),
# given the definition of s below.
# s = 'audacity'
# print 'U' + s[2:]

# Undestanding Selection Quiz
s = 'Andy'
print s[:]
print s + s[0:-1+1]
print s[0:]
print s[:-1]
print s[:3] + s[3:]

# Testing find 2 Quiz
s = 'any string'
print s.find(s)
print s.find('s')
print 's'.find('s')
print s.find('')
print s.find(s + '!!!') + 1

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1

# This segment is just a chance for you to play around with
# finding strings within strings. Read through the code and
# press Test Run to see what it does. Is there anything
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string

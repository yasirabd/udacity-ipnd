# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
# step 1 - select folder
# step 2 - for files in folder
# step 2.1 - remove numbers
#

# Your code here.
import os

def rename_files():
    # 1. get file names from the folder
    file_list = os.listdir(r"E:\Udacity\Intro to Programming\udacity-ipnd\stage_3\lesson_3.2_using_functions\secret_message\prank")
    print file_list

    # check the current working directory
    saved_path = os.getcwd()
    # print "Current Working Directory is " + saved_path

    # changes directory
    os.chdir(r"E:\Udacity\Intro to Programming\udacity-ipnd\stage_3\lesson_3.2_using_functions\secret_message\prank")

    # 2. for each file, rename filenames
    for file_name in file_list:
        print "Old name - " + file_name
        print "New name - " + file_name.translate(None, "0123456789") 
        os.rename(file_name, file_name.translate(None, "0123456789"))

    # changes back the path
    os.chdir(saved_path)
rename_files()

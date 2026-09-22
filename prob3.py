#------------------------------
# Group Members: Laureate Clei Balba, Aleeyah Dela Vega, Chrizzia Jillian Medrano
# Section: 8-Adelfa
# Title: Activity 7, Problem 3 - School Grade Level Validator
# Date: 09/22/26
#------------------------------

#--Assign the allowed/accepted grade levels--
valid_grade_level = ["7", "8", "9", "10", "11", "12,"]

#--Acquire the user's grade level--
grade_level = int(input("Enter you grade level: "))

#--Verify if the grade level the user inputted is one of the valid grade levels, and output the result--
if grade_level in valid_grade_level:
    print("Valid grade level.")
else:
    print("Invalid grade level.")
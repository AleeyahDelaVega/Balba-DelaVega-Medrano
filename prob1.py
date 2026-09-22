#------------------------------
# Group Members: Laureate Clei Balba, Aleeyah Dela Vega, Chrizzia Jillian Medrano
# Section: 8-Adelfa
# Title: Activity 7, Problem 1 - Student Age Validator
# Date: 09/22/26
#------------------------------

try:
    #--Ask the student for their age--
    student_age = int(input("Enter your age: "))
    #--Check is the student's age is only 12-18, then output each result based on if their age is valid or invalid.
    if 12 <= student_age <= 18:
        print("Valid age.")
    else:
        print("Invalid age. Must be from 12 to 18.")
except ValueError:
    #--Display this result if the student typed out their age with letters--
    print("Invalid input. Please enter a whole number.")
#------------------------------
# Group Members: Laureate Clei Balba, Aleeyah Dela Vega, Chrizzia Jillian Medrano
# Section: 8-Adelfa
# Title: Activity 7, Problem 2 - Username Validator
# Date: 09/22/26
#------------------------------

#--Ask user for their username--
username = input("Enter username: ")

#--Verify if the username only contains 5-10 alphanumeric characters. Then, output each result based on if the username's valid or not--
if 5 <= len(username) <= 10 and username.isalnum():
    print("Valid username.")
else:
    print("Invalid username.")
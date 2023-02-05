# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 10/12/2022
# Description: asks the user to enter a positive integer
# then finds all factors of that integer and prints them






user_integer = int(input("Please enter a positive integer: "))
print("The factors of", user_integer, "are:")
for integer in range(1, 1 + user_integer):
    if user_integer % integer == 0:
        print(integer)

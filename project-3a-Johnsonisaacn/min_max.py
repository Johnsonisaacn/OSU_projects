# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 10/12/2022
# Description: Asks the user how many integers they want to enter,
# prompts them to enter that many integers, then prints the maximum
# and minimum values of their entries
print("How many integers would you like to enter? ")
NUM_INTEGERS = int(input())
counter = 1
print("Please enter", NUM_INTEGERS, "integers")
max = min = int(input())
while counter < NUM_INTEGERS:
    number = int(input())
    if number >= max:
        max = number
    if number <= min:
        min = number
    counter += 1
print("min:", min)
print("max:", max)

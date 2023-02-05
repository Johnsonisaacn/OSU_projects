# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 10/12/2022
# Description: the program asks the user to enter an integer
# then prompts a player to guess that integer by entering integers
# until the correct one is guessed, giving hints if guesses are too
# high or too low

print("Enter the integer for the player to guess.")
hidden_num = int(input())
counter = 1
print("Enter your guess.")
guess = int(input())
if guess == hidden_num:
    print("You guessed it in 1 try.")
else:
    while guess != hidden_num:
        if guess > hidden_num:
           print("Too high - try again:")
        if guess < hidden_num:
            print("Too low - try again:")
        guess = int(input())
        counter += 1
    print("You guessed it in", counter, "tries.")

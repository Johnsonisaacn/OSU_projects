# Author: Isaac Johnson
# Github username: Johnsonisaacn
# Date: 10/05/2022
# Description: gives change with the fewest number of coins

print("Please enter an amount in cents less than a dollar.")
total = int(input())
quarters = total // 25
total = total % 25
dimes = total // 10
total = total % 10
nickels = total // 5
total = total % 5
pennies = total
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)

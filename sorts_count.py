# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 2/1/2023
# Description: counts the number of comparisons between values in lists using bubble sort and using insertion sort

def bubble_count(a_list):
  """Counts the number of comparisons between values using insertion sorting"""

  comparisons = 0
  exchanges = 0
  for pass_num in range(len(a_list) - 1):
    for index in range(len(a_list) - 1 - pass_num):
      comparisons += 1
      if a_list[index] > a_list[index + 1]:
        temp = a_list[index]
        a_list[index] = a_list[index + 1]
        a_list[index + 1] = temp
        exchanges += 1
  return (comparisons, exchanges)

def insertion_count(a_list):
  """Counts the number of comparisons between values using insertion sorting"""

  comparisons = 0
  exchanges = 0
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      comparisons += 1
      a_list[pos + 1] = a_list[pos]
      exchanges += 1
      pos -= 1

    a_list[pos + 1] = value
  return (comparisons, exchanges)


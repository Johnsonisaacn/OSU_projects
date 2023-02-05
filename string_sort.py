# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 2/1/2023
# Description: sorts a list of strings in place

def string_sort(string_list):
  """sorts a list of strings in ascending order regardless of capitalization"""
  for string in range(1, len(string_list)):
    value = string_list[string]
    pos = string - 1
    while pos >= 0 and string_list[pos].upper() > value.upper():
      string_list[pos + 1] = string_list[pos]
      pos -= 1
    string_list[pos + 1] = value



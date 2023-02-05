# Author: Isaac Johnson
# GitHub UserID: Johnsonsisaacn
# Date: 11/16/2022
# Description: takes lists of employee names, employee IDs, salaries, and emails and
# using class Employee, creates a dictionary of the data

class Employee:
    """Stores data about employees including name, ID number, salary, and email address"""
    def __init__(self, name, ID_number, salary, email_address):
        """initialize data members with argument values"""
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address
    def get_name(self):
        """passes employee name"""
        return self._name
    def get_ID_number(self):
        """passes ID number"""
        return self._ID_number
    def get_salary(self):
        """passes employee's salary"""
        return self._salary
    def get_email_address(self):
        """passes employee's email address"""
        return self._email_address

def make_employee_dict(names=None, IDs=None,salaries=None,emails=None):
    """Takes four lists of equal length and with data from the lists creates Employee
    objects
    """
    if names is None:
        names = []
    if IDs is None:
        IDs = []
    if salaries is None:
        salaries = []
    if emails is None:
        emails = []
    employee_database = {}
    for i in range(0,len(names)):
        employee_database[IDs[i]] = Employee(names[i],IDs[i],salaries[i],emails[i])
    return employee_database



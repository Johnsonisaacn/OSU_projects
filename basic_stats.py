# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 1/11/2023
# Description: Class Student that takes student names and grades as parameters and a function basic_stats
# that takes a list of Student objects and returns the mean, median, and mode of student's grades
from statistics import mean, median, mode
class Student:
    """creates Student objects with name and grade as parameters, includes a function get_grade to return the student's grade"""
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    def get_grade(self):
        return self._grade
def basic_stats(students, student_grades=None):
    """takes a list of Student objects as a parameter and returns a tuple containing the mean, median, and mode of the grades
    of the students"""
    if student_grades is None:
        student_grades = []
    for student in students:
        student_grades.append(student.get_grade())
    grade_mean = mean(student_grades)
    grade_median = median(student_grades)
    grade_mode = mode(student_grades)
    grade_stats = (grade_mean, grade_median, grade_mode)
    return grade_stats



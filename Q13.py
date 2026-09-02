# # Write a NumPy program using the following student marks:Find all students who scored 70 or above.
# Find all students who failed, where failing means marks < 40.
# Count how many students scored 70 or above.
# Calculate the average marks of students who scored 70 or above.
# Find the highest mark among students who scored 70 or above.
# Replace every mark below 40 with 40.
# Create a new array containing only marks between 50 and 80, inclusive.

import numpy as np

marks = np.array([45, 78, 92, 33, 67, 88, 54, 95, 41, 73, 29, 81])

# Find all students who scored 70 or above
students_above_70 = marks[marks >= 70]
print("Students who scored 70 or above:", students_above_70)

# Find all students who failed (marks < 40)
failed_students = marks[marks < 40]
print("Students who failed:", failed_students)

# Count how many students scored 70 or above
count_above_70 = np.sum(marks >= 70)
print("Number of students who scored 70 or above:", count_above_70)

# Calculate the average marks of students who scored 70 or above
average_above_70 = np.mean(students_above_70)
print("Average marks of students who scored 70 or above:", average_above_70)

# Find the highest mark among students who scored 70 or above
highest_above_70 = np.max(students_above_70)
print("Highest mark among students who scored 70 or above:", highest_above_70)

# Replace every mark below 40 with 40
marks[marks < 40] = 40
print("Array after replacement:", marks)

# Create a new array containing only marks between 50 and 80, inclusive
marks_between_50_and_80 = marks[(marks >= 50) & (marks <= 80)]
print("Marks between 50 and 80 (inclusive):", marks_between_50_and_80)
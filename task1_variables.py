"""Task 1: Variables and variable names  (lesson 1.1 and 1.2)

Edit this file, then run:  python task1_variables.py
Replace every TODO. Do not rename the variables or functions.
"""

# 1. Create four variables about yourself.
#    student_name -> a string (not empty)
#    age          -> an int
#    gpa          -> a float
#    is_enrolled  -> a bool
student_name = "RUEL SHEPHERD CUDAL"  # TODO
age = 20  # TODO
gpa = 4.0  # TODO
is_enrolled = true  # TODO

# 2. Swap the values of a and b WITHOUT creating a third variable.
#    After your code runs, a must be 7 and b must be 3.
a, b = b, a
# TODO: swap them here (hint: multiple assignment)
b = a
a = b
# 3. Which of these are valid Python variable names?
#    Put ONLY the valid ones in the list, in the same order they appear.
candidates = ["my_var", "2nd_place", "_hidden", "first-name", "Total", "for", "user name", ""]
valid_names = ["my_var", "_hidden", "Total"]  # TODO

# 4. One line that assigns the value 0 to x, y and z at the same time.
# TODO: write it here, e.g. x = ...
x = y = z = 0
if __name__ == "__main__":
    print(student_name, age, gpa, is_enrolled)
    print(a, b)
    print(valid_names)

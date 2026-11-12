"""Task 1: Variables and variable names  (lesson 1.1 and 1.2)

Edit this file, then run:  python task1_variables.py
Replace every TODO. Do not rename the variables or functions.
"""

# 1. Create four variables about yourself.
student_name = "Jhonrhane Elarcosa"
age = 18
gpa = 1.75
is_enrolled = True

# 2. Swap the values of a and b WITHOUT creating a third variable.
a = 3
b = 7
a, b = b, a

# 3. Which of these are valid Python variable names?
candidates = ["my_var", "2nd_place", "_hidden", "first-name", "Total", "for", "user name", "x1"]
valid_names = ["my_var", "_hidden", "Total", "x1"]

# 4. Assign the value 0 to x, y and z at the same time.
x = y = z = 0

if __name__ == "__main__":
    print(student_name, age, gpa, is_enrolled)
    print(a, b)
    print(valid_names)
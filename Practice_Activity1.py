#Activity 1.


#name = input("Enter your name: ")
#age = input("Enter your age: ")
#course = input("Enter your course: ")

#print("=========STUDENT INFORMATION===========")
#print("name: ", name)
#print("Age: ", age)
#print("course", course)


#Activity 2.

#word = input("Enter word: ")

#print("Original: ", word)
#print("UpperCase: ", word.upper())
#print ("Lowercase: ", word.lower())
#print("Title: ", word.title())
#print("length: ", len(word))
#print("first character: ", word[0])
#print("last character: ", word[-1])

#Activity 3

#word = input("Enter a word: ")

#print("first 3: ", word.strip())
#print("Replace: ", word.replace("a", "@"))
#print("Number of 'a':", word.count("a"))
#print("position of 'a': ", word.find("a"))
#print("words: ", word.split())

#Activity 4

#word = input("Enter a word: ")

#print("first 3: ", word[:3])
#print("last 3: ", word[-3:])
#print("Index 1 to 4: ", word[1:4])
#print("reverse: ", word[::-1])

#Activity 5

#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))

#print("Addtion: ", num1 + num2)
#print("Subtraction: ", num1 - num2)
#print("Multiplication: ", num1 * num2)
#print("Division: ", num1 / num2)
#print("Floor Division: ", num1 // num2)
#print("Modulo: ", num1 % num2)
#print("Exponent: ", num1 ** num2)

#Activity 6

#num1 = input("Enter first number: ")
#um2 = input("Enter second number: ")

#num1 = int(num1)
#num2 = int(num2)

#total = num1 + num2

#print("Total: ", total)

#Activity 7

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("Equal: ", a == b)
#print("Not equal: ", a != b)
#print("Greater: ", a > b)
#print("Less: ", a < b)
#print("Greater or equal: ", a >= b)
#print("less or equal: ", a <= b)

#Activity 8

#age = int(input("Enter your age: "))

#if age >= 18:
    #print("Adult")
#else:
    #print("Minor")

#Activity 9

#grade = float(input("Enter your grade: "))

#if grade >= 90:
#    print("Excellent")
#elif grade >= 80:
#    print("very good")
#elif grade >= 75:
#    print("Passed")
#else:
#    print("Failed")


#Activity 10

#num = int(input("Enter a number: "))

#result = "Positive" if num >= 0 else "Negative"

#print(result)

#Activity 11

#age = int(input("Enter your age: "))
#has_id = input("Do you have an ID (Yes/NO): ")

#if age >= 18 and has_id == "yes":
 #   print("Entry allowed")
#else:
#    print("Enry denied")

#Activity 12

#x = 10
#print(x > 5 and x < 20)

#x = 10
#print(x < 5 or x == 10)

#x = 10
#print(not x == 10)

#Activty 13

#x = 0

#if x != 0 and 10 / x > 1:
#    print("yes")
#else:
#    print("no")

#Activity 14

#num = int(input("Enter a number: "))

#if 1 <= num <= 100:
#    print("Number is within the range.")
#else:
#    print("Number is outside the eange.")

#Final

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
quiz1 = int(input("Enter your quiz 1: "))
quiz2 = int(input("Enter your quiz 2: "))
quiz3 = int(input("Enter your quiz 3: "))


print("==========STUDENT INFORMATION============")
print("Name: ", name)
print("Age: ", age)
print("course: ", course)
print("\n")

total = quiz1 + quiz2 + quiz3
average = total / 2
if average >= 75:
    status = "PASSED"
    remark = "Good"
elif average >= 90:
    status = "PASSED"
    remark = "Excellent!!"
elif average >= 85:
    status = "PASSED"
    remark = "Very good"
else:
    status = "Failed"

age_status = "Adult" if age >= 18 else "minor"

print("Total: ", total)
print("Average: ", round(average, 2))
print("Status: ", status)
print("Remark: ", remark)
print("Age Status: ", age_status)
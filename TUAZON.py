# Create a simple python program that asks the user to enter student name,id #,course and section, an 4 quarter grades
# Get the average of 4 quarter grades using math expressions

Name = input("Enter name:  ")
Student = input("Enter Student ID: ")
Section = input("Enter Course/Section: ")
print("Average grade Calculator")
Grade1 = eval(input("Enter First Quarter Grade: "))
Grade2 = eval(input(" Enter Second Quarter Grade:"))
Grade3 = eval(input("Enter Third Quarter Grade: "))
Grade4 = eval(input("Enter Fourth Quarter Grade: "))
Average = (Grade1 + Grade2 + Grade3 + Grade4) / 4
print("Student Name: ", Name)
print("Student ID No.:", Student)
print("Course/Section:", Section)
print("First Quarter Grade:", Grade1)
print("Second Quarter Grade:", Grade2)
print("Third Quarter Grade:", Grade3)
print("Fourth Quarter Grade:", Grade4)
print("Your General Average is:", Average)

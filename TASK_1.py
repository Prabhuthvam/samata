#problem Statement
'''
Write a Python function calculate_area that takes two parameters: length and width. It 
should calculate and return the area of a rectangle. However, add a condition: if the length 
is equal to the width, return "This is a square!" instead of the area. Then, write a program to 
input values for length and width from the user and call the calculate_area function to 
display either the area or the message.'''

# user input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Checking the condition
if length == width:
    print("This is a square!")
else:
    area = length * width
    print("The area of the rectangle is:", area)

# Example Output
'''
Enter the length: 5
Enter the width: 10
The area of the rectangle is: 50.0

Enter the length: 5
Enter the width: 5
This is a square!
'''

# Problem Statement:
'''
Write a Python program that generates the Fibonacci sequence up to a specified number of 
terms, n. The Fibonacci sequence starts with 0 and 1, and each subsequent number in the 
sequence is the sum of the two preceding numbers (e.g., 0, 1, 1, 2, 3, 5, 8, ...). Prompt the 
user to enter the number of terms (n) they want in the sequence and then display the 
Fibonacci sequence up to that number of terms.'''

# user input
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

a, b = 0, 1

fibonacci_sequence = [a, b]
for _ in range(2, n):
    a, b = b, a + b
    fibonacci_sequence.append(b)

print("Fibonacci sequence up to", n, "terms:")
print(fibonacci_sequence)

# Example Output
'''
Enter the number of terms for the Fibonacci sequence: 5
Fibonacci sequence up to 5 terms:
[0, 1, 1, 2, 3]

Enter the number of terms for the Fibonacci sequence: 2
Fibonacci sequence up to 2 terms:
[0, 1]
'''

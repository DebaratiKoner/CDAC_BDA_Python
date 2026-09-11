"""
### Exercise 2: Reversed Uppercased String

Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"EROLAGNAB"`
"""

def reverse():
    word = input("Enter the string: ")
    w1=word[::-1].upper()
    print(f"the output:{w1}")

reverse()
"""
### Exercise 5: Custom Title Case Formatter

Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). **Do not use Python's built-in `.title()` method.**

- **Sample Input**: `"WELCOME TO BANGALORE CITY"`
- **Sample Output**: `"Welcome To Bangalore City"`

"""
def title():
    text=input("Enter a string:")
    text=text.lower()
    word=text.split()
    result=[]
    for title in word:
        title_word=title[0].upper()+title[1:]
        result.append(title_word)
    result=" ".join(result)
    print(f"Output:{result}")
title()
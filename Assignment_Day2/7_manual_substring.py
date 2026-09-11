"""
### Exercise 7: Manual Substring Counter

Write a program that prompts the user to enter a main text string and a substring. Count how many times the substring appears in the main string **without using Python's built-in `.count()` method**.

- **Sample Input**: (User inputs main string `"banana"` and substring `"an"`)
- **Sample Output**: `2`
"""
def substring():
    text = input("Enter main string: ")
    sub = input("Enter substring: ")
    count = 0
    for i in range(len(text)):
        if text[i:i + len(sub)] == sub:
            count += 1
    print(count)
substring()
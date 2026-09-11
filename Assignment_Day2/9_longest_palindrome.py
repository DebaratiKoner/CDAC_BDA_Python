"""
### Exercise 9: Longest Palindromic Substring

Write a program that prompts the user to enter a text string and finds the longest substring within it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, print any one of them.

- **Sample Input**: `"babad"`
- **Sample Output**: `"bab"` (or `"aba"`)
- **Sample Input**: `"cbbd"`
- **Sample Output**: `"bb"`
"""
text = input("Enter text: ")

longest = ""

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):

        word = text[i:j]

        if word == word[::-1]:
            if len(word) > len(longest):
                longest = word

print(longest)
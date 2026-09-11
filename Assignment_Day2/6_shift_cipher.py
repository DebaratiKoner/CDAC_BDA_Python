"""
### Exercise 6: Shift Cipher Encrypter

Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the string by the specified shift number down the alphabet. Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

- **Sample Input**: (User inputs string `"Vinod"` and shift `3`)
- **Sample Output**: `"Ylqrg"`

"""
def cipher():
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    result = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in text:
        if ch in lower:
            position = lower.index(ch)
            new_position = (position + shift) % 26
            result = result + lower[new_position]
        elif ch in upper:
            position = upper.index(ch)
            new_position = (position + shift) % 26
            result = result + upper[new_position]
        else:
            result = result + ch
    print(result)
cipher()
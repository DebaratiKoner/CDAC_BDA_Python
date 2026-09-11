"""
### Exercise 10: Run-Length String Compression

Write a program that prompts the user to enter a text string and compresses it using run-length encoding (listing character counts next to each repeated character). If the compressed string is not smaller in size than the original string, print the original string.

- **Sample Input**: `"aabcccccaaa"`
- **Sample Output**: `"a2b1c5a3"`
- **Sample Input**: `"abcd"`
- **Sample Output**: `"abcd"` (since `"a1b1c1d1"` is longer than `"abcd"`)
"""
def compress():
    text = input("Enter text: ")

    compressed = ""
    count = 1

    for i in range(len(text)):

        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1

        else:
            compressed = compressed + text[i] + str(count)
            count = 1

    if len(compressed) < len(text):
        print(compressed)
    else:
        print(text)
compress()
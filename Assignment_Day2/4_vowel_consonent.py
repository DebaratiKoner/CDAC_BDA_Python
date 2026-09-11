"""
### Exercise 4: Vowel & Consonant Frequency

Write a program that prompts the user to enter a string and counts:

1. The individual frequency of each vowel (`a`, `e`, `i`, `o`, `u`), case-insensitively.
2. The total count of all consonants.

- **Sample Input**: `"Vinod Kumar Kayartaya"`
- **Sample Output**:
  ```text
  Vowel Frequencies:
  a: 4
  e: 0
  i: 1
  o: 1
  u: 1
  Total Consonants: 12
"""

def frequency():
    word=input("Enter a string:")
    word=word.lower()
    a=e=i=o=u=0
    c=0
    for ch in word:
        if ch=='a':
            a+=1
        elif ch=='e':
            e+=1
        elif ch=='i':
            i+=1
        elif ch=='o':
            o+=1
        elif ch=='u':
            u+=1
        elif ch.isalpha(): # it checks if the character is an alphabet and not a vowel, then it is a consonant
            c+=1
    print(f"Vowel Frequencies:\n a:{a}\n e:{e}\n i:{i}\n o:{o}\n u:{u}\n Total Consonants:{c}")

frequency()
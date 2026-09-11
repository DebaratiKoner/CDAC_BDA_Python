"""
### Exercise 1: Sentence Analysis (Character & Word Count)

Write a Python program that prompts the user to enter a sentence. The program must count and display:

1. The total number of characters (including spaces and punctuation).
2. The total number of words.

- **Sample Input**: `"Learning Python is fun!"`
- **Sample Output**:
  ```text
  Total Characters: 23
  Total Words: 4
  ```
  """

def sentence():
  word=input("Enter a sentence:") 
  char_count= len(word)
  word_count= len(word.split())
  print(f"Total characters:{char_count}")
  print(f"Total words:{word_count}")
sentence()
"""
### Exercise 5: The Spy's Word Reverser
**Scenario**: A secret agent wants to send an encrypted message. The encryption rule is simple: **reverse every word in the sentence, but keep the order of words unchanged**. Write a program that prompts the user for a sentence, splits it, uses a list comprehension to reverse the letters of each word, and joins them back together.
* **Sample Input**: `"Meet me at midnight"`
* **Sample Output**: `"teeM em ta thgindim"`
"""
def reverse():
  spy_word = input("Enter the string: ").split()
  result=[]
  for word in spy_word:
    result.append(word[::-1])
  result=" ".join(result)
  print(f"Result:{result}")
reverse()
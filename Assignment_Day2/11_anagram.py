"""
### Exercise 11: Group Anagrams

Write a program that starts with a list of strings defined at the top of your script (e.g., `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`) and groups the anagrams (words formed by rearranging letters) together. Print the final grouped list of lists.

- **Hardcoded Input**: `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Sample Output**: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`
"""
def anagram():
    words =input("Enter the words: ").split()

    groups = []

    for word in words:
        found = False

        for group in groups:
            if sorted(word) == sorted(group[0]):
                group.append(word)
                found = True
                break

        if found == False:
            groups.append([word])

    print(groups)
anagram()
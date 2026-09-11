"""
### Exercise 2: Movie Night Playlist
**Scenario**: You are organizing a movie marathon. You start with a playlist: `["Inception", "The Matrix", "Interstellar"]`. Prompt the user to enter the name of a movie they want to add.
* If the movie is already in the list, print `"Already added!"` and do not insert it.
* If it is not in the list, append it to the end of the list.
Finally, sort the movie list alphabetically and print the updated playlist.
* **Sample Input**: `"Interstellar"`
* **Sample Output**:
  ```text
  Already added!
  Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
  ```
* **Sample Input**: `"Avatar"`
* **Sample Output**:
  ```text
  Added Avatar!
  Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']
  ```
"""

def movie():
    str=input("Enter the string:").split()
    str1=input("Enter the item:")
    if str1 in str:
        print("Already added")
    else:
        str.append(str1)
        str.sort()
        print(f"Added {str1}")
        print(f"List:{str}")
movie()
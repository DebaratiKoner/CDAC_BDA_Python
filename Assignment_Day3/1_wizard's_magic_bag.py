"""
## Part A: Easy Complexity (3 Exercises)

### Exercise 1: The Wizard's Magic Bag
**Scenario**: A wizard has a magic bag containing a sequence of items: `["staff", "potion", "spellbook"]`. When the wizard steps through a magic portal, two things happen:
1. A new item enters the bag (prompts the user to input the item name to append to the end).
2. The oldest item in the bag (at index 0) is dissolved and ejected.
Write a program to simulate this portal transition and print the final bag contents.
* **Sample Input**: (User inputs `"amulet"`)
* **Sample Output**:
  ```text
  Portal transition activated!
  Ejected oldest item: staff
  Current items in the magic bag: ['potion', 'spellbook', 'amulet']

Enter the string: staff potion spellbook
Enter new item:amulet                
Removed item:staff
New list:['potion', 'spellbook', 'amulet']

"""

def magic():
    str = input("Enter the string: ")
    str=str.split()
    item=input("Enter new item:")
    str.append(item)
    delete_item=str.pop(0)
    print(f"Removed item:{delete_item}")
    print(f"New list:{str}")
magic()
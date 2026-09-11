"""
### Exercise 3: The Cargo Train Scanner
**Scenario**: A train has wagons carrying different resources: `["coal", "iron", "gold", "coal", "timber", "coal"]`. The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type (e.g., `"coal"` or `"gold"`).
* Print the total number of wagons carrying that resource (using `.count()`).
* If the resource is on the train, print the index of the very first wagon carrying it (using `.index()`). If it is not found, print `"Resource not found on train!"`.
* **Sample Input**: `"coal"`
* **Sample Output**:
  ```text
  Number of coal wagons: 3
  First coal wagon is at index: 0
  ```
* **Sample Input**: `"oil"`
* **Sample Output**: `"Resource not found on train!"`

"""
def cargo():
    wagons = input("Enter the wagons: ").split()
    w1 = input("Enter the item: " )
    item = wagons.count(w1)
    if w1 in wagons:
        w2=wagons.index(w1)
        print(f"No. of wagons: {item}")
        print(f"First index:{w2}") 
    else:
        print("Resource not found on train!")
cargo()
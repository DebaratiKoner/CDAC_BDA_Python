"""
### Exercise 4: Odd or Even Checker
Write a program that prompts the user for an integer and prints whether it is even or odd.
* **Sample Input**: `7`
* **Sample Output**: `7 is an Odd number.`


"""
def odd_even():
    n=int(input("Enter a number :"))
    if n %2 == 0:
        print(f"{n} is an Even number.")
    else:
        print(f"{n} is an Odd number.")
odd_even()
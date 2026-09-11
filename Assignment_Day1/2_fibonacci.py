"""
### Exercise 2: Fibonacci Sequence Generator
Write a Python script to print the first $N$ terms of the Fibonacci sequence, where N is provided by the user.
* **Fibonacci sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
* **Sample Input**: `N = 6`
* **Sample Output**: `0, 1, 1, 2, 3, 5`

"""
def fibonacci():
    n=int(input("Enter the number of terms :"))
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci()
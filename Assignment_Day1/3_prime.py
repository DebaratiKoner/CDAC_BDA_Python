"""
### Exercise 3: Prime Number Checker
Write a program that checks whether a positive integer entered by the user is a prime number.
* **Logic**: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
* **Sample Input**: `17`
* **Sample Output**: `17 is a prime number.`

"""
def prime():
    n = int(input("Enter a number: "))
    if n<=1:
        print(f"{n} is not a prime number.")
    else:
        for i in range(2,n):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
prime()
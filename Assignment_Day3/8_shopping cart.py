"""
### Exercise 8: De-duplicating Shopping Cart
**Scenario**: An online shopping cart has duplicate items due to double-clicks: `["apple", "banana", "apple", "orange", "banana", "banana"]`. Write a program that processes the list and removes all duplicate items, **but keeps the first occurrence of each item in its original order**. Print the cleaned cart.
* **Hardcoded Input**: `cart = ["apple", "banana", "apple", "orange", "banana", "banana"]`
* **Sample Output**: `['apple', 'banana', 'orange']`

"""
def duplicate():
    items = input("Enter the items: ").split()
    cart=[]
    for i in items:
        if i not in cart:
            cart.append(i)
    print(f"Cart: {cart}")
duplicate()
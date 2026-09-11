"""
### Assignment 4: Atomic E-Commerce Order Processor
#### Scenario
You are building an ordering subsystem for an online store. Orders containing multiple products must be processed **atomically**: either the entire order completes successfully, or the entire transaction fails. If one item in the order is out of stock or is unrecognized, no stock should be deducted for any other item (rollback).

#### Problem Description
1. Define two custom exceptions:
   - `ProductNotFoundError` (raised when a product ID is not present in the catalog).
   - `OutOfStockError` (raised when the customer's ordered quantity exceeds the available stock).
2. Write a function `process_order(catalog, order)`:
   - `catalog` is a dictionary containing product database records. Format:
     ```python
     catalog = {
         "P01": {"price": 100.0, "stock": 5},
         "P02": {"price": 50.0, "stock": 2}
     }
     ```
   - `order` is a dictionary containing product IDs (keys) and quantities ordered (values). Format: `{"P01": 2, "P02": 1}`.
   - **Validation Phase**: Before modifying any inventory levels:
     - Check if all ordered keys exist in the catalog. If a product ID does not exist, raise `ProductNotFoundError` with message: `"Product '<product_id>' not found in store catalog."`
     - Check if the catalog contains sufficient stock for each item ordered. If the ordered quantity exceeds available stock, raise `OutOfStockError` with message: `"Product '<product_id>' is out of stock. Requested: <requested_qty>, Available: <available_stock>."`
   - **Execution Phase**: If (and only if) all products pass validation:
     - Deduct the ordered quantities from the stock numbers in the catalog dictionary.
     - Calculate and return the total cost of the order (float).
     - If an exception was raised during validation, the catalog must remain completely unchanged.

#### Example Walkthrough
```python
catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}

# 1. Successful Order
total = process_order(catalog, {"P01": 2, "P02": 1})
# Returns: 40.0
# Catalog stock changes to: P01 stock = 3, P02 stock = 9

# 2. Failed Order (Triggers Rollback)
# Current Catalog: {"P01": {"price": 10.0, "stock": 3}, "P02": {"price": 20.0, "stock": 9}}
try:
    total = process_order(catalog, {"P01": 2, "P02": 15})
except OutOfStockError as e:
    print(e) # Output: Product 'P02' is out of stock. Requested: 15, Available: 9.

# Verify Catalog Stock: P01 must remain at 3 (NOT decreased to 1).
print(catalog["P01"]["stock"]) # Output: 3
```

---

"""

class ProductNotFoundError(Exception):
    pass
class OutOfStockError(Exception):
    pass
def process_order(catalog, order):
    total = 0.0
    for productId , quantity in order.items():
        if productId not in catalog:
            raise ProductNotFoundError(f"Product {productId} not found in store catalog.")
        available_Stock = catalog[productId]["stock"] 
        if quantity > available_Stock:
            raise OutOfStockError(f"Product {productId} is out of stock."
                                  f"Requested: {quantity},Available: {available_Stock}.")
         # Calculate total price
        price = catalog[productId]["price"]
        total += price * quantity

    # Phase 2: Execution
    # Deduct stock only after ALL products pass validation
    for productId, quantity in order.items():
        catalog[productId]["stock"] -= quantity

    return total


# -----------------------------
# Main Program
# -----------------------------

catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}

order = {
    "P01": 2,
    "P02": 1
}

try:
    total = process_order(catalog, order)
    print("Order successful!")
    print("Total cost:", total)

except ProductNotFoundError as e:
    print("Error:", e)

except OutOfStockError as e:
    print("Error:", e)

print("Updated catalog:", catalog)



    
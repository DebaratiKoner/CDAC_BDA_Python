"""
### Exercise 10: Snake Game Board Renderer
**Scenario**: Render a simple 2D text game board. Write a program that performs the following steps in sequence:
1. Creates a $5 \times 5$ grid filled with dots `"."` represented as a nested list.
2. Places a food item `"F"` at grid position `[2, 3]`.
3. Prompts the user to enter coordinate inputs: a `row` and a `col` (integers between 0 and 4) for the snake's head.
4. Places the snake's head `"S"` at the user-supplied coordinate `[row, col]`, overwriting the character at that position.
5. If the user-supplied coordinates are exactly `[2, 3]`, print the message `"Yum! The snake ate the food!"` (the snake `"S"` will occupy index `[2, 3]` on the printed board, overwriting the `"F"`).
6. Prints the grid neatly line-by-line (each row's elements separated by spaces).

* **Sample Input**: (User inputs Row `0` and Column `3`)
* **Sample Output**:
  ```text
  . . . S .
  . . . . .
  . . . F .
  . . . . .
  . . . . .
  ```
* **Sample Input**: (User inputs Row `2` and Column `3`)
* **Sample Output**:
  ```text
  . . . . .
  . . . . .
  . . . S .
  . . . . .
  . . . . .
  Yum! The snake ate the food!
  ```

"""
def game():
  grid=[]
  for i in range(5):
    row=[]
    for j in range(5):
      row.append(".")
    grid.append(row)
  grid[2][3]="F"
  row=int(input("Enter the row:"))
  col=int(input("Enter the column:"))
  grid[row][col]="S"
  if row==2 and col==3:
    print("Yum! The snake ate the food")
  for row in grid:
    for item in row:
      print(item,end=" ")
    print()

game()
"""
### Exercise 6: Grading on a Curve
**Scenario**: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated test scores. Convert them to a list of integers. Using a **single list comprehension with conditionals**, apply the following curve rules:
* If a score is below `50`, add `10` points.
* If a score is `50` or higher, add `5` points.
* The maximum possible score is capped at `100` (e.g., a score of `98` becomes `100`, not `103`).
Print the original and the curved grades.
* **Sample Input**: `"45 88 30 98 50"`
* **Sample Output**:
  ```text
  Original: [45, 88, 30, 98, 50]
  Curved: [55, 93, 40, 100, 55]
  ```
"""
def grade():
  score = list(map(int,input("Enter the number: ").split()))
  r1=[]
  for marks in score:
    if marks>=50:
      result=marks+5
    else:
      result=marks+10
    if result>100:
      result = 100
    r1.append(result)
  print(f"original score: {score}")
  print(f"result : {r1}")
grade()
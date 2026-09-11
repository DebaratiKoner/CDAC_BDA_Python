"""
### Exercise 8: Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:
* 90-100: A
* 80-89: B
* 70-79: C
* 60-69: D
* Below 60: F

"""
def grade():
    score = int(input("Enter the test score: "))
    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print("Grade: B")
    elif 70 <= score < 80:
        print("Grade: C")
    elif 60 <= score < 70:
        print("Grade: D")
    elif 0 <= score < 60:
        print("Grade: F")
    else:
        print("Error: Score must be between 0 and 100.")
grade()
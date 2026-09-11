"""
### Assignment 1: Structured CSV & JSON Data Processor
#### Scenario
An academic registrar stores student course registrations in a CSV file. You need to read this file, compute overall statistics, and export a summarized JSON report.

#### Problem Description
1. Create a function `process_student_records(input_csv_path, output_json_path)`:
   - Reads an `input_csv_path` containing columns: `student_id`, `name`, `course`, `score`.
   - Uses `csv.DictReader` inside a context manager to parse all rows.
   - Computes:
     - `total_students`: Total number of students processed.
     - `average_score`: Arithmetic mean of all student scores (rounded to 2 decimal places).
     - `top_scorer`: The dictionary `{"name": <name>, "score": <score>}` of the highest scoring student.
     - `course_counts`: A dictionary mapping each course name to the count of enrolled students.
   - Writes the summary dictionary into `output_json_path` formatted with an indentation of 4 spaces using `json.dump()`.

#### Example Walkthrough
```python
# Given input CSV:
# student_id,name,course,score
# 101,Arham,AI,88.5
# 102,Lisa,BDA,94.0
# 103,Vinod,AI,96.5

process_student_records("students.csv", "summary.json")

# Expected summary.json output:
# {
#     "total_students": 3,
#     "average_score": 93.0,
#     "top_scorer": {
#         "name": "Vinod",
#         "score": 96.5
#     },
#     "course_counts": {
#         "AI": 2,
#         "BDA": 1
#     }
# }
```

---
"""
import csv
import json

students=[
    {"student_id":101,"name":"Arham","course":"AI","score":88.5},
    {"student_id":102,"name":"Lisa","course":"BDA","score":94.0},
    {"student_id":103,"name":"Vinod","course":"AI","score":96.5}
]

with open("students.csv","w",newline="") as file:
    writer=csv.DictWriter(file,fieldnames=["student_id","name","course","score"])
    writer.writeheader()
    writer.writerows(students)

def process_student_records(input_csv_path,output_json_path):
    with open(input_csv_path,"r") as file:
        reader=csv.DictReader(file)
        records=list(reader)

    total_students=len(records)

    scores=[float(row["score"]) for row in records]
    average_score=round(sum(scores)/total_students,2)

    top=max(records,key=lambda row:float(row["score"]))

    top_scorer={
        "name":top["name"],
        "score":float(top["score"])
    }

    course_counts={}

    for row in records:
        course=row["course"]

        if course in course_counts:
            course_counts[course]+=1
        else:
            course_counts[course]=1

    summary={
        "total_students":total_students,
        "average_score":average_score,
        "top_scorer":top_scorer,
        "course_counts":course_counts
    }

    with open(output_json_path,"w") as file:
        json.dump(summary,file,indent=4)

process_student_records("students.csv","summary.json")
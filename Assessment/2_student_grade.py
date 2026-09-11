import json

students = [
{"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
{"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"}
]

id_counter=len(students)

def menu():
    menu_items='''
    [1] Enroll Student 
    [2] Cohort Directory
    [3] Query Records 
    [4] Revise Evaluation 
    [5] Purge Record
    [6] Save to JSON
    [7] Load from JSON
    [8] Terminate
'''
    print("Student Grade Management System")
    print(menu_items)
    try:
        choice=int(input("Enter the choice:"))
    except:
        choice=-1

    return choice

def calculate_grade(marks):
    if marks>=85:
        return 'A'
    elif marks>=70:
        return 'B'
    elif marks >=50:
        return 'C'
    else:
        return 'F'
    
def enroll_students():
    global id_counter
    try:
        name=input("Enter the name:").strip()
        if name=="":
            print("Name string must not be blank")
            return
        course=input("Enter the course:").strip()
        if course=="":
            print("Course string must not be blank")
            return
        marks=float(input("Enter the marks:"))
        if not 0<=marks<=100:
            print("Enter valid marks.")
            return
        students.append(dict(id=id_counter+1,name=name,course=course,marks=marks,grade=calculate_grade(marks)))
        id_counter+=1
        print("Students enrolled successfully.")
    except:
        print("Please enter valid input.")

def print_one_student(s):
    id,name,course,marks,grade=s.values()
    print("Student Details")
    print(f"ID:{id}")
    print(f"Name:{name}")
    print(f"Course:{course}")
    print(f"Marks:{marks}")
    print(f"Grade:{grade}")
    print("-"*60)

def print_many_student(students):    
    print("-"*60)
    print(f"{'ID':^5}{'Name':<20}{'Course':<20}{'Marks':<10}{'Grade':<5}")

    print("-"*60)
    for s in students:
        id,name,course,marks,grade=s.values()
        print(f"{id:^5}{name:<20}{course:<20}{marks:<10}{grade:<5}")
    print("-"*60)

def cohort_directory():
    if len(students)==0:
        print("No student record found")
    elif len(students)==1:
        print_one_student(students[0])
    else:
        print_many_student(students)

def search_by_id(id):
    result=[]
    for s in students:
        if s['id']==id:
            result.append(s)
    if not result:
        print(f"No product found for id {id}")
        return None
    print_one_student(result[0])
    return result[0]

def search_by_name():
    result=[]
    name=input("Enter the name:")
    for s in students:
        if s['name']==name:
            result.append(s)
    if not result:
        print(f"No product found for name {name}")
        return None
    if len(result)==1:    
        print_one_student(result[0])
    else:
        print_many_student(result)

def search_by_course():
    result=[]
    course=input("Enter the course:")
    for s in students:
        if s['course']==course:
            result.append(s)
    if not result:
        print(f"No product found for course {course}")
        return None
    if len(result)==1:    
        print_one_student(result[0])
    else:
        print_many_student(result)

def query_records():
    try:
        print("1.Search by id")
        print("2.Search by name")
        print("3.Search by course")
        choice=int(input("Enter the choice:"))
        if choice==1:
            id=int(input("Enter the id:"))
            search_by_id(id)
        elif choice==2:
            search_by_name()
        elif choice==3:
            search_by_course()
        else:
            print("Student not found")
    except:
        print("Please provide valid input.")

def revise_evaluation():
    try:
        id=int(input("Enter the id:"))
        student=search_by_id(id)
        if student is None:
            return
        print("1.Update name.")
        print("2.Update course.")
        print("3.Update marks.")
        choice=int(input("Enter the choice:"))
        if choice==1:
            name=input("Enter the name:").strip()
            if name!="":
                student["name"]=name
        elif choice==2:
            course=input("Enter the course:").strip()
            if course!="":
                student["course"]=course
        elif choice==3:
            marks=float(input("Enter the marks:"))
            if  0<=marks<=100:
                student["marks"]=marks
                student["grade"]=calculate_grade(marks)
        else: 
            print("Invalid choice.")
            return
        print("Student updated successfully")
        print_one_student(student)
    except:
        print("Please enter valid input.")

def purge_record():
    try:
        id=int(input("Enter the id:"))
        s=search_by_id(id)
        if s is None:
            return
        ans=input("Do you want to delete it(y/n)")
        if ans=='y':
            students.remove(s)
            print("Product deleted successfully")
    except:
        print("Give valid values")
        
def save_to_json():
    try:
        with open ("students.json","w") as file:
            json.dump(students,file,indent=4)
        print("Data saved Successfully")
    except:
        print("File error")

def load_from_json():
    try:
        with open("students.json","r")as file:
            students=json.load(file)
            print(students)
    except:
        print("Invalid file")
     
def main():
    while True:
        choice=menu()
        match choice:
            case 1:
                enroll_students()
            case 2:
                cohort_directory()
            case 3:
                query_records()
            case 4:
                revise_evaluation()
            case 5:
                purge_record()
            case 6:
                save_to_json()
            case 7:
                load_from_json()
            case 8:
                break
            case _ :
                print("Invalid choice")
if __name__=='__main__':
    main()
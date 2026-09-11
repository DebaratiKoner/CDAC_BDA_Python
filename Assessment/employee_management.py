import csv

employees = [
    {"id": 1, "name": "Rahul", "department": "IT", "salary": 55000},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000}
]

id_counter=len(employees)

def menu():
    menu_items='''
    1.Add Employee
    2.View Employee
    3.Search Employee
    4.Update Employee
    5.Delete Employee
    6.Save to CSV
    7.Load from CSV
    8.Exit
    '''
    print("--------Employee Management System---------")
    print(menu_items)
    try:
        choice=int(input("Enter the choice:"))
    except:
        choice=-1
    return choice

def add_employee():
    global id_counter
    try:
        name=input("Enter the name:").strip()
        if name=="":
            print("Name cannot be empty.")
            return
        department=input("Enter the department:").strip()
        if department=="":
            print("Department cannot be empty.")
            return
        salary=float(input("Enter the salary:"))
        if salary<=0:
            print("Salary must be > 0.")
            return
        employees.append(dict(id=id_counter+1,name=name,department=department,salary=salary))
        id_counter+=1
                         
        print("Employee Management is added.")
    except:
        print("Enter valid value.")

def print_one_employee(e):
    id,name,department,salary=e.values()
    print("Employee Details")
    print(f"ID:{id}")
    print(f"Name:{name}")
    print(f"Department:{department}")
    print(f"Salary:{salary}")
    print("-"*70)

def print_many_employee(employees):
    print("-"*70)
    print(f"{'ID':^5}{'Name':<20}{'Department':<20}{'Salary':>10}")
    print("-"*70)
    for e in employees:
        id,name,department,salary=e.values()
        print(f"{id:^5}{name:<20}{department:<20}{salary:>10}")
    print("-"*70)

def view_employee():
    if len(employees)==0:
        print("No employees are found.")
    elif len(employees)==1:
        print_one_employee(employees[0])
    else:
        print_many_employee(employees)

def search_by_id(id):
    result=[]
    for e in employees:
        if e['id']==id:
            result.append(e)
    if not result:
        print(f"No employee found with id {id}")
        return None
    print_one_employee(result[0])
    return result[0]

def search_by_name():
    result=[]
    name=input("Enter the name:")
    for e in employees:
        if e['name']==name:
            result.append(e)
    if not result:
        print(f"No employee found with name {name}")
        return None
    if len(result)==1:
        print_one_employee(result[0])
    else:
        print_many_employee(result)
    
def search_employee():
    try:
        print("1.Search by Id:")
        print("2.Search by Name:")
        choice=int(input("Enter the choice:"))
        if choice==1:
            id=int(input("Enter the id:"))
            search_by_id(id)
        elif choice==2:
            search_by_name()
        else:
            print("Invalid Choice.")
    except:
        print("Enter a valid value.")

def update_employee():
    try:
        id=int(input("Enter the id:"))
        employee=search_by_id(id)
        if employee is None:
            return
        print("1.Update name")
        print("2.Update department")
        print("3.Update salary")
        choice=int(input("Enter the choice:"))
        if choice==1:
            name=input("Enter the name:").strip()
            if name !="":
                employee['name']=name
        elif choice==2:
            department=input("Enter the department").strip()
            if department!="":
                employee['department']=department
        elif choice==3:
            salary=float(input("Enter the salary:"))
            if salary>0:
                employee['salary']=salary
        else:
            print("Invalid choice")
            return
        print("Employee updated")
        print_one_employee(employee)
    except:
        print('Enter a valid value')

def delete_employee():
    try:
        id=int(input("Enter the id:"))
        employee=search_by_id(id)
        if employee is None:
            return
        ans=input("Do u want to delete(y/n):")
        if ans=='y':
            employees.remove(employee)
            print("Product deleted")
    except:
        print("Enter valid value")
def save_to_csv():
    try:
        with open("employees.csv","w")as file:
            fieldnames=['id','name','department','salary']
            writer=csv.DictWriter(file,fieldnames=fieldnames,lineterminator="\n")
            writer.writeheader()
            for e in employees:
                writer.writerow(e)
        print("Data saved successfully")
    except:
        print("Enter valid value")

def load_from_csv():
    global employees
    global id_counter
    try:
        with open("employees.csv","r")as file:
            reader=csv.DictReader(file)
            employees=[]
            for data in reader:
                employees.append({
                    'id':int(data['id']),
                    'name':data['name'],
                    'department':data['department'],
                    'salary':float(data['salary'])
                })
        if employees:
            id_counter=max(employee['id']for employee in employees)+1
        else:
            id_counter=1
        print(employees)
        print("Data loaded successfully")    
    except:
        print("Enter valid value")

def main():
    while True:
        choice=menu()
        match choice:
            case 1:
                add_employee()
            case 2:
                view_employee()
            case 3:
                search_employee()
            case 4:
                update_employee()
            case 5:
                delete_employee()
            case 6:
                save_to_csv()
            case 7:
                load_from_csv()
            case 8:
                break
            case _:
                print("Invalid Choice.")
if __name__=='__main__':
    main()
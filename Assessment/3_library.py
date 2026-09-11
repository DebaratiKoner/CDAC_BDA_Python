import json
import csv
books=[{"id":1,"book_title":"Python Programming","author_name":"John Zelle","Genre":"Technical","price":650,"copies":15},
         {"id":2,"book_title":"Clean Code","author_name":"Robert Martin","Genre":"Technical","price":950,"copies":8},
         {"id":3,"book_title":"The Great Gatsby","author_name":"F. Scott Fitzgerald","Genre":"Fiction","price":350,"copies":20},
         {"id":4,"book_title":"Sapiens","author_name":"Yuval Noah Harari","Genre":"History","price":550,"copies":12},
         {"id":5,"book_title":"Cosmos","author_name":"Carl Sagan","Genre":"Science","price":480,"copies":6}
     ]
id_counter=len(books)

def menu():

    
    menu_items='''
    1. Add Book
    2. View Catalog
    3. Search Books
    4. Update Details
    5. Delete Book
    6. Save to File
    7. Load from File
    8. Exit
    '''
    print("FILE CATALOG MANAGEMENT SYSTEM")
    print(menu_items)
    try:
        choice=int(input("Enter the choice:"))    
    except:
        choice=-1
    return choice

def add_books():
    global id_counter
    try:
        book_title=input("Enter the title:").strip()
        if book_title =="":
            print("String must not be empty")
            return
        author_name=input("Enter the author name:").strip()
        if author_name =="":
            print("String must not be empty")
            return
        genre=input("Enter the genre:").strip()
        if genre =="":
            print("String must not be empty")
            return
        price=float(input("Enter the price:"))
        if price <=0:
            print("Price must be >0")
            return
        copies=int(input("Enter the copies:"))
        if copies <0:
            print("Copies must be >=0")
            return
        books.append(dict(id=id_counter,book_title=book_title,author_name=author_name,genre=genre,price=price,copies=copies))
        id_counter+=1
        print("Books Added Successfully.")
    except ValueError:
        print("Enter valid input.")

def print_one_book(book):
    id,book_title,author_name,genre,price,copies=book.values()
    print("Book Details")
    print(f"ID:{id}")
    print(f"Book Title:{book_title}")
    print(f"Author Name:{author_name}")
    print(f"Genre:{genre}")
    print(f"Price:{price}")
    print(f"Copies:{copies}")
    print("-"*90)

def print_many_book(book_list):
    print("-"*90)
    print(f"{'ID':^5}{'Book Title':<20}{'Author Name':<20}{'Genre':<20}{'Price':>10}{'Çopies':>10}")
    print("-"*90)
    for book in book_list:
        id,book_title,author_name,genre,price,copies=book.values()
        print(f"{id:^5}{book_title:<20}{author_name:<20}{genre:<20}{price:>10}{copies:>10}")
        print("-"*90)

def view_catalog():
    if len(books)==0:
        print("No books found")
    elif len(books)==1:
        print_one_book(books[0])
    else:
        print_many_book(books)

def search_by_id(id):
    result=[]
    for b in books:
        if b['id']==id:
            result.append(b)
    if not result:
        print(f"No product found for id {id}") 
        return
    print_one_book(result[0])
    return result[0]

def search_by_title():
    result=[]
    title=input("Enter the title:")
    for b in books:
        if b['book_title']==title:
            result.append(b)
    if not result:
        print(f"No product found for title {title}") 
        return
    if len(result)==1:
        print_one_book(result[0])
    else:
        print_many_book(result)

def search_by_author():
    result=[]
    name=input("Enter the name:")
    for b in books:
        if b['author_name']==name:
            result.append(b)
    if not result:
        print(f"No product found for name {name}") 
        return
    if len(result)==1:
        print_one_book(result[0])
    else:
        print_many_book(result)

def search_books():
    try:
        print("1.Search by ID")
        print("2.Search by Book Title")
        print("3.Search by Author Name")
        choice=int(input("Enter the choice:"))
        if choice==1:
            id=int(input("Enter the id:"))
            search_by_id(id)
        elif choice ==2:
            search_by_title()
        elif choice==3:
            search_by_author()
        else:
            print("Invalid Choice.")
    except:
        print("Enter valid books.")
def update_details():
    try:
        id=int(input("Enter the id:"))
        books=search_by_id(id)
        if books is None:
            return
        print("1.Update price.")
        print("2.Update copies.")
        choice=int(input("Enter the choice:"))
        if choice==1:
            price=float(input("Enter the price:"))
            if price >0:
                books["price"]=price
        elif choice==2:
            copies=int(input("Enter the copies:"))
            if copies >=0:
                books["copies"]=copies
        else: 
            print("Invalid choice.")
            return
        print("Books updated successfully")
        print_one_book(books)
    except:
        print("Please enter valid input.")
    
def delete_books():
    try:
        id=int(input("Enter the id:"))
        s=search_by_id(id)
        if s is None:
            return
        ans=input("Do you want to delete it(y/n)")
        if ans=='y':
            books.remove(s)
            print("Book deleted successfully")
    except:
        print("Give valid values")
"""             
def save_to_file():
    try:
        with open("books.txt", "w") as file:

            for book in books:
                file.write(
                    f"{book['id']}|"
                    f"{book['book_title']}|"
                    f"{book['author_name']}|"
                    f"{book['Genre']}|"
                    f"{book['price']:.2f}|"
                    f"{book['copies']}\n"
                )
        print("Books saved successfully.")
    except :
        print("File error.")

def load_from_file():
    global books
    global id_counter
    try:
        with open("books.txt", "r") as file:
            books = []
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                data = line.split("|")
                book = {
                    "id": int(data[0]),
                    "book_title": data[1],
                    "author_name": data[2],
                    "Genre": data[3],
                    "price": float(data[4]),
                    "copies": int(data[5])
                }
                books.append(book)
        if books:
            id_counter = max(book["id"] for book in books) + 1
        else:
            id_counter = 1
        print(books)
        print("Books loaded successfully.")
    except :
        print("File error.")
"""

"""
def save_to_file(): #json
    try:
        with open ("books.json","w") as file:
            json.dump(books,file,indent=4)
        print("Data saved Successfully")
    except:
        print("File error")

def load_from_file(): #json
    try:
        with open("books.json","r")as file:
            books=json.load(file)
            print(books)
    except:
        print("Invalid file")
"""

#"""
def save_to_file():
    try:
        with open("books.csv", "w",newline="") as file:
            fieldnames=['id','book_title','author_name','Genre','price','copies']
            writer = csv.DictWriter(file,fieldnames=fieldnames,lineterminator="\n")
            writer.writeheader()
            for b in books:
                writer.writerow(b)
        print("Data saved successfully.")
    except :
        print("Something went wrong")

def load_from_file():
    global books
    global id_counter
    try:
        with open("books.csv", "r") as file:
            reader = csv.DictReader(file)
            books = []
            for data in reader:
                books.append({
                    "id": int(data["id"]),
                    "book_title": data["book_title"],
                    "author_name": data["author_name"],
                    "Genre": data["Genre"],
                    "price": float(data["price"]),
                    "copies": int(data["copies"])
                })
        if books:
            id_counter=max(book["id"] for book in books)+1
        else:
            id_counter=1
        print(books)
        print("Data loaded successfully.")
    except :
        print("Something went wrong")
#"""     
    
def main():

    while True:
        choice=menu()
        match choice:
            case 1:
                add_books()
            case 2:
                view_catalog()
            case 3:
                search_books()
            case 4:
                update_details()
            case 5:
                delete_books()
            case 6:
                save_to_file()
            case 7:
                load_from_file()
            case 8:
                break
            case _:
                print("Invalid choice")
if __name__=='__main__':
    main()
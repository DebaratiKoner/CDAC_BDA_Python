products = [ 
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, 
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50} 
]
id_counter=len(products)

def menu():
    menu_items="""
    1.Add products.
    2.View all products.
    3.Search products.
    4.Update products.
    5.Delete products.
    6.Exit.
"""
    print("Product Inventory Management System")
    print(menu_items)
    try:
        choice=int(input("Enter the choice:"))
    except:
        choice=-1
    return choice

def add_product():
    global id_counter
    try:
        print("Add the products:")
        name=input("Enter the name:").strip()
        if name=="":
            print("Name cannot be empty")
            return

        category=input("Enter the category:").strip()
        if category =="":
            print("Category cannot be empty")
            return
        price=float(input("Enter the price: "))
        if price <=0:
            print("Price should be greater than zero")
            return
        quantity=int(input("Enter the quantity:"))
        if quantity<0:
            print("Quantity should be >=0")
            return
        products.append(dict(id=id_counter+1,name=name,category=category,price=price,quantity=quantity))
        id_counter+=1
    except:
        print("Please put a valid value.")

def print_one_product(p):
    id,name,category,price,quantity=p.values()
    print("PRODUCT DETAILS")
    print(f"ID:{id}")
    print(f"NAME:{name}")
    print(f"CATEGORY:{category}")
    print(f"PRICE:{price}")
    print(f"QTY:{quantity}")
    print("-"*70)

def print_many_products(product_list):
    print("-"*70)
    print(f"{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}")
    print("-"*70)
    for p in product_list:
        id,name,category,price,quantity=p.values()
        print(f"{id:^5}{name:<20}{category:<20}{price:>10}{quantity:>5}")
    print("-"*70)

def view_product():
    if len(products)==0:
        print("No product found")
    elif len(products)==1:
        print_one_product(products[0])
    else:
        print_many_products(products) 

def search_product():
    try:
        print("1.Search by ID")
        print("2.Search by name")
        choice=int(input("Enter the choice:"))
        if choice==1:
            id=int(input("Enter the ID"))
            search_by_id(id)
        elif choice ==2:
            search_by_name()
        else:
            print("The product not found")
    except:
        print("Enter valid product")

def search_by_id(id):
    result=[]
    for p in products:
        if p['id']==id:
            result.append(p)
    if not result:
        print(f"No product found for id{id}")
        return None
    print_one_product(result[0])
    return result[0]

def search_by_name():
    result=[]
    name=input("Enter the name")
    for p in products:
        if p['name']==name:
            result.append(p)
    if not result:
        print(f"No product found for name{name}")
        return None
    if len(result)==1:
        print_one_product(result[0])
    else:
        print_many_products(result)
    
def update_product():
    try:
        id=int(input("enter the Id"))
        product=search_by_id(id)
        if product is None:
            return
        name=input("Enter the name:").strip()
        if name!="":
            product["name"]=name
        category=input("Enter the category:").strip()
        if category !="":
            product["category"]=category       
        price=float(input("Enter the price: "))
        if price >0:
            product["price"]=price
        quantity=int(input("Enter the quantity:"))
        if quantity >0:
            product["quantity"]=quantity
        print("Product updated succesfully")
        print_one_product(product)
    except:
        print("Enter valid value")

def delete_product():
    try:
        id=int(input("Enter the id:"))
        p=search_by_id(id)
        if p is None:
            return
        ans=input("Do you want to delete it(y/n)")
        if ans=='y':
            products.remove(p)
            print("Product deleted successfully")
    except:
        print("Give valid values")

def main():
    while True:
        choice=menu()
        match choice:
            case 1:
                add_product()
            case 2:
                view_product()
            case 3:
                search_product()
            case 4:
                update_product()
            case 5:
                delete_product()
            case 6:
                break
            case _:
                print("Invalid choice")
            
if __name__=='__main__':
    main()

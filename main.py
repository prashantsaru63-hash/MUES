from models import User , Product 
from database import load_data , save_data

def menu() :

    print("======== Multi-User Ecommerce System =========")
    print("1. Rester")
    print("2. Login")
    print("3. Exit")

def user_menu() :
    print(" ===== Customer Menu ======")    
    print("1. View Product")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Place order")
    print("5. Logout")

def admin_menu() :
    print(" ====== Admin Menu =======")    
    print("1. Add Product")
    print("2. View All Products")
    print("3. View orders ")
    print("4. Logout")


def main() :

    data = load_data()

    while True :

        menu() 

        choice = input("Enter the choice : ")


        ''' Register  '''

        if choice == "1" :

            u = input("Enter the user : ")
            p = input("Enter the Password : ")

            if u in data["users"] :
                print(" User already exists !!! ")

            else : 
                data["users"][u] = {
                    "password" : p,
                    "role" : "customer",
                    "cart" : []
                }   

                save_data(data) 
                print("Register")


        # login  

        elif choice == "2" :
            u = input("Enter the user : ")
            p = input("Enter the password : ")

            if u not in data["users"] or data["users"][u]["password"] != p :
                print("Invalid login")
                continue

            role = data["users"][u]["role"]
            print(f"Welcome {u} {role}")


        # Customer Panel 

            if role == "customer" :

                while True :

                    user_menu()

                    c = input("Enter choices : ")

                # view products 

                    if c == "1" :
                        for pid , prod in data["products"].items():
                            print(pid,prod)


                # Add to cart             

                    elif c == "2":
                        pid = int(input("Enter the product ID : "))

                        if pid in data["products"] :
                            data["users"][u]["cart"].append(pid)
                            save_data(data)


                # View Cart 

                    elif c == "3" :
                     
                        for pid in data["users"][u]["cart"] :
                            print(pid,data["products"][pid])


                # Place order 

                    elif c == "4" :

                        total = 0
                        items = []

                        for pid in data["users"][u]["cart"] :
                            prod = data["products"][pid]
                            total += prod["price"]
                            items.append(prod["name"])

                            prod["stock"] -= 1

                        order = {
                            "user" : u,
                            "items" : items,
                            "total" : total
                        }    

                        data["orders"].append(order) 
                        data["users"][u]["cart"] = []

                        save_data(data)
                        print("Order Placed")

                    elif c == "5" :
                        break    

            if role == "admin" :

                while True :
                    admin_menu()

                    c = input("Enter the choice : ")      

                    # ADD Product 

                    if c == "1" :
                        pid = input("ID : ")
                        name = input("Name : ")
                        price = float(input("Price : ")) 
                        stock = int(input("Stock : "))

                        data["products"][pid] = {
                            "name" : name,
                            "price" : price,
                            "stock" : stock
                        }

                        save_data(data)


                        # view Products

                    elif c == "2" :
                        print(data["products"])   

                        # view 

                    elif c == "3" :

                        for o in data["orders"] :
                            print(o)

                    elif c == "4" :
                        break            



        elif choice == "3" :
            print("User not Found")
            break

        else : 
            print("Invalid choice !!! ")


if __name__ == "__main__" :
    main()
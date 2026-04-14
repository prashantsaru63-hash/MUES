from models import User
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


        elif choice == "3" :
            print("User not Found")
            break

        else : 
            print("Invalid choice !!! ")


if __name__ == "__main__" :
    main()
class User : 
    def __int__(self , user,password , role = "customer"):
        self.user = user
        self.password = password
        self.role = role
        self.cart = []

class Product :

    def __init__(self,pid,name,price,stock):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock        
         
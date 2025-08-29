#Q4. Create a class Product with attributes like name, price, 
# and stock_quantity.Create a class ShoppingCart that allows 
# adding/removing products and calculating total cost.
#Use encapsulation to ensure stock levels are updated correctly when items are added.
#Implement a method checkout() that validates stock and generates a receipt.
#Add a custom exception OutOfStockError.

from abc import ABC, abstractmethod

class OutOfStockError(Exception):
    pass

class Product(ABC):
    def __init__(self, name, price, stock_quantity):
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_stock_quantity(self):
        return self.__stock_quantity
    
    def reduce_stock(self, quantity):
        if quantity > self.__stock_quantity:
            raise  OutOfStockError(f"Not enough stock for {self.__name}. available: {self.__stock_quantity}")
        self.__stock_quantity -= quantity

    def increase_stock(self, quantity):
        self.__stock_quantity += quantity

class ShoppingCart:
    def __init__(self):
        self.cart ={}

    def add_product(self, product, quantity):
        product.reduce_stock(quantity)
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product]

        def remove_product(self, product, quantity):
           if product not in self.cart or self.cart[product] < quantity:
               print("product not in cart or invalid quantity") 
               return
           self.cart[product] -= quantity
           product.increase_stock(quantity)
           if self.cart[product] == 0:
               del self.cart[product]

        def calculate_total(self):
            total = 0
            for product, qty in self.cart.items():
                total += product.get_price() * qty
            return total
        
        def checkout(self):
            if not self.cart:
                print("Cart is empty")
                return
        print("\n--- Receipt ---")
        for product, qty in self.cart.items():
            print(f"{product.get_name()} x{qty} = ${product.get_price() * qty}")
        print(f"Total: ${self.calculate_total()}")
        self.cart.clear()

if __name__ == "__main__":
    products =[]

    n = int(input("Enter number of products: "))
    for _ in range(n):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
        products.append(Product(name, price, stock))

    cart = ShoppingCart()

    while True:
        choice = input("Add product ").lower()
        if choice == "no":
            break
        index = int(input("Enter product index : "))
        qty = int(input("enter quantity: "))
        try:
            cart.add_product(products[index], qty)
        except OutOfStockError as e:
            print(e)

    cart.checkout()



    









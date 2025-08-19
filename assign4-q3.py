# Q3. Develop a Product class with attributes like name, price, and stock quantity. 
#Create a Cart class to manage a list of products a customer wants to buy.
#Implement methods to add, remove, and calculate the total price of items in the cart. 

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class Cart:

    def __init__(self):
        self.items =[]

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product,quantity))
            product.stock -= quantity
            print(f"Added {quantity} * {product.name} to cart.")
        else:
            print(f"Not enough stock {product.name}.")


    def remove_product(self, product_name):
        for item in self.items:
            if item[0].name==product_name:
                product, qty = item
                product.stock += qty
                self.items.remove(item)
                print(f"Remove {qty} * {product_name} from cart.")
                return 
        print(f"{product_name} not fond in cart.")


    def calculate_total(self):
        return sum(product.price * qty for product, qty in self.items )
    
    def show_cart(self):
        if not self.items:
            print("cart is empty.")

        else:
            print("\n Items in cart:")

            for product, qty in self.items:

                print(f"{qty} * {product.name} = ${product.price * qty}")

            print(f"Total: $({self.calculate_total()}")        
        
cart = Cart()

name = input("Enter product name: ")
price = float(input( "Enter product price: "))
stock = int(input("Enter stock quantity: "))

product = Product(name, price, stock)
cart.add_product(product, 1)  # add 1 item
cart.show_cart()


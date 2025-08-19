# Q4. Build a Car class with attributes like make, model, and rental price. 
#Create a Customer class with attributes like name, license number, and rental history. 
#Design a RentalService class to manage car rentals and returns.

class Car:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.rental_price = rental_price
        self.is_rented = False
    def __str__(self):
        status = "Rented" if self.is_rented else "Available"
        return f"{self.make} {self.model} - {self.rental_price}/day ({status})"
    

class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.rental_history=[]

    def __str__(self):
        return f"Customer: {self.name}, License: {self.license_number}"
    

class RentalService:
    def __init__(self):
        self.cars =[]
        self.customers=[]

    def add_car(self, car):
        self.cars.append(car)
        print(f"car added: {car}")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer addes: {customer}")

    def rent_car(self, customer, car_make, car_model):
        for car in self.cars:
            if car.make == car_make and car.model==car_model and not car.is_rented:
                car.is_rented = True
                customer.rental_history.append(car)
                print(f"{customer.name} rented {car.make} {car.model} for ${car.rental_price}/day.")
                return
            print("car not available")


    def return_car(slef, customer, car_make, car_model):
        for car in customer.rental_history:
            if car.make==car_make and car.model==car_model and car.is_rented:
                car.is_rented = False
                print(f"{customer.name} returned {car.make} {car.model}")
                return
        print("Car not found in rentals history")


    def show_available_cars(self):
        print("\nAvailable Cars:")
        available= [car for car in self.cars if not car.is_rented]
        if not available:
            print("No cars available")
        else:
            for car in available:
                print(car)
        
service = RentalService()

while True:
    print("\n--- Car Rental Menu ---")
    print("1. Add Car")
    print("2. Add Customer")
    print("3. Rent Car")
    print("4. Return Car")
    print("5. Show Available Cars")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        price = float(input("Enter rental price per day: "))
        car = Car(make, model, price)
        service.add_car(car)
        print("Car added successfully.")

    elif choice == "2":
        name = input("Enter customer name: ")
        license_number = input("Enter license number: ")
        customer = Customer(name, license_number)
        service.add_customer(customer)
        print("Customer added successfully.")

    elif choice == "3":
        name = input("Enter customer name: ")
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        service.rent_car(name, make, model)

    elif choice == "4":
        name = input("Enter customer name: ")
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        service.return_car(name, make, model)

    elif choice == "5":
        service.show_available_cars()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")


    
    

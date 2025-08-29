#Q2. Create an abstract class Vehicle with an abstract method get_max_speed().
#Implement subclasses: Car, Bike, and Truck, each returning a different speed.
#Store vehicle name and type using encapsulation with validation.
#Create a method print_vehicle_speeds() that demonstrates polymorphism.
#Add a custom exception InvalidSpeedError if speed is negative.

from abc import ABC, abstractmethod

class InvalidSpeedError(Exception):
    pass

class Vehicle(ABC):
    def __init__(self, name, vehicle_type, max_speed):
        self.__name = None
        self.__type = None
        self.__max_speed = None

        self.set_name(name)
        self.set_type(vehicle_type)
        self.set_max_speed(max_speed)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        self.__name = name

    def get_type(self):
        return self.__type

    def set_type(self, vehicle_type):
        if not vehicle_type:
            raise ValueError("Vehicle type cannot be empty.")
        self.__type = vehicle_type

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, speed):
        if speed < 0:
            raise InvalidSpeedError("Speed cannot be negative.")
        self.__max_speed = speed

    @abstractmethod
    def vehicle_info(self):
        pass

class Car(Vehicle):
    def vehicle_info(self):
        return f"Car {self.get_name()} max speed: {self.get_max_speed()} km/h"

class Bike(Vehicle):
    def vehicle_info(self):
        return f"Bike {self.get_name()} max speed: {self.get_max_speed()} km/h"

class Truck(Vehicle):
    def vehicle_info(self):
        return f"Truck {self.get_name()} max speed: {self.get_max_speed()} km/h"

def print_vehicle_speeds(vehicles):
    for vehicle in vehicles:
        print(vehicle.vehicle_info())

vehicles = []
num = int(input("How many vehicles to enter? "))

for i in range(num):
    print(f"\nEnter details for Vehicle {i+1}:")
    name = input("Name: ")
    vehicle_type = input("Type (Car/Bike/Truck): ")
    speed = float(input("Max speed: "))

    if vehicle_type.lower() == "car":
        vehicles.append(Car(name, vehicle_type, speed))
    elif vehicle_type.lower() == "bike":
        vehicles.append(Bike(name, vehicle_type, speed))
    elif vehicle_type.lower() == "truck":
        vehicles.append(Truck(name, vehicle_type, speed))
    else:
        print("Invalid vehicle type. Skipping this entry.")

print("\n--- Vehicle Speeds ---")
print_vehicle_speeds(vehicles)

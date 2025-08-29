#Q1. Create an abstract base class Shape with an abstract method calculate_area().
# Create concrete subclasses Circle, Rectangle, and Triangle that inherit 
# #from Shape and implement the abstract method according to their specific formulas.
#Each shape should properly encapsulate its attributes (radius, width, height, etc.) 
# with appropriate validation.
#Create a ShapeCalculator utility class that can process lists of shapes.
#Demonstrate polymorphism by creating a method
#calculate_total_area() that computes the sum of areas 
#for any collection of shapes.Add custom exceptions


from abc import ABC, abstractmethod
import math

class InvalidDimensionError(Exception):
    """Raised when a shape is initialized with invalid dimensions."""
    pass

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <=0:
            raise InvalidDimensionError("Radius must be positive.")
        self._radius=radius

    def radius(self):
        return self._radius

    def calculate_area(self):
        return math.pi * (self._radius ** 2)
    
class Rectangle(Shape):
    def __init__(self,length,width):
        if length <= 0 or width <= 0:
            raise InvalidDimensionError("length and width must be positive.")
        self._length=length
        self._width=width

    def length(self):
        return self._length
    
    def width(self):
        return self._width 
    

    def calculate_area(self): 
        return self._length * self._width
    
class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise InvalidDimensionError("Base and Height must be positive.")
        self._base = base
        self._height = height

    def base(self):
        return self._base
    
    def heigth(self):
        return self._height

    def calculate_area(self):
        return 0.5 * self._base * self._height
    

class ShapeCalculator:
    @staticmethod
    def calculate_total_area(shapes):
        return sum(shape.calculate_area() for shape in shapes)
    
shapes = []
shapes.append(Circle(float(input("Enter the radius:"))))
shapes.append(Rectangle(float(input("Enter rectangle length")),float(input("Enter rectangle width"))))
shapes.append(Triangle(float(input("Enter base of triangle")), float(input("Enter height of triangle"))))
print("Total areas=",ShapeCalculator.calculate_total_area(shapes))


    

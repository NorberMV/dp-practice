from abc import ABC, abstractmethod


# Interface
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")

# Define a class that inheriths from 'Shape'

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")
        print(f"Width: {self.width}, Height: {self.height}")


if __name__ == "__main__":
    rectangle = Rectangle(4, 5, "purple")
    print(f"Rectangle area: {rectangle.area()}")
    print(f"Rectangle perimeter: {rectangle.perimeter()}")
    print(f"Rectangle description: {rectangle.description()}")
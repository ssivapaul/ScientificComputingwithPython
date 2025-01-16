class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Call the parent class (Rectangle) constructor with width and height as the same value
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"


# Example Usage
if __name__ == "__main__":
    rect = Rectangle(4, 5)
    print(rect)  # Output: Rectangle(width=4, height=5)
    print("Area:", rect.area())  # Output: Area: 20
    print("Perimeter:", rect.perimeter())  # Output: Perimeter: 18

    square = Square(4)
    print(square)  # Output: Square(side=4)
    print("Area:", square.area())  # Output: Area: 16
    print("Perimeter:", square.perimeter())  # Output: Perimeter: 16

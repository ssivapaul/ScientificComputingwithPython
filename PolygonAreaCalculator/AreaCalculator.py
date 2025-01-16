class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        shape = '*' *self.width + '\n'
        shape += shape*(self.height - 1)
        return shape

    def get_amount_inside(self, shape):        
        times_of_width = self.width//shape.width
        times_of_height = self.height//shape.height
        number_of_times =times_of_width * times_of_height
        return number_of_times

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height
    def __str__(self):
        return f'Square(side={self.height})'
        
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
sq.set_width(3)
sq.set_height(6)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.set_height(12)
rect.set_width(18)
print(rect)
print(rect.get_picture())
print(rect.get_amount_inside(sq))
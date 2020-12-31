class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        return(self.width + self.width + self.height + self.height)
    

rectangle = Shape(12, 15)
print(rectangle.area())
print(rectangle.perimeter())

square = Shape(12, 12)
print(square.area())
print(square.perimeter())


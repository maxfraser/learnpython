from shape import Shape

class Triangle(Shape):
    def area(self):
        return(self.width * self.height/2)

    def perimeter(self):
        return(self.width + self.width + self.width)


triangle = Triangle(19, 18)
print(triangle.area())
print(triangle.perimeter())

#define the header of the rectangle class
class Rectangle:
#define the __init__ method
    def __init__(self,width,height):
        self.width = width
        self.height = height
#define the __add__ method
    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)
#define the area method
    def area(self):
        return self.width * self.height

#create the Rectangle objects
rect1 = Rectangle(3, 4)
rect2 = Rectangle(7, 4)

#add the rectangles
rect3 = rect1 + rect2

#print the area of the resulting rectangle
print("Area of the resulting rectangle:", rect3.area())
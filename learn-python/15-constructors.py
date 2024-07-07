#  A class in Python is a way to define a custom data structure that encapsulates data and behavior,
#  allowing you to create reusable and organized code.

class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.move()

suare = Point()
suare.draw()

## By using constructors, you ensure that objects are initialized properly and consistently,
## leading to more reliable and maintainable code.
class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")

    def draw(self):
        print("draw")


point1 = Point(10,20)
print(point1.y)
point1.y =23
print(point1.y)

square = Point(4,4)
print(square.y)
square.draw()

##

class Person:
    def __init__(self , name , age ):
        self.name = name
        self.age  = age
    def detalis(self):
        print(f'Hello {self.name}')
        print(f'your age is: {self.age} years')


hema = Person("hema",20)
hema.detalis()

rama = Person("rama",18)
rama.detalis()

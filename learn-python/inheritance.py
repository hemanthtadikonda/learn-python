##By using inheritance, you can build a logical class hierarchy, promote code reuse.
# and enable polymorphic behavior, leading to a more structured and maintainable codebase.
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def shout(self):
        print("Bow Bow")

class Cat(Mammal):
    def jump(self):
        print("can jump")


cow = Mammal()
cow.walk()

tom = Dog()
tom.walk()
tom.shout()

cay = Cat()
cay.walk()
cay.jump()


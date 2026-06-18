# Polymorphism: one interface, many behaviors.
# The same method call or operator does the right thing for each object type.


# 1. Method overriding: subclasses each redefine the same base method.
# Loop over a list of different objects and call the same method on each;
# Python dispatches to the version defined on each object's own class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):  # base behavior, meant to be overridden
        return f"{self.name} makes a generic sound"


class Dog(Animal):
    def speak(self):  # override: Dog's own version
        return f"{self.name} says Woof"


class Cat(Animal):
    def speak(self):  # override: Cat's own version
        return f"{self.name} says Meow"


class Cow(Animal):
    def speak(self):  # override: Cow's own version
        return f"{self.name} says Moo"


print("\n--- 1. Method overriding across subclasses ---")
animals = [Animal("Creature"), Dog("Rex"), Cat("Whiskers"), Cow("Bessie")]
for animal in animals:  # same call, different result per object
    print("speak:", animal.speak())  # each runs its own overridden version


# 2. Duck typing: "if it quacks like a duck, treat it as a duck."
# A function works on ANY object that has the needed method, even if the
# classes are unrelated and share no common base class.
class Duck:
    def quack(self):
        return "Quack quack"


class Person:  # totally unrelated to Duck, but also has quack()
    def quack(self):
        return "I'm imitating a duck"


def make_it_quack(thing):  # cares only that thing.quack() exists
    return thing.quack()


print("\n--- 2. Duck typing ---")
print("Duck quack:", make_it_quack(Duck()))
print("Person quack:", make_it_quack(Person()))  # works despite no shared base


# 3. A polymorphic function treating different shapes uniformly.
# Each shape exposes an area() method; the function uses that shared
# interface without caring about the concrete type.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def print_area(shape):  # uniform handling via the shared area() interface
    return f"{type(shape).__name__} area = {shape.area():.2f}"


print("\n--- 3. Polymorphic function over shapes ---")
shapes = (Circle(5), Rectangle(4, 3), Square(2))
for shape in shapes:  # one function, many shape types
    print(print_area(shape))


# 4. Built-in polymorphism: len() and + adapt to the type given.
print("\n--- 4. Built-in polymorphism: len() and + ---")
print("len of string:", len("hello"))  # counts characters
print("len of list:", len([1, 2, 3, 4]))  # counts elements
print("len of dict:", len({"a": 1, "b": 2}))  # counts key/value pairs
print("int + int (addition):", 2 + 3)  # numeric addition
print("str + str (concatenation):", "foo" + "bar")  # joins text
print("list + list (joining):", [1, 2] + [3, 4])  # merges into one list


# 5. Operator overloading preview: make + work on YOUR objects.
# Defining __add__ lets Python's + operator add Vector instances.
# (Dunder methods get full coverage in their own file: 06_dunder_methods.py.)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # called when you write vector_a + vector_b
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):  # readable text form for printing
        return f"Vector({self.x}, {self.y})"


print("\n--- 5. Operator overloading preview (__add__) ---")
vector_a = Vector(1, 2)
vector_b = Vector(3, 4)
print("vector_a:", vector_a)
print("vector_b:", vector_b)
print("vector_a + vector_b:", vector_a + vector_b)  # uses our __add__

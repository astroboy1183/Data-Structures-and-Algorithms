# Abstraction: define WHAT must exist, not HOW, via abstract base classes.
# An ABC (abc.ABC) with @abstractmethod forces subclasses to fill in the gaps.

from abc import ABC, abstractmethod


# 1. Define an abstract base class; you CANNOT instantiate it directly.
# Shape declares area() as abstract, so Shape itself is incomplete.
class Shape(ABC):
    @abstractmethod
    def area(self):  # no body needed; subclasses MUST provide one
        ...


print("\n--- 1. Cannot instantiate an abstract base class ---")
try:
    bad = Shape()  # abstract class has an unimplemented method
    print("created:", bad)  # never reached
except TypeError as error:  # Python refuses to build it
    print("caught TypeError:", error)


# 2. A concrete subclass that implements the abstract method.
# Square fills in area(), so it becomes a fully usable class.
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # concrete implementation satisfies the contract
        return self.side * self.side


print("\n--- 2. Concrete subclass implements the abstract method ---")
square = Square(4)  # works: nothing abstract remains
print("square side:", square.side)
print("square area:", square.area())
print("isinstance of Shape:", isinstance(square, Shape))  # True


# 3. A subclass that does NOT implement the abstract method.
# Triangle forgets area(), so it stays abstract and can't be built.
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    # note: no area() here, so the abstract method is still unfilled


print("\n--- 3. Subclass missing the abstract method stays abstract ---")
try:
    shape = Triangle(3, 6)  # area() never implemented
    print("created:", shape)  # never reached
except TypeError as error:  # error names the missing method
    print("caught TypeError:", error)


# 4. Multiple concrete subclasses sharing one interface, used polymorphically.
# Circle and Rectangle each implement area() their own way.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # circle's own formula
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # rectangle's own formula
        return self.width * self.height


print("\n--- 4. Many shapes, one interface, used polymorphically ---")
shapes = [Circle(2), Rectangle(3, 4), Square(5)]  # all are Shapes
for item in shapes:  # same call works on every concrete type
    print(f"{type(item).__name__} area:", round(item.area(), 2))


# 5. Template pattern: a concrete method calls an abstract one.
# describe() is shared behavior; area() is the slot each subclass fills.
class DescribableShape(ABC):
    @abstractmethod
    def area(self):  # the variable part subclasses must supply
        ...

    def describe(self):  # concrete method inherited by all subclasses
        # relies on the subclass's area() to build a shared message
        return f"{type(self).__name__} with area {round(self.area(), 2)}"


class Pentagon(DescribableShape):
    def __init__(self, side):
        self.side = side

    def area(self):  # fill in only the abstract part
        return 1.72048 * self.side * self.side


print("\n--- 5. Template pattern: shared method calls abstract method ---")
pentagon = Pentagon(6)  # inherits describe(), supplies area()
print("pentagon area:", round(pentagon.area(), 2))
print("pentagon describe:", pentagon.describe())  # uses inherited template


# 6. An abstract PROPERTY combining @property with @abstractmethod.
# name is required to exist as a property; subclasses must define it.
class NamedShape(ABC):
    @property
    @abstractmethod
    def name(self):  # subclasses MUST expose a 'name' property
        ...


class Hexagon(NamedShape):
    @property
    def name(self):  # concrete property implementation
        return "Hexagon"


print("\n--- 6. Abstract property implemented in a subclass ---")
hexagon = Hexagon()  # works: the abstract property is implemented
print("hexagon name:", hexagon.name)  # accessed like an attribute
print("isinstance of NamedShape:", isinstance(hexagon, NamedShape))  # True

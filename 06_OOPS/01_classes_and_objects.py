# Classes & Objects: the fundamentals of OOP in Python.
# A class is a blueprint; an object (instance) is a thing built from it.


# 1. Define a class and create MULTIPLE objects (instances).
# The class is the blueprint; each call to Car() builds a separate object.
class Car:
    pass


print("\n--- 1. Define a class and create multiple objects ---")
car_a = Car()  # first independent object
car_b = Car()  # second independent object
car_a.color = "red"  # set an attribute on car_a only
car_b.color = "blue"  # car_b has its own separate attribute
print("car_a color:", car_a.color)
print("car_b color:", car_b.color)
print("car_a is car_b:", car_a is car_b)  # False: two distinct objects


# 2. The __init__ constructor and instance attributes.
# __init__ runs automatically when the object is created. 'self' is the
# object being built; self.name stores data on THAT specific object.
class Student:
    def __init__(self, name, grade):
        self.name = name  # instance attribute, unique per object
        self.grade = grade  # instance attribute, unique per object


print("\n--- 2. The __init__ constructor and instance attributes ---")
alice = Student("Alice", 90)  # __init__ called with name="Alice", grade=90
bob = Student("Bob", 75)  # a different object with its own attributes
print("alice name:", alice.name)
print("alice grade:", alice.grade)
print("bob name:", bob.name)
print("bob grade:", bob.grade)


# 3. Instance methods take self and use the object's attributes.
class StudentWithMethods:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def describe(self):  # 'self' lets the method read this object's data
        return f"{self.name} has grade {self.grade}"

    def has_passed(self):  # methods can compute results from attributes
        return self.grade >= 50


print("\n--- 3. Instance methods that use the attributes ---")
carol = StudentWithMethods("Carol", 88)
dave = StudentWithMethods("Dave", 40)
print("carol describe:", carol.describe())
print("dave describe:", dave.describe())
print("carol has_passed:", carol.has_passed())
print("dave has_passed:", dave.has_passed())


# 4. Class attribute (shared by ALL instances) vs instance attribute.
# 'school' lives on the class, so every instance sees the same value.
class SchoolStudent:
    school = "Greenwood High"  # class attribute, shared by all instances

    def __init__(self, name):
        self.name = name  # instance attribute, per object


print("\n--- 4. Class attribute vs instance attribute ---")
eve = SchoolStudent("Eve")
frank = SchoolStudent("Frank")
print("eve school:", eve.school)
print("frank school:", frank.school)
SchoolStudent.school = "Riverside Academy"  # change on the class itself
print("eve school after class change:", eve.school)  # affects all instances
print("frank school after class change:", frank.school)
eve.school = "Private Tutor"  # assigning to the instance shadows the class attr
print("eve school (shadowed):", eve.school)  # only eve changes
print("frank school (still class value):", frank.school)  # unchanged
print("class attribute value:", SchoolStudent.school)  # the class is unchanged


# 5. Default parameter values in __init__.
# If an argument is omitted, the default is used.
class Vehicle:
    def __init__(self, brand, wheels=4, electric=False):
        self.brand = brand  # required argument
        self.wheels = wheels  # defaults to 4 if not given
        self.electric = electric  # defaults to False if not given


print("\n--- 5. Default parameter values in __init__ ---")
sedan = Vehicle("Toyota")  # uses both defaults
bike = Vehicle("Harley", wheels=2)  # override one default
tesla = Vehicle("Tesla", electric=True)  # override another default
print("sedan brand/wheels/electric:", sedan.brand, sedan.wheels, sedan.electric)
print("bike brand/wheels/electric:", bike.brand, bike.wheels, bike.electric)
print("tesla brand/wheels/electric:", tesla.brand, tesla.wheels, tesla.electric)


# 6. Inspecting an object: type, isinstance, and __dict__.
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


print("\n--- 6. Inspecting an object ---")
novel = Book("Dune", 412)
print("type of novel:", type(novel))  # <class '...Book'>
print("isinstance Book:", isinstance(novel, Book))  # True
print("isinstance str:", isinstance(novel, str))  # False: not a string
print("novel __dict__:", novel.__dict__)  # instance attributes as a dict


# 7. Adding / modifying attributes after creation.
# Python lets you set brand-new attributes on an instance at any time.
class Phone:
    def __init__(self, model):
        self.model = model


print("\n--- 7. Adding / modifying attributes after creation ---")
my_phone = Phone("Pixel")
print("before, model:", my_phone.model)
my_phone.model = "Pixel Pro"  # modify an existing attribute
my_phone.storage_gb = 256  # add a brand-new attribute not in __init__
print("after, model:", my_phone.model)
print("new attribute storage_gb:", my_phone.storage_gb)
print("updated __dict__:", my_phone.__dict__)

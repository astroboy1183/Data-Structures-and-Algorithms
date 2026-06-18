# Inheritance: a child class reuses and extends a parent class.
# The parent (base) defines shared behavior; the child (derived) adds more.


# 1. Single inheritance: a child inherits the parent's attributes and methods.
# Dog inherits from Animal, so a Dog object can call Animal's methods.
class Animal:
    def __init__(self, name):
        self.name = name  # attribute defined on the parent

    def eat(self):  # method defined on the parent
        return f"{self.name} is eating"


class Dog(Animal):  # Dog(Animal) means Dog inherits from Animal
    pass  # adds nothing yet; reuses everything from Animal


print("\n--- 1. Single inheritance ---")
rex = Dog("Rex")  # Dog has no __init__, so Animal's __init__ runs
print("rex name (inherited attr):", rex.name)
print("rex eat (inherited method):", rex.eat())  # eat() comes from Animal


# 2. super().__init__(): the child sets shared attributes via the parent,
# then adds its own. This avoids repeating the parent's setup code.
class Pet(Animal):
    def __init__(self, name, owner):
        super().__init__(name)  # runs Animal.__init__ to set self.name
        self.owner = owner  # then add a new attribute specific to Pet


print("\n--- 2. super().__init__() ---")
buddy = Pet("Buddy", "Alice")
print("buddy name (set by parent):", buddy.name)
print("buddy owner (set by child):", buddy.owner)
print("buddy eat (still inherited):", buddy.eat())


# 3. Method overriding AND extending: the child redefines a method but calls
# super().method() inside it to reuse the parent's logic, then adds more.
class Cat(Animal):
    def eat(self):  # override: same method name as the parent's
        base = super().eat()  # reuse the parent's eat() result
        return f"{base} (quietly, like a cat)"  # extend with extra detail


print("\n--- 3. Method overriding and extending ---")
whiskers = Cat("Whiskers")
print("whiskers eat (overridden + extended):", whiskers.eat())


# 4. Multilevel inheritance: A -> B -> C, where C inherits through B from A.
class LivingThing:  # level A
    def breathe(self):
        return "breathing"


class Mammal(LivingThing):  # level B, inherits from A
    def feed_milk(self):
        return "feeding milk"


class Puppy(Mammal):  # level C, inherits from B (and thus from A)
    def play(self):
        return "playing"


print("\n--- 4. Multilevel inheritance (A -> B -> C) ---")
pup = Puppy()
print("pup breathe (from A):", pup.breathe())  # reached through B
print("pup feed_milk (from B):", pup.feed_milk())
print("pup play (own method C):", pup.play())


# 5. Multiple inheritance / mixin: a class inheriting from two parents.
# SwimMixin adds one ability; combined with Animal it makes a Duck.
class SwimMixin:  # a mixin: a small class meant to add one capability
    def swim(self):
        return f"{self.name} is swimming"  # relies on a 'name' attribute


class Duck(Animal, SwimMixin):  # inherits from BOTH Animal and SwimMixin
    def speak(self):
        return f"{self.name} says quack"


print("\n--- 5. Multiple inheritance / mixin + MRO ---")
donald = Duck("Donald")
print("donald eat (from Animal):", donald.eat())
print("donald swim (from SwimMixin):", donald.swim())
print("donald speak (own method):", donald.speak())
# __mro__ is the Method Resolution Order: where Python searches for methods.
print("Duck MRO:", [cls.__name__ for cls in Duck.__mro__])


# 6. isinstance(obj, Class) and issubclass(Child, Parent) checks.
print("\n--- 6. isinstance and issubclass ---")
print("isinstance(rex, Dog):", isinstance(rex, Dog))  # True
print("isinstance(rex, Animal):", isinstance(rex, Animal))  # True: Dog is Animal
print("isinstance(rex, Cat):", isinstance(rex, Cat))  # False: unrelated sibling
print("issubclass(Dog, Animal):", issubclass(Dog, Animal))  # True
print("issubclass(Puppy, LivingThing):", issubclass(Puppy, LivingThing))  # True
print("issubclass(Animal, Dog):", issubclass(Animal, Dog))  # False: wrong way
print("issubclass(Duck, SwimMixin):", issubclass(Duck, SwimMixin))  # True

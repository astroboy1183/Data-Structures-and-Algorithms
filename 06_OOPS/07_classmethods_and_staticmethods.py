# Instance methods vs @classmethod vs @staticmethod.
# Instance = needs object data; classmethod = needs the class;
# staticmethod = standalone helper grouped on the class.


# 1. The three method types side by side in ONE class.
# instance method gets the object (self); classmethod gets the class
# (cls); staticmethod gets neither and is just a plain function.
class Toolbox:
    brand = "Acme"  # class attribute, shared by every instance

    def __init__(self, owner):
        self.owner = owner  # instance attribute, unique per object

    def instance_method(self):  # receives the object as 'self'
        return f"instance_method sees owner={self.owner}, brand={self.brand}"

    @classmethod
    def class_method(cls):  # receives the class as 'cls'
        return f"class_method sees the class {cls.__name__}, brand={cls.brand}"

    @staticmethod
    def static_method():  # no self, no cls: a grouped plain function
        return "static_method gets neither self nor cls"


print("\n--- 1. The three method types side by side ---")
box = Toolbox("Jay")
print("instance call:", box.instance_method())  # self = box
print("class call:", Toolbox.class_method())  # cls = Toolbox
print("static call:", Toolbox.static_method())  # no implicit argument
# classmethod and staticmethod also work when called via an instance:
print("classmethod via instance:", box.class_method())  # cls still Toolbox
print("staticmethod via instance:", box.static_method())  # same plain result


# 2. A @classmethod that reads/updates a CLASS attribute.
# 'count' lives on the class, so a classmethod is the natural place to
# read and reset a running total shared by all Employee objects.
class Employee:
    count = 0  # class attribute: how many employees have been created

    def __init__(self, name):
        self.name = name  # instance attribute
        Employee.count += 1  # update the shared class-level counter

    @classmethod
    def how_many(cls):  # reads the shared counter via the class
        return cls.count

    @classmethod
    def reset_count(cls):  # updates the shared counter via the class
        cls.count = 0


print("\n--- 2. @classmethod reads/updates a class attribute ---")
print("employees at start:", Employee.how_many())  # 0
emp_a = Employee("Asha")
emp_b = Employee("Ben")
print("created:", emp_a.name, "and", emp_b.name)
print("employees after creating two:", Employee.how_many())  # 2
Employee.reset_count()  # classmethod updates the shared count
print("employees after reset:", Employee.how_many())  # 0


# 3. A @classmethod used as an ALTERNATIVE CONSTRUCTOR.
# The normal __init__ takes numbers; from_string parses text and then
# returns cls(...) so the SAME class can be built from a different input.
class Date:
    def __init__(self, year, month, day):
        self.year = year  # store the three parts as instance attributes
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text):  # alternative constructor from "Y-M-D"
        year, month, day = text.split("-")  # split the string into parts
        return cls(int(year), int(month), int(day))  # build a real object

    def __repr__(self):  # readable text so prints show the contents
        return f"Date({self.year}, {self.month}, {self.day})"


print("\n--- 3. @classmethod as an alternative constructor ---")
normal_date = Date(2026, 6, 16)  # built the usual way
parsed_date = Date.from_string("2026-06-16")  # built from a string
print("normal_date:", normal_date)
print("parsed_date:", parsed_date)
print("parsed_date is a Date:", isinstance(parsed_date, Date))  # True
print("parsed year/month/day:", parsed_date.year, parsed_date.month,
      parsed_date.day)


# 4. A @staticmethod as a utility that needs no self/cls.
# is_leap_year only needs a plain number; it belongs ON Date for
# organization but does not touch any particular object or the class.
class Calendar:
    @staticmethod
    def is_leap_year(year):  # pure helper grouped on the class
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def is_weekend(day_name):  # another standalone helper
        return day_name.lower() in {"saturday", "sunday"}


print("\n--- 4. @staticmethod as a utility function ---")
print("2024 is leap year:", Calendar.is_leap_year(2024))  # True
print("2026 is leap year:", Calendar.is_leap_year(2026))  # False
print("1900 is leap year:", Calendar.is_leap_year(1900))  # False (century rule)
print("2000 is leap year:", Calendar.is_leap_year(2000))  # True (400 rule)
print("Sunday is weekend:", Calendar.is_weekend("Sunday"))  # True
print("Monday is weekend:", Calendar.is_weekend("Monday"))  # False


# 5. WHEN to use each (summary).
print("\n--- 5. When to use each method type ---")
# Instance method (self):  use when the work needs THIS object's data,
#                          e.g. emp.name or self.year.
# @classmethod (cls):      use when the work needs the CLASS itself,
#                          e.g. a shared counter or an alternative
#                          constructor that returns cls(...).
# @staticmethod (neither): use for a standalone helper that logically
#                          belongs with the class but touches no object
#                          and no class state, e.g. is_leap_year(year).
print("Instance method -> needs object data (self)")
print("@classmethod    -> needs the class / alternative constructor (cls)")
print("@staticmethod   -> standalone helper grouped on the class")

# Encapsulation: bundling data + methods in a class and controlling access
# to that data using public, protected, and private members.


# 1. Public attributes are part of the class's open interface. Any code can
# read them and write to them freely without restriction.
print("\n--- 1. Public Attributes ---")


class PersonPublic:
    """A person whose data is fully public."""

    def __init__(self, name, age):
        self.name = name  # public attribute
        self.age = age  # public attribute


person = PersonPublic("Alice", 30)
print("Read public name:", person.name)
person.name = "Alicia"  # freely writable from outside
print("After writing public name:", person.name)


# 2. A single leading underscore marks an attribute as "protected". This is
# only a CONVENTION: Python does not block access, it signals "internal use".
print("\n--- 2. Protected Attribute (single underscore) ---")


class PersonProtected:
    """A person with a protected attribute by convention."""

    def __init__(self, name, ssn):
        self.name = name  # public
        self._ssn = ssn  # protected: please do not touch from outside


citizen = PersonProtected("Bob", "123-45-6789")
print("Public name:", citizen.name)
# Still reachable, but we are breaking convention by reading it directly.
print("Protected _ssn (accessible but discouraged):", citizen._ssn)


# 3. A double leading underscore triggers NAME MANGLING. Python rewrites
# __balance to _ClassName__balance, so it is hard to reach by accident.
print("\n--- 3. Private Attribute (double underscore, name mangling) ---")


class BankAccountPrivate:
    """A bank account with a name-mangled private attribute."""

    def __init__(self, balance):
        self.__balance = balance  # becomes _BankAccountPrivate__balance

    def show_balance(self):
        return self.__balance  # works fine inside the class


account = BankAccountPrivate(500)
print("Balance via method:", account.show_balance())
# Reachable only via the mangled name from outside the class:
print("Mangled access:", account._BankAccountPrivate__balance)
try:
    print(account.__balance)  # plain name does not exist outside the class
except AttributeError as error:
    print("AttributeError reading __balance:", error)


# 4. Getter and setter METHODS give the class control over how a private
# attribute is read and written, letting us add rules in one place.
print("\n--- 4. Getter and Setter Methods ---")


class BankAccountMethods:
    """A bank account exposing its balance via explicit methods."""

    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance  # controlled read

    def set_balance(self, amount):
        if amount < 0:  # rule enforced in one place
            print("Rejected: balance cannot be negative")
            return
        self.__balance = amount  # controlled write


savings = BankAccountMethods(1000)
print("Getter returns:", savings.get_balance())
savings.set_balance(1500)
print("After valid setter:", savings.get_balance())
savings.set_balance(-50)  # rejected by the setter's rule
print("After invalid setter:", savings.get_balance())


# 5. The @property decorator turns a method into a Pythonic getter, so the
# value is read like a plain attribute (no parentheses needed).
print("\n--- 5. @property as a Pythonic Getter ---")


class BankAccountProperty:
    """A bank account whose balance is read via a property."""

    def __init__(self, balance):
        self.__balance = balance  # private

    @property
    def balance(self):
        return self.__balance  # accessed as account.balance


checking = BankAccountProperty(750)
print("Read like an attribute:", checking.balance)  # no () after balance


# 6. A @property setter can VALIDATE input before storing it. Here a negative
# balance is rejected by raising ValueError, caught with try/except.
print("\n--- 6. @property Setter With Validation ---")


class BankAccountValidated:
    """A bank account whose setter validates the new balance."""

    def __init__(self, balance):
        self.__balance = balance  # private

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:  # reject invalid input
            raise ValueError("balance cannot be negative")
        self.__balance = amount


wallet = BankAccountValidated(200)
wallet.balance = 350  # valid assignment goes through the setter
print("After valid assignment:", wallet.balance)
try:
    wallet.balance = -100  # triggers the validation rule
except ValueError as error:
    print("ValueError from setter:", error)


# 7. A property with only a getter is READ-ONLY. Because no setter is defined,
# assigning to it raises AttributeError, which we catch and display.
print("\n--- 7. Read-Only Property (getter only) ---")


class BankAccountReadOnly:
    """A bank account exposing a read-only account number."""

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private
        self.__balance = balance  # private

    @property
    def account_number(self):
        return self.__account_number  # no setter defined -> read-only

    @property
    def balance(self):
        return self.__balance


fixed = BankAccountReadOnly("ACC-001", 999)
print("Read-only account number:", fixed.account_number)
try:
    fixed.account_number = "ACC-002"  # no setter -> not allowed
except AttributeError as error:
    print("AttributeError assigning read-only property:", error)

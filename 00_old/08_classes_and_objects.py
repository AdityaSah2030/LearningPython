"""
This script demonstrates:
1. Defining a basic class with an __init__ constructor.
2. Instance attributes and methods.
3. Class attributes.
4. Static methods and class methods.
5. Inheritance and method overriding.
6. Encapsulation and using property decorators for controlled attribute access.

How to run:
    python 08_classes_and_objects.py
"""

# ------------------------------------------------------------------------------
# SECTION 1: Basic Class and Instance Attributes
# ------------------------------------------------------------------------------
print("=== SECTION 1: BASIC CLASS AND INSTANCE ATTRIBUTES ===")

class Person:
    """
    A simple Person class.
    """
    # Class attribute: shared by all instances
    species = "Homo sapiens"

    def __init__(self, name, age):
        """
        Constructor to initialize name and age.
        """
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute

    def introduce(self):
        """
        Instance method: prints a greeting with the person's name.
        """
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Create an instance of Person
alice = Person("Alice", 30)
alice.introduce()
print("Species:", alice.species)
print()

# ------------------------------------------------------------------------------
# SECTION 2: Class Methods and Static Methods
# ------------------------------------------------------------------------------
print("=== SECTION 2: CLASS METHODS AND STATIC METHODS ===")

class Person:
    """
    Enhanced Person class with class and static methods.
    """
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def change_species(cls, new_species):
        """
        Class method: modifies the class attribute 'species'.
        """
        cls.species = new_species

    @staticmethod
    def is_adult(age):
        """
        Static method: returns True if the given age qualifies as an adult.
        Does not access class or instance attributes.
        """
        return age >= 18

# Demonstrate class method
bob = Person("Bob", 17)
print(f"Before change, species of Bob: {bob.species}")
Person.change_species("Modern Homo sapiens")
print(f"After change, species of Bob: {bob.species}")
print(f"Is Bob an adult? {Person.is_adult(bob.age)}")
print()

# ------------------------------------------------------------------------------
# SECTION 3: Inheritance and Method Overriding
# ------------------------------------------------------------------------------
print("=== SECTION 3: INHERITANCE AND METHOD OVERRIDING ===")

class Student(Person):
    """
    Student class inherits from Person and adds an extra attribute.
    """
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of Person
        self.student_id = student_id  # Additional attribute for Student

    # Overriding the introduce() method to include student_id
    def introduce(self):
        print(f"Hello, I am {self.name}, {self.age} years old, and my student ID is {self.student_id}.")

# Create an instance of Student
charlie = Student("Charlie", 20, "S12345")
charlie.introduce()
print()

# ------------------------------------------------------------------------------
# SECTION 4: Encapsulation and Property Decorators
# ------------------------------------------------------------------------------
print("=== SECTION 4: ENCAPSULATION AND PROPERTY DECORATORS ===")

class BankAccount:
    """
    A simple BankAccount class demonstrating encapsulation.
    The balance is a 'protected' attribute (conventionally, using a single underscore)
    and can be accessed via a property.
    """
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance  # Protected attribute

    @property
    def balance(self):
        """
        Getter method for balance.
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Setter method for balance with validation.
        """
        if amount < 0:
            print("Error: Balance cannot be negative.")
        else:
            self._balance = amount

    def deposit(self, amount):
        """
        Deposits a positive amount into the account.
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws an amount from the account if sufficient balance exists.
        """
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Error: Insufficient balance or invalid amount.")

# Create an instance of BankAccount
account = BankAccount("Diana", 1000)
print(f"Account owner: {account.owner} | Initial balance: {account.balance}")
account.deposit(500)
account.withdraw(300)
account.balance = 2000  # Using the setter
print("Updated balance via property:", account.balance)
account.balance = -100  # Attempt to set a negative balance
print()

# ------------------------------------------------------------------------------
# END OF SCRIPT
# ------------------------------------------------------------------------------
print("End of 08_classes_and_objects.py")

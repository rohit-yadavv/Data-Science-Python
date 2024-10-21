"""

Inheritance: A mechanism where a class (derived/child class) inherits attributes and methods from another class (base/parent class).

Purpose: Promotes code reusability and establishes relationships between classes.

Method Overriding:
Child class can redefine a method from the parent class.
Use super() to call the parent class's method


"""


class BaseClass:
	# Base class members
	pass


class DerivedClass(BaseClass):
	# Derived class members
	pass


class Parent:
	def show(self):
		print("Parent class")


class Child(Parent):
	def show(self):
		super().show()  # Calls Parent method
		print("Child class")


c = Child()
c.show()


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"name is {self.name} and id is {self.id}")


class Programmer(Employee):
    def showLanguage(slef):
        print("the lang is python")


# e1 = Employee("rohit", 1)
# e1.showDetails()
# # e1.showLanguage() will give error as show lang is in programmer and not in employyee

# e2 = Programmer("mohi", 2)
# e2.showLanguage()
# e2.showDetails()  # will work as programmer as inherited all the things of employee

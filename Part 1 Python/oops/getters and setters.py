'''

In Python, getters and setters are methods used to access and modify private or protected attributes of a class. 
While Python does not have explicit keywords for getters and setters like C++, 
it uses the @property decorator to create a getter and @<property_name>.setter decorator for the setter.

'''
class Person:
    def __init__(self, name):
        self._name = name  # The attribute is "protected"

    # Getter method using @property
    @property
    def name(self):
        print("Getting name")
        return self._name

    # Setter method using @name.setter
    @name.setter
    def name(self, value):
        print("Setting name")
        self._name = value

# Usage
p = Person("Rohit")
print(p.name)  # Calls the getter
p.name = "Yadav"  # Calls the setter
print(p.name)  # Calls the getter again



 
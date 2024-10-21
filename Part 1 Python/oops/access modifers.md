### Access Modifiers in Python - Complete Notes:

In Python, access modifiers are implemented through **naming conventions** rather than keywords like `public`, `private`, and `protected`. These conventions control the accessibility of class attributes and methods, but **all attributes are technically accessible** due to Python's flexible nature.

#### Types of Access Modifiers:

1. **Public**:
   - **Syntax**: No prefix (`public_var`)
   - **Access**: Accessible from **anywhere** (inside and outside the class).
   - **Usage**: Public members are default in Python and can be accessed directly.
   - **Example**:
     ```python
     class MyClass:
         def __init__(self):
             self.public_var = "I am public"

     obj = MyClass()
     print(obj.public_var)  # Accessible anywhere
     ```

2. **Protected**:
   - **Syntax**: Single underscore (`_protected_var`)
   - **Access**: Accessible within the class and **subclasses**, but **not restricted** from outside the class.
   - **Convention**: Indicates that the member is intended for internal use or subclass use, but it can still be accessed outside (just a warning, not enforced).
   - **Example**:
     ```python
     class MyClass:
         def __init__(self):
             self._protected_var = "I am protected"

     obj = MyClass()
     print(obj._protected_var)  # Accessible, but discouraged
     ```

3. **Private**:
   - **Syntax**: Double underscore (`__private_var`)
   - **Access**: Restricted to the **class only**. Cannot be accessed directly from outside the class.
   - **Enforced**: Python uses **name mangling** to make private attributes harder to access, but they can still be accessed using the mangled name (`_ClassName__private_var`).
   - **Example**:
     ```python
     class MyClass:
         def __init__(self):
             self.__private_var = "I am private"

     obj = MyClass()
     # print(obj.__private_var)  # Raises an AttributeError
     print(obj._MyClass__private_var)  # Accessed via name mangling
     ```

#### Name Mangling:
- **Private attributes** (`__var`) are internally renamed by Python to `_ClassName__var` to prevent accidental access, but not fully private.
- This provides a **strong hint** not to access them directly, but they **can still be accessed** if needed.

#### Key Points:
- **Public** members are fully accessible everywhere.
- **Protected** members (using a single `_`) are accessible, but should be treated as "internal" members.
- **Private** members (using `__`) are more restricted, but can still be accessed through name mangling.
- Access modifiers in Python are **mostly conventions** and do not provide true encapsulation like in other languages.


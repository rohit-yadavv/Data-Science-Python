# is =>  checks exact location of object in memory 
# == =>  it compares values

a = 4
b = "4"

print(a is b)
print(a == b) 

a = 3
b = 3

# as 3 is const python crates a memory location of 3 as it is constant and will not changes
# for immutable type same values will have same memory location but not mutable

print("for immutable: ", a is b)
print("for immutable: ", a == b) 

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print("for list (mutable): ", a is b)
print("for list (mutable): ", a == b) 

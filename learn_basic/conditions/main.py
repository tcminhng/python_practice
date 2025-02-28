# Basic condition
# x = 2
x = "2" # String 
print(x == 2)
print(x == 3)
# print(x < 3)
print(x == "3")
print(x != "3")
print(x != 3)

# ==, != -> Compare Datatype -> compare Value
# >= <= -> Compare digit, float (compare Value)

#################
# Boolean operation: and, or
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# "in" -> List
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick. <- Here")

# ^ Same thing
for n in ["John", "Rick"]:
    if n == name:
        print("Your name is either John or Rick. <- Here")

# If statement
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# "is" operation: Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. For example:
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# "not"
print(not False) # Prints out True
print((not False) == (False)) # Prints out False
astring = "Hello world!"
astring2 = 'Hello world!'

# Print length
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# Print index
astring = "Hello world!"
print(astring.index("o"))

# Count 
astring = "Hello world!"
print(astring.count("l"))

# Print partially
astring = "Hello world!"
print(astring[0:3])
print(astring[:3])
print(astring[:])
print(astring[-1])
print(astring[3:-1])
print(astring[3:])

# Print skip step
# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:2])

# Reverse print
astring = "Hello world!"
print(astring[::-1])

# Upper lower
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# Get letter
string = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# Split string into a list
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
# Assignment: Give array of name, add a name, remove last name, remove name at position 2

# Array initialization
name = ["Minh Nguyen", "Diana", "Rose"]
print(name)

for i in range(len(name)):
    print(name[i])

# Add a new array
name.append("Michael")
print(name)

# Remove last array
name.pop()
print(name)

# Remove array at position 2
name.remove(name[1])
print(name)

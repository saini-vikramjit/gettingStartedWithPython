friends = ["Ravi", "Mahipal", "Srinath", "Mohit", "Aurolina"]

print(friends)

print(friends[1])

print(friends[-1])

print(friends[2:])

print(friends[1:3])

#list functions

luckyNumbers = [1,45,19,23,81,13,45]

# Appending item to end of list
luckyNumbers.append(71)
print(luckyNumbers)

# Appending list to list
#friends.extend(luckyNumbers)
#print(friends)

# Insert item to particular index
luckyNumbers.insert(0,21)
print(luckyNumbers)

# Remove item from list
friends.remove("Mohit")
print(friends)

# Clear a list
#friends.clear()
#print(friends)

# Remove element from end of list
luckyNumbers.pop()
print(luckyNumbers)

# Find the index of item in the list
print(luckyNumbers.index(23))

# Find the count of same item in the list
print(luckyNumbers.count(45))

# Sort the list
brands = ["Nike", "Rebook", "Addidas", "Puma", "New Balance"]
brands.sort()
print(brands)
luckyNumbers.sort()
print(luckyNumbers)

# Create copy of the list
sportBrands = brands.copy()
print(sportBrands)


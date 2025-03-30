# SETs : are Unordered collection of unique elements
s = {1,2,3,4,5,6,7,8,9,10}
print(s)
# print(s[2]) # Error: 'set' object is not subscriptable

# functions of the sets : 

# Add an element to the set
s.add(11)
print(s)

# Remove an element from the set
s.remove(5)
print(s)
s.discard(2)
print(s)

# Check if an element is in the set
print(3 in s)

# Get the length of the set
print(len(s))

# Clear the set
s.clear()
print(s)

# isdisjoint
# issubset
# issuperset
# union
# intersection
# difference
# update
# intersection_update
# difference_update
# symmetric_difference
# symmetric_difference_update

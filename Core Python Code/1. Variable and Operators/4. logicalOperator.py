# Logical and
a = 4
b = 6
c = 2
d = 555

print("******* Logical and *******")
print(a > b and a > c)
print(a > b and a < c)
print(a < b and a > c)
print(a < b and a < c)
print(a > b and c)
print(a > b and c and d)
print(a < b and c)
print(a < b and c and d)

# Logical or
print("******* Logical or *******")
print(a > b or a > c)
print(a > b or a < c)
print(a < b or a > c)
print(a < b or a < c)
print(a > b or c)
print(a > b or c or d)
print(a < b or c)
print(a < b or c or d)

# Logical not
print("******* Logical not *******")
print(not (a < b))
print(not (a > b))

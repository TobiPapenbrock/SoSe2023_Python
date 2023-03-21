i   = 28.0
f   = 28.0

print(type(i), id(i), i)
print(type(f), id(f), f)

i+=1
print(type(i), id(i), i)
print(type(f), id(f), f)

# Liste
m   = ['a', 'b', 'c', 'e', 'f']

print(id(m))
m[0] = "A"
print(id(m))

# Tupel
l   = ('a', 'b', 'c', 'e', 'f')
print(id(l))
l+="x",
print(l)
print(id(l))

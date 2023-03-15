print("---Immutable---")
x=100
print("ID von x, ",id(x))
y=x
print("ID von y, ", id(y))
y+=1
print("ID von y, ",id(y))
print("")
f=(1,2,3)
print("ID von f,", id(f))
g=f
print("g", g)
print("ID von g,", id(g))

print("")
print("---Mutable---")
a=[1,2,3]
print ("ID von a,", id(a))
print ("Wert von a,", a)
b=a
print ("ID von b,", id(b))
print ("Wert von b,", b)
b+=[4]
print ("ID von b,", id(b))
print ("Wert von b,", b)
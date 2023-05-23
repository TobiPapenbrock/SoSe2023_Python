

# Nr. 1
def quadrat(x=None):
    """Diese Funktion quadriert die Zahl 'x'."""
    if(x is None):
        return x
    else:
        return x**2

# Nr. 2
def addition(x, *y):
    """Diese Funktion lässt zwei oder mehr Zahlen addieren"""
    return x+sum(y)

# Nr. 3
def quad_func(x,a=1,b=1,c=1):
    """Berechnung der Funktion f(x) = a*x^2 + b*x + c."""
    return a* x**2 + b*x + c

# Nr.1 & 2 
print(quadrat(10))
print(quadrat())
print("")

# Nr. 3
print(addition(3,4,5,6,7))
print("")

#Nr. 4
i=0
while i<=10:
    print(quad_func(i,1,2,3))
    i+=1
print("")

#Nr. 5
i=0
while i <= 10:
    print(quad_func(i))
    i+=1
print("")

# Nr. 6
print(quad_func(10, 5))
print(quad_func(10, c=5))
print("")

# Nr. 7
parameter=(2,3,4)
print(quad_func(10, *parameter))
print("")

#Nr. 8
param={'b':2, 'c':1, 'a':5}
print(quad_func(10, **param))
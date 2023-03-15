#Aufg 1. 

for n in range(10, 0, -1):
    print(n)

print("---------")
n=10
while n >=1:
    print(n) 
    n-=1
print("--------------")
n=10
while 1: 
    print(n)
    n-=1

    if n<1:
        break


print("---Treppe---")
x=1
y=1
for x in range(1,10):
    for y in range(0,x):
        print(x, end="")
    x+=1
    y=1
    print("")
print("")
print("---Andere Treppe---")
for x in range(1,10):
    print(str(x)*x)
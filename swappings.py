print("Using Temp")
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a,b)
print("Using ,")
a=int(input())
b=int(input())
a,b=b,a
print(a,b)
print("Using + and -")
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a,b)
print("Using ^")
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a,b)

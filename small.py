n = int(input("Enter the no. of elements: "))
num = []

for i in range(n):
    x = int(input("Enter the element: "))
    num.append(x)
    small = num[0]

for i in range(1, n):
    if num[i] < small:
        small = num[i]

print("smallest no =", small)

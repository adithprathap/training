n = int(input("Enter the no. of elements: "))
num = []

for i in range(n):
    x = int(input("Enter the element: "))
    num.append(x)

large = num[0]

for i in range(1, n):
    if num[i] > large:
        large = num[i]

print("Largest no =", large)

n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    a.append(int(input("Enter element: ")))
a = list(set(a))
print("After removing duplicates:", a)

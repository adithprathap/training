n = int(input("Enter the no.of elements:"))
a = []
for i in range(n):
    num = int(input("Enter the number:"))
    a.append(num)
search = int(input("Enter element to count:"))
count = 0
for i in range(n):
    if a[i] == search:
        count = count + 1
print("Occurrence:", count)

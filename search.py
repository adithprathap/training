n=int(input("enter the limit"))
num=[]
for i in range(n):
    x = int(input("Enter the element: "))
    num.append(x)
print(num)
s=int(input("enter the number to be searched"))
if s in num:
  print("element found")
else:
  print("not found")

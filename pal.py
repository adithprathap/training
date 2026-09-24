x=int(input("enter the number"))
rev=0
dup=x
while x>0:
  r=x%10
  rev=rev*10+r
  x=x//10
if(dup==rev):
  print("is palindrome")
else:
  print("not palindrome")


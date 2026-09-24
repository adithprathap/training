str= input("Enter a string: ")
s = ""
for char in str:
    if char not in s:
       s = s + char
print("Without duplicates:",s)

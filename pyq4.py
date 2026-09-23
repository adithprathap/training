#Given the number of rats r, the amount of food each rat consumes unit, and an array arr representing the amount of food present in each house, find the minimum number of houses required to feed all the rats.

Constraints

r and unit are positive integers.
arr is a positive integer array of size n.
0 <= i, where i is the index of the array arr.
If the array is null, return -1.
If the total amount of food from all houses is not sufficient for all the rats, return 0.
Example

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2
Output: 4



r=int(input("Enter the no of rats:"))
u=int(input("Enter the no of units:"))
arr=[]
n=int(input("enter the no of elements:"))
arr=list(map(int, input("Enter the elements: ").split()))
sum=0
h=0
for i in range(0,n):
  sum=sum + arr[i]
  h+=1
  if(sum >= r*u):
    break;
print("output=",h)

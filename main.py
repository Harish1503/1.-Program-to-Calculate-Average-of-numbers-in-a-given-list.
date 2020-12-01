# Python Program to Calculate the Average of Number in a given List

n = int(input("Enter the total number of elements:"))
a = []
for i in range(0,n):
  element = int(input())
  a.append(element)
total = sum(a)
average = total / n
print(average)
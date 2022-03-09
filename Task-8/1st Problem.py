import numpy as np

array = []
n = int(input("Enter number of elements in array : "))
for i in range(0, n):
    ele = int(input())
    array.append(ele)
print("Original array:")
print(array)
p = 5
New_array = np.zeros(len(array) + (len(array)-1) * (p))
New_array[::p+1] = array
print("\nModified array:")
print(New_array)


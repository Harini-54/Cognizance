import numpy as np
array1 = []
n = int(input("Enter number of elements for 1st array : "))
for i in range(0, n):
    ele = int(input())
    array1.append(ele)
array2 = []
n = int(input("Enter number of elements for 2nd array: "))
for i in range(0, n):
    ele = int(input())
    array2.append(ele)
print(np.array_equal(array1,array2))

import pandas as pd
array = []
n = int(input("Enter number of elements in array : "))
for i in range(0, n):
    ele = str(input())
    array.append(ele)
Series = pd.Series(array)
New_series = Series.str.capitalize()
print("The modified series:")
print(New_series )

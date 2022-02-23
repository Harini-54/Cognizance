
x = []
n = int(input("Enter number of rows : "))
print("Enter the roll number , name and marks respectively to output a data table")
for i in range(0, n):
    ele = [input(), input(),input()]
    x.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for i in range(3):
    print(x[1][i], end=" "*10)

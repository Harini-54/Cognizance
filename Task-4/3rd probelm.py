#This program is for outputting the given data in n(collected from user) rows and 3 columns
x= []
n = int(input("Enter number of rows : "))
print("Enter the data to output it as a table")
for i in range(0, n):
    ele = [input(), input(),input()]
    x.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for a in x:
    for b in a:
        print(b,end=" "*10)
    print()




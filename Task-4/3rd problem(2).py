x = [ [1, 'Mahesh', 97],
     [2, 'Sweety', 77],
     [3, 'Harini', 87]]
print("{:<10} {:<10} {:<10} ".format('Roll no.', 'Name',  'Marks'))
for i in range(3):
    print(x[0][i], end=" "*10)
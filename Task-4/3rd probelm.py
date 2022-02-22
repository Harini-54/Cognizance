x = [ [1, 'Mahesh', 97],
     [2, 'Sweety', 77],
     [3, 'Harini', 87]]
print("{:<10} {:<10} {:<10} ".format('Roll no.', 'Name',  'Marks'))
                   #format is used like header(what has to be in 1st row)
for a in x:        #a represents the vertical manner
    for b in a:    #b represents the columns
        print(b,end=" "*10)
    print()




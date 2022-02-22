x =int (input("Enter a number:"))
a = x
rev=0
while(x > 0):
    dig = x % 10
    rev = rev*10+dig
    x = x//10
if(a==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
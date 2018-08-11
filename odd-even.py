#check the given integer is odd or even number

n = int(input("Enter the any integer value: "))

if(n>0):
    if(n%2==0):
        print("%d is even number "%(n))
    else:
        print("%d is odd number "%(n))
else:
    print("invalid input")

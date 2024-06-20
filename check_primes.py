def is_prime(number):
    if number==0 or number==1:
        return True
    flag=False
    for i in range(2,(number//2)+1):
        if number%i==0:
            flag=True
            break
    return flag
number=int(input("enter the number"))
x=is_prime(number)
if x:
    print("given numbers is not prime")
else:
    print("given numbers is prime")

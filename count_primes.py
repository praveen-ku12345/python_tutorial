def is_prime(i):
    if i<2:
        return False
    for j in range(2,(i//2)+1):
        if i%j==0:
            return False
    return True
def count_primes(numbers):
    count=0
    for i in numbers:
        if is_prime(i):
            count+=1
    return count
numbers=list(map(int,input("enter the numbers separeted by the space :").split()))
x=count_primes(numbers)
print(x)
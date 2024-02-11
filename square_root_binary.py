def square_root(number,epsilon=1e-6):
    if number<0:
        raise ValueError("can't possible for negative numbers :")
    if number==0 or number==1:
        return number
    left=0
    right=number
    result=1.0
    while abs(result*result-number)>epsilon:
        mid=(left+right)/2
        if mid*mid==number:
            return mid
        elif mid*mid<number:
            left=mid
        else:
            right=mid
        result=mid
    return result
number=int(input("enter the number :"))
x=round(square_root(number),2)
print(x)
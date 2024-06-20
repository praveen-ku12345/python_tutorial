def binary_search(numbers,target):
    result=-1
    n=len(numbers)
    low=0
    high=n-1
    mid=(low+high)//2
    while(low<=high):
        if numbers[mid]==target:
            return numbers[mid+1]
        elif numbers[mid]<target:
            result=numbers[mid]
            low=mid+1
        else:
            high=mid-1
        mid=(low+high)//2
    return result
numbers=list(map(int,input("enter the numbers separeted by the comma :").split(",")))
target=int(input("enetr the target element"))
x=binary
_search(numbers,target)
print(x)
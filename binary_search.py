def binary_search(numbers,target):
    n=len(numbers)
    low=0
    high=n-1
    mid=(low+high)//2
    while(low<=high):
        if numbers[mid]==target:
            return mid
        elif numbers[mid]>target:
            high=mid-1
        else:
            low=mid+1
        mid=(low+high)//2
    return -1
numbers=list(map(int,input("enter the numbers separeted by the comma :").split(",")))
target=int(input("enetr the target element"))
x=binary_search(numbers,target)
if x!=-1:
    print(f"element is presant at {x} location")
else:
    print("element is not present:")
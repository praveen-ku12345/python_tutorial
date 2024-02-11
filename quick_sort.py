def partition(numbers,low,high):
    pivot=numbers[low]
    lb=low+1
    ub=high
    while True:
        while lb<=ub and pivot>numbers[lb]:
            lb=lb+1
        while lb<=ub and pivot<numbers[ub]:
            ub=ub-1
        if lb<=ub:
            numbers[ub],numbers[lb]=numbers[lb],numbers[ub]
        else:
            break
    numbers[low],numbers[ub]=numbers[ub],numbers[low]                                                             
    return ub
def quick_sort(numbers,low,high):
    if low<high:
        p=partition(numbers,low,high)
        quick_sort(numbers,low,p-1)
        quick_sort(numbers,p+1,high)
numbers=list(map(int,input("enter the numbers separeted by space :").split()))
n=len(numbers)
quick_sort(numbers,0,n-1)
print(numbers)
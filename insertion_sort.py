def insertion_sort(numbers):
    n=len(numbers)
    for i in range(1,n):
        temp=numbers[i]
        j=i-1
        while j>=0 and numbers[j]>temp:
            numbers[j+1]=numbers[j]
            j=j-1
        numbers[j+1]=temp
numbers=list(map(int,input("enter the numbers separeted by space:").split()))
insertion_sort(numbers)
print(numbers)

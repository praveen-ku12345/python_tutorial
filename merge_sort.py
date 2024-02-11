def merge_sort(numbers):
    if len(numbers)>1:
        n=len(numbers)
        mid=n//2
        left_half=numbers[:mid]
        right_half=numbers[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=j=k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<=right_half[j]:
                numbers[k]=left_half[i]
                i=i+1
            else:
                numbers[k]=right_half[j]
                j=j+1
            k=k+1
        while i<len(left_half):
            numbers[k]=left_half[i]
            i=i+1
            k=k+1
        while j<len(right_half):
            numbers[k]=right_half[j]
            j=j+1
            k=k+1
numbers=list(map(int,input("enter the numbers separeted by comma : ").split(",")))
merge_sort(numbers)
print(numbers)
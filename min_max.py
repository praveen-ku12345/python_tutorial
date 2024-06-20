def min_max(numbers):
    if not numbers:
        return None,None
    n=len(numbers)
    if n%2==0:
        if numbers[0]<numbers[1]:
            min_value=numbers[0]
            max_value=numbers[1]
        else:
            min_value=numbers[1]
            max_value=numbers[0]
        start_index=2
    else:
        min_value,max_value=numbers[0]
        start_index=1
    for i in range(start_index,n-1,2):
        if numbers[i]<numbers[i+1]:
            min_value=min(min_value,numbers[i])
            max_value=max(max_value,numbers[i+1])
        else:
            min_value=min(min_value,numbers[i+1])
            max_value=max(max_value,numbers[i])
    return min_value,max_value
numbers=list(map(int,input("enter the elements:").split()))
min_value,max_value=min_max(numbers)
print(f"minimum value={min_value} \nmaximum value={max_value}")
def max_subarray_sum(numbers):
    current_sum=max_sum=numbers[0]
    for i in numbers[1:]:
        current_sum=max(current_sum,i+current_sum)
        max_sum=max(current_sum,max_sum)
    return max_sum
numbers=list(map(int,input("entre the values :").split()))
result=max_subarray_sum(numbers)
print(f"{result}")
# from collections import Counter
# def counting_sort(arr):
#     count = Counter(arr)
#     return [num for num, freq in sorted(count.items()) for _ in range(freq)]
# try:
#     input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
#     sorted_result = counting_sort(input_list)
#     print("Sorted Array:", sorted_result)
# except ValueError:
#     print("Please enter a valid list of integers.")
# from collections import Counter
# def counting_sort(numbers):
#     count=Counter(numbers)
#     return [i for i,j in sorted(count.items()) for k in range(j)]
# try:
#     numbers=list(map(int,input("enter the numbers separeted by space :").split()))
#     x=counting_sort(numbers)
#     print(x)
# except:
#     print("plaese enter only numbers:")

from collections import Counter
def counting_sort(numbers):
    count=Counter(numbers)
    return [i for i,j in sorted(count.items()) for k in range(j)]
try:
    numbers=list(map(int,input("enter the numbers separeted by the space :").split()))
    result=counting_sort(numbers)
    print(result)
except:
    print("enter the only numbers ")
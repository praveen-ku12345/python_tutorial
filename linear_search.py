def linear_search(numbers,target):
    for i in range(len(numbers)-1):
        if numbers[i]==target:
            return i
    return -1
numbers=list(map(int,input("enter the numbers separeted by the space: ").split()))
target=int(input("enter the target elemnt :"))
x=linear_search(numbers,target)
if x!=-1:
    print(f"elemnt is presant at {x} position:")
else:
    print("element is not present")
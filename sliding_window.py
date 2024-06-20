def sliding_window(numbers,k):
    n=len(numbers)
    if k>n:
        return "Invalid Input"
    current_sum=0
    max_sum=float('-inf')
    for i in range(k):
        current_sum+=numbers[i]
    for i in range(k,n):
        current_sum=current_sum+numbers[i]-numbers[i-k]
        max_sum=max(current_sum,numbers[i])
    return max_sum
numbers=list(map(int,input("enetr the elemnets separeted by the space :").split()))
k=int(input("enter the window size :"))
x=sliding_window(numbers,k)
print(x)
def three_sum(numbers,target):
    numbers.sort()
    result=[]
    for i in range(len(numbers)-2):
        low,middle,high=i+1,i+2,len(numbers)-1
        while middle<high:
            current_sum=numbers[i]+numbers[middle]+numbers[high]
            if current_sum==target:
                result.append([numbers[i],numbers[middle],numbers[high]])
                middle+=1
                high-=1
            elif current_sum<target:
                middle=middle+1
            else:
                high-=1
    return result
numbers=list(map(int,input("enter the numbers separated by space :").split()))
target=int(input("enter the target element"))
x=three_sum(numbers,target)
print(x)
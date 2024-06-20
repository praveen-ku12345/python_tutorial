def container_with_most_water(numbers):
    left=0
    right=len(numbers)-1
    max_area=0
    while left<right:
        h=min(numbers[left],numbers[right])
        w=right-left
        current_area=h*w
        max_area=max(max_area,current_area)
        if numbers[left]<numbers[right]:
            left+=1
        else:
            right-=1
    return max_area
numbers=list(map(int,input("enter the numbers separeted by space :").split()))
x=container_with_most_water(numbers)
print(x)
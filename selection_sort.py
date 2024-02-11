def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index=i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[min_index]:
                min_index=j
        numbers[min_index],numbers[i]=numbers[i],numbers[min_index]
numbers=list(map(int,input("enetr the numbers separeted by space :").split()))
selection_sort(numbers)
print(numbers)
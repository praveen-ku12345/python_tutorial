def merge_sorted_array(numbers1,numbers2):
    i=0
    j=0
    merged_array=[]
    while i<len(numbers1) and j<len(numbers2):
        if numbers1[i]<numbers2[j]:
            merged_array.append(numbers1[i])
            i=i+1
        else:
            merged_array.append(numbers2[j])
            j=j+1
    while i<len(numbers1):
        merged_array.append(numbers1[i])
        i+=1
    while j<len(numbers2):
        merged_array.append(numbers2[j])
        j+=1
    return merged_array
numbers1=list(map(int,input("enter the numbers separeted by the space of 1st array :").split()))
numbers2=list(map(int,input("enetr the elments of second array :").split()))
x=merge_sorted_array(numbers1,numbers2)
print(x)
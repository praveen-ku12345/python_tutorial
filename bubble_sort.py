def bubble_sort(k):
    n=len(k)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if k[j]>k[j+1]:
                k[j],k[j+1]=k[j+1],k[j]
k=list(map(int,input().split()))
bubble_sort(k)
print(k)
def array_rotation(numbers,k):
    n=len(numbers)
    located=k%n
    if k>n:
        return "cannot rotate as the size of array less then rotate size"
    array=[]
    array=numbers[located:]+numbers[:located]
    return array
numbers=list(map(int,input('enter the numbers separeted by the space :').split()))
k=int(input("enter the rotation size :"))
x=array_rotation(numbers,k)
print(x)
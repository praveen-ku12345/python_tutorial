# def greet(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)

# greet(name='Praveen',dept='cse',subject='oops')
# greet(name='vamshi',dept='ece')

def greet(*args,**kwargs):#args followed by kwargs
    for key,value in kwargs.items():
        print(key,value)
    print(args)
    c=0
    for i in args:
        c=c+i
    print(f"sum is {c}")

greet(1,2,3,4,5,name='Praveen',dept='cse',subject='oops')
greet(1,2,3,4,5,6,67,name='vamshi',dept='ece')
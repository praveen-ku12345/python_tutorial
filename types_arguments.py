# def greet(name,dept):
#     print(f"hello {name}")
#     print(f"are you belongs to {dept} department")
# greet("Praveen","cse")                           #positional arguments

# def greet1(name1,dept1):
#     print(f"helllo {name1}")
#     print(f"hello {dept1}")
# greet1(dept1="heelo sru",name1='u')               #keyword arguments.order does not matter

# def greet2(name2,dept):
#     print(f"hello {name2}")
#     print(f"hello {dept}")
# greet2("praveen",dept="cse")#combination of positional and keyword arguments.positional followed by keyword arguments.

# def greet3(name3,subject,dept="cse"):#default argument.always positional arguments followed by default argument
#     print(f"hello {name3}")
#     print(f"do u like {subject}")
#     print(f"hello {dept}")
# greet3("praveen","python")

# def greet4(name3,subject,dept="cse"):#overrides
#     print(f"hello {name3}")
#     print(f"do u like {subject}")
#     print(f"hello {dept}")
# greet4("praveen","python","sru")

# def add(a,b):
#     c=a+b
#     print(f"sum is  {c}")
# add(7,9)

def add(*args):#variable lenth argumnets
    c=0
    for i in args:
        c=c+i
    print(f"sum is {c}")
add(1,2,3,4,5,6,7,8)
add(3,2,5,667,5)
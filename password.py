import random
alphabets=['a','b','c','d','f','g']
digits=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
n_alphabets=int(input("enter the number of alphabets:\n"))
n_digits=int(input("enter the number of digits:\n"))
n_symbols=int(input("enter the  number of symbols you want:\n"))
password=""
for i in range(1,n_alphabets+1):
    password1=random.choice(alphabets)
    password+=password1
for i in range(1,n_digits+1):
    password1=random.choice(digits)
    password+=password1
for i in range(1,n_symbols+1):
    password1=random.choice(symbols)
    password+=password1
print(password)
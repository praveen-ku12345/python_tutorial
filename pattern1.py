# n=4
# ct1=1
# ct2=n*n+1
# 1*2*3*4*17*18*19*20
#  5*6*7*14*15*16
#    8*9*12*13
#     10*11
n=int(input())
ct1=1
ct2=n*n+1
for i in range(n,0,-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print(ct1,'*',sep='',end='')
        ct1+=1
    for j in range(i-1):
        print(ct2,'*',sep='',end='')
        ct2+=1
    print(ct2)
    ct2=ct2-2*(i-1)
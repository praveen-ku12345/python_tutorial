def lps(input_string):
    n=len(input_string)
    dp=[[False]*n for i in range(n)]
    for i in range(n):
        dp[i][i]=True
    start=0
    max_length=1
    for i in range(n-1):
        if input_string[i]==input_string[i+1]:
            dp[i][i+1]=True
            start=i
            max_length=2
    for k in range(3,n+1):
        for i in range(n-k+1):
            j=i+k-1
            if dp[i+1][j-1] and input_string[i]==input_string[j]:
                dp[i][j]=True
                start=i
                max_length=k
    return input_string[start:start+max_length]
input_string=input("enter the string :")
result=lps(input_string)
print(result)
print(len(result))

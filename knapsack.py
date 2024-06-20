def knapsack_problem(weights,profits,capacity):
    n=len(weights)
    dp=[[0 for i in range(capacity+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(dp[i-1][w],profits[i-1]+dp[i-1][w-weights[i-1]])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
weights=list(map(int,input("enter the wieghts for knapsack :").split()))
profits=list(map(int,input("enter the weights :").split()))
capacity=int(input("enter the capacity :"))
result=knapsack_problem(weights,profits,capacity)
print(f"maximum profit is {result}")
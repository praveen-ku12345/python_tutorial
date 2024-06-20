n = 4
num = 1

for i in range(n):
    # Print leading spaces
    for j in range(i):
        print("  ", end="")
    # Print numbers with '*' separator
    for k in range(n - i):
        if k == n - i - 1:
            print(num, end="")
        else:
            print(num, end="*")
        num += 1
    # Move to the next line
    print("*")

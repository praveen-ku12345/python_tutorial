def isMagicSquare(matrix):
    target_sum = sum(matrix[0])
    # Check rows
    if any(sum(row) != target_sum for row in matrix):
        return False
    # Check columns
    if any(sum(col) != target_sum for col in zip(*matrix)):
        return False
    # Check diagonals
    if sum(matrix[i][i] for i in range(3)) != target_sum or sum(matrix[i][2 - i] for i in range(3)) != target_sum:
        return False
    return True
# Dynamically take input from the user for a 3x3 matrix
matrix = []
print("Enter the elements of the 3x3 matrix:")
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)
if isMagicSquare(matrix):
    print("The given matrix forms a magic square.")
else:
    print("The given matrix does not form a magic square.")
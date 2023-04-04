# CS T09 Compulsory Task 1
# This solution for this task shows example of a nested 'for' loop e.g. for loop inside another for loop.

# number of rows = 5, so outer loop will execute five times.
rows = 5

# outer loop
# For each iteration the outer, the column gets incremented by 1.
for i in range(1, rows + 1):
    # inner loop is the total number of column in each row.
    for j in range(1, i + 1):
        print("*", end="")
    print('')

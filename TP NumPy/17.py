import random

rows = 3
cols = 4

matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

for row in matrix:
    print(row)
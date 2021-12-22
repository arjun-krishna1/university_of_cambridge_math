import numpy as np

# row 1, col1 , col2, , col3, col4
B = np.array([28, 0, 30, 23, 22])

A = np.array([
  [2, 2, 0,0,0],
  [1, 0, 1, 2, -1],
  [1, 3, 0, 0, 0],
  [0, 1, 1, 2, 0],
  [1, 1, 0, 2, 0]
])

res = np.linalg.solve(A, B)

print(" tr, sq, he, ci, ?")
print(res)

B_expected = np.matmul(A, res)

print("\nshould be the same")
print(B)
print(B_expected)

import numpy as np

'''
https://nrich.maths.org/1053

I turned this into a Linear Algebra problem
I made each shape a variable
They were added together to give the resulting value for each row and column
  i.e. a system of linear equations
  
There are 5 variables, the value of each shape and the question mark

I needed 5 equations, I chose row 1 and all of the columns

A*res = B

We know A and B so we can use numpy to solve for res using the
numpy linear algebra solver
'''

# the constants for each equation
B = np.array([28, 0, 30, 23, 22])

# the coefficient matrix for the system of equations
A = np.array([
  [2, 2, 0,0,0],
  [1, 0, 1, 2, -1],
  [1, 3, 0, 0, 0],
  [0, 1, 1, 2, 0],
  [1, 1, 0, 2, 0]
])

# solving for the result
res = np.linalg.solve(A, B)

# displaying the results
print(" tr, sq, he, ci, ?")
print(res)

# verifying res:
B_expected = np.matmul(A, res)

print("\nshould be the same")
print(B)
print(B_expected)

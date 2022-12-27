from utils import *

A = A_star(start, end, 0)
print(A)
B = A_star(end, start, A)
print(B)
C = A_star(start, end, B)
print(C)

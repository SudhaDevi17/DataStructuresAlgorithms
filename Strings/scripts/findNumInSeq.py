import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
N = int(input())
num = 0
if not N:
    print(N)
    pass
while num < N:

    if '2' in str(num) or '14' in str(num):
        num += 1
        N += 1
    num += 1
print(num)

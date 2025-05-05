#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input().strip())
    print("n:", n)
    binary_rep = bin(n)[2:]
    print("n to Binary:", binary_rep)
    consecutive_ones = binary_rep.split('0')
    print("consecutive_ones:", consecutive_ones)
    max_ones = max(len(group) for group in consecutive_ones)
    print(max_ones)


# Sample Input 1
# 5
# Sample Output 1
# 1
# Sample Input 2
# 13
# Sample Output 2
# 2

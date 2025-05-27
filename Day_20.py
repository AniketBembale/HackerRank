#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    total_swaps = 0
    
    for i in range(n):
        number_of_swaps = 0

        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                number_of_swaps += 1
                total_swaps += 1
        
        if number_of_swaps == 0:
            break

    print(f"Array is sorted in {total_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


# Sample Input 0
# 3
# 1 2 3
# Sample Output 0

# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3
# Explanation 0

# The array is already sorted, so 0 swaps take place and we print the necessary 3 lines of output shown above.

# Sample Input 1
# 3
# 3 2 1
# Sample Output 1

# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3


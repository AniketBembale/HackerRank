#HourGlass Calculation
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    max_sum = None

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_sum = top + mid + bot
            if max_sum is None:
                max_sum = hourglass_sum
            else:
                max_sum = max(max_sum, hourglass_sum)
                
    print(max_sum)

#Inputs
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
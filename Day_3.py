#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0:
        print("Weird")
    elif N in range(2, 5) and N % 2 == 0:
        print("Not Weird")
    elif N in range(6, 21) and N % 2 == 0:
        print("Weird")
    elif N >= 20 and N % 2 == 0:
        print("Not Weird")


# Inputs
# 3
# 24

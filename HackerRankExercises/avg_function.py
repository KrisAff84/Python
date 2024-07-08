#!/bin/python

import math
import os
import random
import re
import sys


def avg(*nums):
    return sum(nums) / len(nums)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    average = avg(*nums)
    print(f'{average:.2f}')
    
    # fptr.write('%.2f' % average + '\n')

    # fptr.close()
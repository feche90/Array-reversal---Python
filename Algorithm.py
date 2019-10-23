#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a):
    l=len(a)
    cont=l
    new_arr=[]
    for i in range(l):
        new_arr.append(a[cont-1])
        cont-=1
    return (new_arr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

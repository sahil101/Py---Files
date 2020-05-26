import math
import os
import random
import re
import sys


# Complete the cutTheSticks function below.

def cutting(arr,a):
    list1 = []
    for i in arr:
        i = i-a
        if(i != 0):
            list1.append(i)
    return list1
def cutTheSticks(arr):
    a = min(arr)
    list1 = []
    if len(arr) == 0:
        return list1
    list1.append(len(arr))
    arr = cutting(arr,a)
    if len(arr) == 0:
        return list1
    cutTheSticks(arr)





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
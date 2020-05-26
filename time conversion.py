#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    str5 = s.split(":")
    str1 = str5[2][0:2]
    str2 = str5[2][2:4]
    if str2 == 'PM':
        str5[0] = int(str5[0]) + 12
        print("{0}:{1}:{2}".format(str5[0], str5[1], str1))
        str3 = str(str5[0])+":"+str5[1] +":"+str1
        return str3
    if str2 == 'AM':
        if str5[0] == "12":
            str5[0] = "00"
        print("{0}:{1}:{2}".format(str5[0],str5[1],str5[2]))
        str3 = str5[0]+":"+str5[1] +":"+str5[2]
        return str3

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # f.write(result + '\n')
    #
    # f.close()

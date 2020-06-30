# This was my solution submitted and passed all the test cases
'''
@Author: Ashutosh Srivastava
Python3 solution
'''

import math

def solution(area):
    res = []
    solarCalc(area, res)
    res.reverse()
    return res

def solarCalc(area, res):
    pArea = 0;
    if (area >= 1 and area <= 1000000):
        tmp = int(math.sqrt(area))
        if (tmp <= 0):
            return pArea
        else:
            pArea = int(math.pow(tmp, 2))
            nArea = area - pArea
            solarCalc(nArea, res)
            res.append(pArea)
        return (pArea)

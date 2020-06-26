# This was my solution submitted and passed all the test cases
'''
Author: Ashutosh Srivastava
Python3 solution
'''

def sorting(li):
    return(sorted(li, key=lambda li:[int(i) for i in li.split('.')]))

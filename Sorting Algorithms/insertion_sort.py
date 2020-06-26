'''
Author: Ashutosh Srivastava
Python3 solution
'''

def insert_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        prev=i-1
        while (prev>=0 and key>arr[prev]):   #while (prev>=0 and key<arr[prev]) <-- ascending condition
            arr[prev+1]=arr[prev]
            prev-=1
        arr[prev+1]=key
    print(arr)
data=[0,1,2,3,4,5,6,7]
insert_sort(data)

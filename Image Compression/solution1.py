'''
Author: Ashutosh Srivastava
Python3 solution
'''

import tinify
tinify.key = '<your key here>'
tinify.from_file('/root/Desktop/amber.jpg').to_file('optimized.jpg')

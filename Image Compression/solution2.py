'''
Author: Ashutosh Srivastava
Python3 solution
'''

from PIL import Image
image = Image.open('/root/Desktop/amber.jpg')
newImage = image.resize((300, 300))
newImage.save('new.jpg')

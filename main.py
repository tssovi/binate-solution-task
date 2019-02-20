import os
from function import ReadFile

file_path = 'textfile/images.txt'
img_path = 'image/'

if not os.path.exists(img_path):
    os.makedirs(img_path)

url_dict = ReadFile(file_path, img_path)

print('\nValid URL found:', url_dict['valid'])
print('\nInvalid URL found:', url_dict['invalid'])


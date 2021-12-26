'''
@author: Shivam Mishra
@date: 23-12-21 10:57 PM
'''
import json

with open('sample2.json') as json_file:
    read_file = json.load(json_file)
print(read_file)
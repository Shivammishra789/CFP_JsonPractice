'''
@author: Shivam Mishra
@date: 23-12-21 10:57 PM
'''
import json

with open('sample2.json') as json_file:
    ss = json.load(json_file)
print(ss)
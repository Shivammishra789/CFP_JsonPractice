'''
@author: Shivam Mishra
@date: 26-12-21 7:59 PM
'''

import json

person = {}

person["leo"] = {'name': 'leo',
                 'address': 'Harayana',
                 'email': None,
                 'phoneNo': '8974512456',
                 'married': False
                 }
person["tim"] = {'name': 'tim',
                 'address': 'Delhi',
                 'email': 'tim@gmail.com',
                 'phoneNo': '8974512456',
                 'married': True
                 }

print(person)
print(type(person))


person_details = json.dumps(person, indent=4)
print(person_details)
print(type(person_details))

with open("person_details.json","w") as json_file:
    json.dump(person_details)

'''
Created on Jun 18, 2020

@author: basedul
'''
import json
import os
import shutil
from warnings import catch_warnings
# 01738202226
if __name__ == '__main__':
    
    m = str(raw_input("Enter Meta.json file path "))
#     print(m)
    with open(m) as f:
        data = json.load(f)
#     print(data['classes'])
#     for meta in data['classes']:
#         directory = "./Images/"+meta['title']
#         if not os.path.exists(directory):
#             os.makedirs(directory)
     
 
#     s = '/home/basedul/Downloads/Medical_mask/Medical_Mask/annotations'
#     s1 = "/home/basedul/Downloads/Medical_mask/Medical_Mask/image/"
    s = str(raw_input("Enter annotations folder path "))
    s1 = str(raw_input("Enter images folder path "))+"/"
    for files in os.listdir(s):
#       print(s+"/"+files)
        file_path = s+"/"+files
        with open(file_path) as fol:
            fol_data = json.load(fol)    
            for first in fol_data['Annotations']:
#                 print(fol_data['FileName'])
#                 print(first['classname'])
                for meta in data['classes']:
                    if meta['title'] == first['classname']:
                        directory = "./Images/"+meta['title']
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        try:
                            shutil.copy(s1+fol_data['FileName'], "./Images/"+meta['title']+"/"+fol_data['FileName'])
                        except:
                            pass
    print("Done!")
#     person = '{"name": "Bob", "languages": ["English", "Fench"]}'
#     person_dict = json.loads(person)
# 
#     # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#     print( person_dict)
# 
#     # Output: ['English', 'French']
#     print(person_dict['languages'])


#     pass
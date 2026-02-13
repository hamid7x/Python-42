# here u have access to everthing inside my_module
import my_modules as mm
# here u only imported find_index, test functions
from my_modules import find_index, test

# some python standard modules (librray)
import random
import math
import datetime
import calendar
import os


import sys
# enforce sys to add a new path so i can import modules not in my working directory
sys.path.append('/home/houkaamo/common_core/My-Modules')
import module


courses = ['History', 'Math', 'Physics', 'CompSci']


index = mm.find_index(courses, 'Physics')
print(index)
print(mm.test)


print(find_index(courses, 'CompSci'))
print(test)

# this print all path that we can import our module from
print(sys.path)
'''
['/home/houkaamo/common_core/github_projects/Python-42/python', 
'/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', 
'/home/houkaamo/.local/lib/python3.10/site-packages', 
'/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
'''


# now u can see the new path we add
print(sys.path)
'''
['/home/houkaamo/common_core/github_projects/Python-42/python',
'/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload',
'/home/houkaamo/.local/lib/python3.10/site-packages', '/usr/local/lib/python3.10/dist-packages',
'/usr/lib/python3/dist-packages', '/home/houkaamo/common_core/My-Modules']
'''
print(module.my_name)


print(random.choice(courses))
print(math.radians(90))
print(datetime.datetime.today())
print(calendar.isleap(2017))
print(calendar.isleap(2020))
print(os.getcwd())


# to print the location of the module file
print(os.__file__)

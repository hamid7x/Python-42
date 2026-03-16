# ------------------------
# --- File Handling ------
# ------------------------
# "a" Append Open file for appending values, create file if not exists
# "r" Read [Default Value] Open file for read and give error if file is not Exists
#  "w" Write Open file for creating, create file if not exists
# "x" Create Create file, give error if file not exists


# absolute path : start from root home
# relative path: start at current working directory

import os

# current wroking directory
print(os.getcwd())

# absolute path of the current file am wroking with
print(os.path.abspath(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

print()

myfile = open('file.txt')

print(myfile)
print(myfile.name)
print(myfile.mode)
print(myfile.encoding)


# print(myfile.read())
# print(myfile.read(5))
# print(myfile.readline())
# print(myfile.readlines())

# for line in myfile:
#     print(line)
#     if line.startswith('3'):
#         break

print(myfile.tell())
myfile.seek(11)

os.remove('file.txt')
# always close file
myfile.close()

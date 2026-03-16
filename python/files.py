import sys

"""
'r'  # read — open existing file to read
     # raises FileNotFoundError if file doesn't exist

'w'  # write — create new file or OVERWRITE existing one
     # dangerous! existing content is deleted

'a'  # append — add to end of existing file
     # creates file if it doesn't exist

'r+' # read AND write — file must exist
"""


f = open('file.txt', 'r')
content = f.read()
print(content)
f.close()

# this will remove the old contenet of file and replace it with this
f = open('file.txt', 'r+')
f.write('hello this is new text will added to file')
print(f.read())



""" Streams """
print('normal data')

sys.stderr.write('ERROR: file not found\n')
sys.stderr.flush()
data = sys.stdin.read()

print(data)

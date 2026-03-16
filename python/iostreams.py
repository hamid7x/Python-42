import sys, time
import os
# sys.stdout.write('hello world')
# sys.stderr.write('this is an error')

# print('this also is an error')

# content = sys.stdin.read()
# print(content)

def progress_bar(total):
    sys.stdout.write('[')
    sys.stdout.flush()
    for i in range(total):
        time.sleep(0.1)
        sys.stdout.write("#")
        sys.stdout.flush()
    sys.stdout.write(']')
    sys.stdout.flush()

i = 3
while True:
    i -= 1
    progress_bar(50)
    os.system('clear')
    if i == 0:
        break
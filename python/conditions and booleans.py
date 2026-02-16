# Comparisons
# Equal:           ==
# NOt Equal:       !=
# Object Identity: is

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

# the difference between == and is :
# == : checking values if they are equall
# is : checking is they are same object in memmory

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (they are have equal values)
print(a is b)  # False (but they are not same in memory)
print(a is c)  # True (same object in memmory)
# we can check their id's :
# u can see that a and c have same id, but has diffrent id
print(id(a))  # 139794029649408
print(id(b))  # 139794029727488
print(id(c))  # 139794029649408

# Booleans comparisons
# and
# or
# not

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')


# falsy values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. for example: '', (), [].
    # Any empty mapping, for example: {}.

condition = False  # None, 0, (), [], {}
# all this will considers as False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

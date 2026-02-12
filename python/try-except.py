# not safe if user enter string or any non number input
age = int(input('Enter your age: '))

print(age)

# safe version is try/except

# simple try/except (now this except catch all exception)
try:
    age_1 = int(input('Enter your age: '))
    print('You are', age_1)
except:
    print('Please enter a valid number!')

# more professional way to use try/except
# is to specifiy with exception you want to catch

try:
    age_2 = int(input('Enter you age: '))
    print('You age ', age_2)
except ValueError:
    print("That's not a number!")

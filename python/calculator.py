'''
here i learn why we use if __name__ == __main__
'''


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


'''
when call calcualtor.py  can see that __name__ is __main__
but when call program.py _name__ is program
so add this this if __name__ == __main__
to say that only run this code if the call from the main program
otherwise u can use add and subtract form another module but u can't
run what under __main__ only from main function
'''
print(__name__)

if __name__ == "__main__":
    print("This is simple calculator!")
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print(f"ADD: a + b = {add(num1, num2)}")
    print(f"SUBTRACT: a - b = {subtract(num1, num2)}")

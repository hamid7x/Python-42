"""
python have multiple error types
that's help the developer to identify
what exctly error hapned in program  and handle it
by displaying a helpeful message for the user about the error
"""
num = 1000
while num != 7:
    try:
        list = [1, 2, 3, 4, 5, 8]
        num = int(input('enter number: '))
        print(10 / num)
        print(list[num])
    except ValueError:
        print('ener a valid number ')
    except ZeroDivisionError:
        print("u can't dived by zero")
    except IndexError:
        print('this number is not in range of list ')


# i try to demonstry what happned when we raise an exception
def call_eror() -> None:
    if True:
        raise ValueError('invaid data', 'this second args', 12)


try:
    print('hi')
    call_eror()
except ValueError as e:
    print(e.args)
    print(e)


"""
__str__ is a special method in Python that gets called automatically
when you do print(object).
So __str__ controls what gets displayed when you print an object.
"""
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"My name is {self.name} and I am {self.age}"


p = Person('Bob', 30)
print(p)

class MyCustomException(Exception):
    pass

print(ValueError())
print(MyCustomException())


class BaseException:
    def __init__(self, *args):
        self.args = args  # stores everything u pass as a tuple
    
    def __str__(self):
        if len(self.args) == 0:
            return ''
        elif len(self.args) == 1:
            return str(self.args[0])  # returns clean string not tuple
        else:
            return str(self.args)  # returns full tuple as string


class Exception(BaseException):
    pass  # inherits everything from BaseException


class ValueError(Exception):
    pass  # inherits everything from Exception


class KeyError(Exception):
    pass  # inherits everything from Exception


"""
When you write ValueError('invalid data'):
1. Python looks for __init__ in ValueError — it only has pass so nothing there.
2. Python goes up the chain to Exception — also pass, nothing there.
3. Python goes up again to BaseException — found __init__! So it runs:
pythondef __init__(self, *args):
    self.args = ('invalid data',)  # stores your message
So pass just means — don't add anything new, just use
whatever the parent class has.
The message still gets stored because BaseException.__init__ handles it!
"""
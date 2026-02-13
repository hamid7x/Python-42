
def hello_func():
    return 'Hello Function!'


def greet_func(greeting, name='You'):
    return '{} Function.'.format(greeting)


print(greet_func('Hi', 'Jhon'))
print(hello_func().upper())


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Jhon', age=22)
courses = ['Math', 'Art']
info = {'name': 'Jhon', 'age': 22}
# without unpacking : studend_info consider courses, info as args
student_info(courses, info)
# unpacking
student_info(*courses, **info)

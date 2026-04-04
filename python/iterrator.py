my_list = ['jhon', 'bob', 35]

print(type(my_list))
my_iter = iter(my_list)
test = my_iter.__iter__()
print(type(test))
print(type(my_iter))
numbers = range(1, 5)
iter_numbers = numbers.__iter__()
iter_numbers = numbers.__iter__()
print(next(iter_numbers))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
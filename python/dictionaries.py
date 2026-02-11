student = {'name': 'Jhon', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])   # Jhon
print(student['courses'])   # ['Math', 'CompSci']
# print(student['phone'])   # KeyError: 'phone' (because this key not exit)

# use method get to return NULL if the key not exist instead throwing error
print(student.get('phone'))  # None
# costume message
print(student.get('phone', 'Not Found'))  # Not Found
print(student.get('age'))  # 25

student['name'] = 'Jane'   # update name student
student['phone'] = '5555-555-55'  # phone will add to student

# update multiple keys
student.update({'name': 'Hamid', 'age': 24})  # update takes object

# delele a key-value
del student['age']  # age will deleted
phone = student.pop('phone')  # also pop remove a and return the deleted value
print(phone)

print(student.keys())  # return dictionay keys
print(student.values())  # return dictionay value
print(student.items())  # return dictionay pair key-value

print(student)


# looping through keys
for key in student:
    print(key)

# looping through keys and values
for key, value in student.items():
    print(key, value)

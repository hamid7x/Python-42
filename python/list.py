# Mutable

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Edudcatoin', 'Languestic']
courses.append('Art')
courses.insert(0, 'Algebra')
courses.extend(courses_2)

courses.remove('Math')
courses.pop()
courses.reverse()
nums = [1, 5, 4, 2, 3]
nums.sort()
nums.sort(reverse=True)

sorted_courses = sorted(courses)

print(min(nums))
print(max(nums))
print((nums))
print(nums)
print(courses)
print(sorted_courses)

print(courses.index('Art'))
print('Art' in courses)
print('Math' in courses)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

print(' '.join(courses))


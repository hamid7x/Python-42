
courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
nums = {6, 5, 1, 2, 1, 3, 4, 5, 4}
print(nums)
print(courses)

art_courses = {'History', 'Design'}
print(courses.intersection(art_courses))
print(courses.difference(art_courses))
print(art_courses.difference(courses))
print(courses.union(art_courses))
print(art_courses.union(courses))


# Empty lists
empty_list = []
empty_list = list()

# Empty tupels
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {}  # this isn't right! it's as dictionnary
empty_set = set()  # this is the only method to create empty set

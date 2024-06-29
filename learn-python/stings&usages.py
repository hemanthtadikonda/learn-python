course = "Python for Beginners"
course1 = "Python's course for Beginners"
course2 = 'Python for "Beginners"'
course3 = '''
Hello Hemanth,

Here is a first mail for you.

Regards//Support Team.

'''
print(course)
print(course1)
print(course2)
print(course3)

####
course = "Python for Beginners"
another = course[:]

print(course [0])
print(course [-1])
print(course [-3])
print(course [0:3])
print(course [0:])
print(course [3:])
print(course [0:6])

print(another)


### formated strings

first = input("enter your first name: ")
last  = input("enter your last name: ")

message = first + ' ['+last+'] is a coder'
msg = f'{first} [{last}] is a coder'

print(message)
print(msg)

####
course = "Python for Beginners"

print(course)
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('o')) # ---> will help us to show index.

print(course.replace('Beginners', 'Absolute Beginners'))

print(course.replace('P','J'))




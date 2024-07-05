# a function is a block of organized, reusable code that is used to perform a single, related action.
def greet_user():
    print('Hi There !')
    print('Welcome to abroad')

print("start")
greet_user()
print("finish")

###
def greet_user(name):
    print(f'Hi {name} !')
    print('Welcome to abroad')


# greet_user() # you have to provide positional argument
greet_user("Hemanth")


greet_user(name="Hemanth") # it is Key word argument

####
def greet_user(first_name , last_name ):
    print(f'Hi {first_name} {last_name} !')
    print('Welcome to abroad')


# greet_user() # you have to provide positional argument
# greet_user("Hemanth" , "Tadikonda")

greet_user(last_name="Tadikonda", first_name ="Hemanth")

# greet_user(last_name="Tadikonda", "Hemanth") # SyntaxError: positional argument follows keyword argument

greet_user("Hemanth",last_name="Tadikonda")
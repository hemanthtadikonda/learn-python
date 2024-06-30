name = input('What is your name?:  ')

print('Hi ' + name )


###
name = input('what is your name?: ')
color = input('what is your favorite color?: ')

print(name + " likes "+color)

###
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)

print(age)

# int()
# float()
# bool()
# type -- will help us know data type
print(type(birth_year))
print(type(age))

# ###

weight_lbs = int(input("Enter your weight in lbs: "))
weight_kgs = weight_lbs * 0.45

print("Your weight is " ,weight_kgs , "kg's")

###

x=eval(input("Enter x= "))
print(x,type(x))




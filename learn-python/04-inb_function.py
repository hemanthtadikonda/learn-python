name = input('What is your name?:  ')

print('Hi ' + name )


###
name = input('what is your name?: ')
color = input('what is your favorite color?: ')

print(name,"likes",color)
print(name + " likes " + color )

###
name = input("Please enter your name: ")
birth_year = int(input("Enter your birth year: "))

age = 2024 - birth_year
print(name,"age is",age,"years now")

# int()
# float()
# bool()
# type -- will help us know data type
print(type(birth_year))
print(type(age))

# ###

weight_lbs = input("Enter Youe weight in Lbs: ")
weight_kgs = 0.45 * int(weight_lbs)

print("You are",weight_kgs,"Kgs")

###

x=eval(input("Enter x= "))
print(x,type(x))




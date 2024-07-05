def square(num):
    num * num
print(square(4))

# By default all functions return value is "None"
## if you need Return value of the that funtion
def square(num):
    return num * num


print(square(4))

# *** --- *** #
def emoji_converter(message):
    words = message.split(' ')
    emoji_converter = {
        ":)": "😁" ,
        ":(": "😥" ,
        "::" : "🤔"
    }
    output = ''

    for word in words:
        output += emoji_converter.get(word, word) + " "

    return output

message = input("> ")
# result = emoji_converter(message)
# print(result)
print(emoji_converter(message))

# *** --- *** # Exceptions # *** --- *** #
# age = int(input("Age: "))
# print(age)

# if you provide string input it will fail

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Please enter vaild Number")

try:
    age = int(input("Age: "))
    income = 20000
    risk = 20000 / age
    print(risk)
except ValueError:
    print("Please enter vaild Number")
except ZeroDivisionError:
    print("Invalid value")


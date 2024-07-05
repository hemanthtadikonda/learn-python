customer = {
    "name": "Hemanth" ,
    "birth_year": 1997 ,
    "is_valid": True ,
}

print(customer["birth_year"])

# print(customer["dob"])
print(customer.get("dob"))
print(customer.get("dob", "Jan 1 1997"))

customer["gender"] = "Male"

print(customer)
print(customer["gender"])

####

phone = input("Phone: ")

digit_mapping = {
    "1": "One" ,
    "2": "Two" ,
    "3": "Three" ,
    "4": "Four" ,
    "5": "Five"
}

output = ''
for ch in phone:
    output += digit_mapping.get( ch , "!") + " "
print(output)

####
messages = input("> ")
words = messages.split(' ')
emoji_converter = {
    ":)": "😁" ,
    ":(": "😥" ,
    "::" : "🤔"
}
output = ''

for word in words:
    output += emoji_converter.get(word, word) + " "

print(output)


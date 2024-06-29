is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("ware warm clothes")
else:
    print("Is's a lovely day")
print("Enjoy your day")

###

price = 1000000
had_good_credit = True

if had_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f'Down payment: ${down_payment}')

### Logical Operators

has_high_income = False
had_good_credit = True
has_criminal_record = True

# if had_good_credit and has_high_income:
#     print("Eligible for loan")

# if has_high_income or had_good_credit:
#     print("Eligible for loan")

if had_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Sorry, Your not Eligible")


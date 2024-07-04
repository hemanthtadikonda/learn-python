i = 1
while i <=5 :
    print(i)
    i = i +1
print("Done")
###
i = 1
while i <=5 :
    print('*' * i)
    i = i +1
print("Done")

### Guess the Number Game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter your choice:  "))
    guess_count += 1
    if guess == secret_number:
        print("Great, You Won!")
        break
else:
    print('Sorry, Better luck next time')

#### CAR GAME ###

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started..")
        else:
            print('car sarted...')
            started = True

    elif command == "stop":
        if not started:
            print("car already stopped. !")
        else:
            print("car stopped.! ")
            started = False
    elif command == "help":
        print('''
start --> to start the car
stop  --> to stop the car
quit  --> to quit the game
''')
    elif command == "quit":
        break
    else:
        print("Sorry. I don't understand! Press 'help' to know more")








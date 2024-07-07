import random

for i in range(3):
    # print (random.random())
    print(random.randint(10,60))

members = ["hema","radha","krinshna","yashodha","balarama","arjun"]
leader = random.choice(members)

print(leader)

##
import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        #return (first,second)
        return first,second


dice = Dice()
print(dice.roll())
import random

# random(help(random))

low = 0
high = 100

number = random.randint(low, high)
number1 = random.random()

options = ("rock", "paper", "scissors")

option = random.choice(options)

print(number)
print(number1)
print(option)


cards  = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)
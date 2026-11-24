# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input(f'Enter the price of a {food}: $'))
        prices.append(price)


print('---- YOUR CART -----')

for item in foods:
    print(item, end=" ")


for price in prices:
    total += price


print()
print(f'Your total is: ${total}')




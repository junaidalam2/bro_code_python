'''

fruits = ['apple', 'orange', 'banana', 'coconut']
vegetables = ['cellery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

groceries = [fruits, vegetables, meats]

print(groceries[0][1])

for row in groceries:
    for food in row:
        print(food, end=" ")
    print()



'''

numpad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*' , 0, '#'))

for row in numpad:
    for char in row:
       print(char, end=" ")
    print()

    
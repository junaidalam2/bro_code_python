
fruits = {'apple', 'orange', 'banana', 'coconut'}


print(fruits)

# print(help(fruits))


print('dog' in fruits)

fruits.remove('apple')
fruits.add('straberry')


fruits_tuple = ('apple', 'orange', 'banana', 'coconut')
print(fruits_tuple)

print(fruits_tuple.index('apple'))
fruits_tuple.count('coconut')

for fruit in fruits_tuple:
    print(fruit)
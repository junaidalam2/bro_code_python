fruits = ['apple', 'orange', 'banana', 'coconut']

print(fruits)

print(fruits[0])

print(fruits[1:2:2])

for fruit in fruits:
    print(fruit)


fruits.append('pineapple')
fruits.remove('apple')
fruits.append('apple')
fruits.insert(0, 'strawberry')
fruits.sort()
fruits.reverse() 


print(fruits.index('apple'))
print(fruits.count('apple'))


print(dir(fruits))

print(len(fruits))

print('apple' in fruits)


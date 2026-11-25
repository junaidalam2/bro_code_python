

capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


# print(dir(capitals))

# print(help(capitals))


print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")

capital_keys = capitals.keys()
capital_values = capitals.values()

items = capitals.items() # tuple of key value pair

print(capital_keys)
print(capitals)
print(capital_values)
print(items)


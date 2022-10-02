data = ['banana', 'apple', 'orange', 'cherry', 'kiwi']

data.remove('banana')
print(data)  # ['apple', 'orange', 'cherry', 'kiwi']

data.pop(0)
print(data)  # ['orange', 'cherry', 'kiwi']


data.pop()

print(data)  # ['orange', 'cherry']


del data[0]
print(data)  # ['cherry']


# del data; #Delete the variable data

data.clear()

print(data) # []




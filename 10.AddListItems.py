
list = ['apple', 'orange', 'banana']

data = []
for item in list:
    data.append(item)
print(data)  # ['apple', 'orange', 'banana']

# insert
list.insert(1, "kiwi")
print(list)  # ['apple', 'kiwi', 'orange', 'banana']


list.extend(["mango", "strawberry"])
print(list)  # ['apple', 'kiwi', 'orange', 'banana', 'mango', 'strawberry']
x = ("apple", "strawberry")
data.extend(x)
print(data)  # ['apple', 'orange', 'banana', 'apple', 'strawberry']

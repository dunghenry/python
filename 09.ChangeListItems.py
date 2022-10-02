list = ["apple", 'banana', 'orange', 'cherry', 'mango']
list[1] = "strawberry"

print(list)  # ['apple', 'strawberry', 'orange', 'cherry', 'mango']

list[1:3] = ["kiwi", "watermelon"]

print(list)  # ['apple', 'kiwi', 'watermelon', 'cherry', 'mango']


list[3:4] = ["banana", "watermelon"]
print(list)  # ['apple', 'kiwi', 'watermelon', 'banana', 'watermelon', 'mango']

list[0:2] = ["orange"]
print(list)  # ['orange', 'watermelon', 'banana', 'watermelon', 'mango']


# insert

list.insert(3, "cherry")
# ['orange', 'watermelon', 'banana', 'cherry', 'watermelon', 'mango']
print(list)

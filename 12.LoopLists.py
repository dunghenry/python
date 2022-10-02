data = ['apple', 'cherry', 'banana']
for item in data:
    print(item)


for i in range(len(data)):
    print(data[i])

i = 0
while i < len(data):
    print(data[i])
    i += 1

[print(i) for i in data]


newlist = []
for i in data:
    if "a" in i:
        newlist.append(i)

print(newlist)  # ['apple', 'banana']

new = [x for x in data if "a" in x]
print(new)  # ['apple', 'banana']


numbers = [x for x in range(10) if x < 5]
print(numbers)  # [0, 1, 2, 3, 4]


replace = [x if x != "banana" else "orange" for x in data]
print(replace)  # ['apple', 'cherry', 'orange']

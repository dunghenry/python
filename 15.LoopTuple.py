data = ("apple", "banana", "cherry")

for i in data:
    print(i)

for i in range(len(data)):
    print(data[i])
i = 0
while i < len(data):
    print(data[i])
    i += 1

tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = (1, 2, 3)

print(tuple1 + tuple2)  # ('a', 'b', 'c', 'd', 'e', 1, 2, 3)


frts = ("apple", "banana", "cherry")
dt = frts * 2
print(dt)  # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')


print(dt.count("apple"))  # 2
print(dt.index("banana"))  # 1

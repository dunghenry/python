fruits = ("apple", "orange", "strawberry", "kiwi")
print(fruits)  # ('apple', 'orange', 'strawberry', 'kiwi')
print(len(fruits))  # 4
print(type(fruits))  # <class 'tuple'>
print(fruits[0])  # apple

# single item
tuples = ("apple", )

print(type(tuples))  # <class 'tuple'>
# item data type : string , int , boolean

data = tuple(("Apple", "Orange"))
print(type(data))  # <class 'tuple'>

if "Apple" in data:
    print("Yes")  # Yes

print(fruits[1: 3])  # ('orange', 'strawberry')

# convert tuple to list and update

#remove: list.remove("apple")

# delete tuple
# del tupleName


s = ("apple", "orange")
(a, b) = s

print(a)  # apple
print(b)  # orange

users = ("Nam", "Mai", "Dung", "Ha")
(nam, mai, *others) = users

print(nam)  # Nam
print(others)  # ['Dung', 'Ha']

(n, *oth, h) = users
print(n)  # Nam
print(oth)  # ['Mai', 'Dung']
print(h) # Ha

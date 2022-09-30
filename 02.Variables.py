x = 1
str = "Hello"
z = float(2)  # int(), str()

print(x)  # 1
print(str)  # Hello
print(z)  # 2.0


# Check type
print(type(x))  # <class 'int'>

x1, x2 = "Orange", "Apple"

print(x1, x2)  # Orange Apple

y1 = y2 = "Orange"

print(y1, y2)  # Orange Orange


fruits = ["Apple", "Orange", "Mango"]

a, b, c = fruits

print(a, b, c)  # Apple Orange Mango


# Variable global

def myF():
    print(a)  # Apple


myF()


k = 1


def myK():
    global k
    print(k) # 1
    k = 2


myK()
print(k)  # 2

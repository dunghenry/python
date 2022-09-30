print(10 > 9)  # True

print(10 == 9)  # False

print(10 < 9)  # False

a = 200
b = 100

# b is not greater than a
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool('a'))  # True
print(bool('1'))  # True

# False
print(bool(False))  # False
print(bool(''))  # False
print(bool(""))  # False
print(bool(0))  # False
print(bool({}))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool(None))  # False


# funtion return boolean
def myF():
    return True


print(myF())  # True

# YES
if myF():
    print("YES")
else:
    print("NO")



x =  10
print(isinstance(x, int)) # True
print(isinstance(x, float)) # False
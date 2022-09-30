str = "Hello"

print(str)

# multiple string """""" or ''''''
a = """Xin chao
cac ban"""

print(a)

print(a[0])  # X

# loop
for x in a:
    print(x)

# len
print(len(a))  # 16

# check string
print("cac" in a)  # True

if "cac" in a:
    print("Yes")

# not in
print("cac" not in a)  # False

if "cac" not in a:
    print("False")

# slice
s = "Xin chao"

print(s[2:5])  # n c
print(s[:5])  # Xin c
print(s[2:])  # n chao
print(s[-4: -1])  # cha

# upper() and lower()
print("hello".upper())  # HELLO
print("Hello".lower())  # hello

# strip(): delete space
print("   hello    ".strip())  # hello

# replaces string
print("hello world".replace("hello", "HELLO"))  # HELLO world


# split()

print("hello world".split())  # ["hello", "world"]

# concat string

s1 = "Hello"
s2 = "World"

print(s1 + " " + s2)  # Hello World


# format
name = "Dung"
age = 22
data = "Hello, my name is {}, I'm {} years old"
print(data.format(name, age))  # Hello, my name is Dung, I'm 22 years old

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"

# I want to pay 49.95 dollars for 3 pieces of item 567
print(myorder.format(quantity, itemno, price))

txt = "Hello \"Dung\""
print(txt)  # Hello "Dung"

arr = ["Hello", "Dung"]
print(" ".join(arr))  # Hello Dung

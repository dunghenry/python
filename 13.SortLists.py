data = ['banana', 'apple', 'orange']

data.sort()

print(data)  # ['apple', 'banana', 'orange']
data.sort(reverse=True)
print(data)  # ['orange', 'banana', 'apple']


nums = [3, 2, 1, 4]

nums.sort()

print(nums)  # [1, 2, 3, 4]

nums.reverse()

print(nums)  # [4, 3, 2, 1]


# coppy

newdata = data.copy()

print(newdata)  # ['orange', 'banana', 'apple']
newdata[0] = 'kiwi'
print(newdata)  # ['kiwi', 'banana', 'apple']
print(data)  # ['orange', 'banana', 'apple']


# reference
dt = [1, 2, 3]
x = dt

x[0] = 10
print(dt)

lst1 = ['a', 'b', 'c', 'd', 'e']
nums = [1, 2, 3, 4, 5, 6, 7]

print(lst1 + nums)  # ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7]

# loop + append, extend


#Methods : append, extend, clear, copy, count: return the number of times the value, remove, insert, index: index item, pop, reverse, sort

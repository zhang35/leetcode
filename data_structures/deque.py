from collections import deque

de = deque([1, 2, 3])

# Access
n = len(de) # 3
a = de[0] # 1
b = de[-1] # 3
print(n, a, b)

# push & pop
de.append(4) # deque([1, 2, 3, 4])
de.appendleft(6) # deque([6, 1, 2, 3, 4])
print(de)
val_1 = de.pop() # 4
val_2 = de.popleft() # 6
print(val_1, val_2)

# concat
de.extend([4,5,6])  # deque([1, 2, 3, 4, 5, 6])
de.extendleft([7, 8, 9])  # deque([9, 8, 7, 1, 2, 3, 4, 5, 6])
print(de)

# transform
# rotates by 3 to left
de.rotate(-3)  # deque([1, 2, 3, 4, 5, 6, 9, 8, 7])
print(de)

de.reverse()  # deque([7, 8, 9, 6, 5, 4, 3, 2, 1])
print(de)
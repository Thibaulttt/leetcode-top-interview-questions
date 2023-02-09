# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Input: n = 4
# 2 2
# 1 1 2
# 2 1 1
# 1 2 1
# 1 1 1 1

n = 2

# print(list((x,y) for x in range(1,3) for y in range(1,3)))

res = [2 for i in range(8 // 2)]

n = 0
n0 = 0
n1 = 1

for i in range(20):
  n = n0 + n1
  n0 = n1
  n1 = n
  print(n)

# n = 
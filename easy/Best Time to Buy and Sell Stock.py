# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
prices = [2,4,1]
# 
# min 1, i=1 and max 7, i=0
# 1 > 0
# [1, 5, 3, 6, 4]
# min 1, i=1 and max 6, i=6
# 1 < 6

cur_max, day_max = max((p,i) for i,p in enumerate(prices))
cur_min, day_min = min((p,i) for i,p in enumerate(prices))

print(cur_max, day_max, cur_min, day_min)

# while day_max <= day_min:
#   for i, p in enumerate(prices[day_max:]):
#     print(p, cur_max, cur_min, day_max, day_min, prices[day_max:])
#     if p > cur_max:
#       cur_max = p
#       day_max = i
    
#     if p < cur_min:
#       cur_min = p
#       day_min = i

#     if day_max < day_min:
#       day_max += 1
#       cur_max = p

max = 0
min = prices[0]

for i in range(1, len(prices)):
  print(prices[i], min, max)
  if prices[i] < min:
    min = prices[i]
  elif (prices[i]-min) > max:
    max = prices[i] - min

print(max)

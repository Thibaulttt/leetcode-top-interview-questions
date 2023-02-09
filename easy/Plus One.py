digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]

print([int(c) for c in str(int(''.join([str(d) for d in digits])) + 1)])


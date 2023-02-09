# class Solution:
#     def reverseBits(self, n: int) -> int:
#         bits = ""
#         while n != 0:
#             bits += str(n%2)
#             n = n//2
#         return int(bits, 2)

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         b = ""
#         while n != 0:
#             r = n%2
#             n = n//2
#             b += str(r)
#         return b

class Solution:
    def reverseBits(self, n: int) -> int:
        print(str(bin(n)[2:]))
        return int(str(bin(n)[2:])[::-1], 2)

# 00000010100101000001111010011100
# 00111001011110000010100101000000

# 00111001011110000010100101000000
n =  43261596

solution = Solution()
print(solution.reverseBits(n), 2)

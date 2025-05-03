# 2022.11.05

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num ** (1/2)
        if sqrt == float(int(sqrt)):
            return True
        return False
        
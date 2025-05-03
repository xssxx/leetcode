# 2022.11.05

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if '-' in x:
            ans = '-' + str(int(x[:0:-1]))
        else:
            ans = int(x[::-1])

        if int(ans) not in range(-2**31, (2**31)-1):
            return 0
        return ans
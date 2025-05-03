# 2022.09.14

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list = []
        for i in range(len(str(x))):
            list.append(x % 10)
            x = x // 10
        
        if list == list[::-1]:
            return True
            
# 2023.03.31

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        
        while start < end:
            mid = (start + end) // 2
            is_bad = isBadVersion(mid)
            
            if is_bad:
                end = mid
            else:
                start = mid + 1
            
        return start

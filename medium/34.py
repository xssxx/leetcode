# 19.4.2026
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        res = [-1, -1]
        while l < n:
            if nums[l] == target:
                res[0] = l
                break
            l += 1
        while r >= 0:
            if nums[r] == target:
                res[1] = r
                break
            r -= 1

        return res

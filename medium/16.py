# 2024.12.16

from types import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = float('inf')
        n = len(nums)
        for i in range(n-2):
            l, r = i+1, n-1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if (abs(curr - target)) < abs(closet - target):
                    closet = curr

                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    return curr
                
        return closet
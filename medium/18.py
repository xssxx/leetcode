class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l, r = j+1, n-1

                while l < r:
                    _sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if _sum < target:
                        l += 1
                    elif _sum > target:
                        r -= 1
                    else:
                        out.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1 
                      
        return out

# 1.5.2026
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        memo = {}
        def backtrack(start, path=[]):
            state = (start, tuple(path))
            if state in memo:
                return
            
            res.append(list(path))
            memo[state] = True

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return res

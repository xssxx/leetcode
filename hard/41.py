class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = {val: 0 for val in nums}
        _max = max(1, max(nums)+2)
        for i in range(1, _max):
            if i not in m:
                return i
        return 1
  

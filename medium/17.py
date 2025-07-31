# 2025.07.31
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        n = {
            "2": "abc", "3": "def", 
            "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", 
            "8": "tuv", "9": "wxyz"
        }

        l = []
        for char in digits:
            l.append(n[char])

        def combine(list, index=0, current="", result=None):
            if result is None:
                result = []

            if index == len(list):
                result.append(current)
                return result
            
            for char in list[index]:
                combine(list, index + 1, current + char, result)

            return result

        return combine(l)
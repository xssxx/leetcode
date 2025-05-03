class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0

        isNeg = False
        if s[0] == "-":
            isNeg = True
            s = s[1::]
        elif s[0] == "+":
            isNeg = False
            s = s[1::]

        n = len(s) - 1
        
        idx = 0
        
        while idx < n:
            if s[idx] == "0":
                idx += 1
            else:
                break

        ans = ""
        while idx <= n:
            if s[idx].isdigit():
                ans += s[idx]
            else:
                break
            
            idx += 1

        if ans == "":
            return 0
        
        ans = int(ans) * -1 if isNeg else int(ans)

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if ans < INT_MIN:
            ans = INT_MIN
        elif ans > INT_MAX:
            ans = INT_MAX

        return ans
    
if __name__ == "__main__":
    sl = Solution()
    print(sl.myAtoi("    -042"))
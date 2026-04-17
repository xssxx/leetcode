class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid = [False] * len(s)
        st = []

        for i, char in enumerate(s):
            if char == '(':
                st.append(i)
            elif char == ')' and st:
                l_idx = st.pop()
                valid[l_idx] = True
                valid[i] = True
        
        max_len = 0
        curr = 0
        for v in valid:
            if v:
                curr += 1
                max_len = max(max_len, curr)
            else:
                curr = 0
        
        return max_len

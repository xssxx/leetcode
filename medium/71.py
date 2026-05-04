# 4.5.2026

class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split('/')
        sp = [s for s in sp if s != '.' and s != '']
        st = []

        for ch in sp:
            if st and ch == '..':
                st.pop()
            else:
                if ch != '..':
                    st.append(ch + '/')

        ans = '/' + ''.join(st)[:-1]
        return ans
        
"""

Example:
"/.../a/../b/c/../d/./"            ->     "/.../b/d"
"/../"                             ->     "/"
"/home//foo/"                      ->     "/home/foo"
"/home/user/Documents/../Pictures" ->     "/home/user/Pictures"

"""

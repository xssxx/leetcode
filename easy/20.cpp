// 2023.04.18

class Solution {
public:
    bool isValid(string s) {
        int N = s.size();
        if (N == 1)
            return false;
        
        vector<char> stack;
        for (int i = 0; i < N; i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                stack.push_back(s[i]);
            } else if (s[i] == ')' || s[i] == ']' || s[i] == '}') {
                if (stack.empty()) {
                    return false;
                } else {
                    char temp = stack.back();
                    stack.pop_back();
                    if ((temp == '(' && s[i] == ')') || (temp == '[' && s[i] == ']') || (temp == '{' && s[i] == '}'))
                        continue;
                    else
                        return false;
                }
            }
        }
        return stack.size() == 0;
    }
};
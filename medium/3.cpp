// 2023.12.22

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        int count = 0;
        int maxCount = 0;
        int start = 0;  

        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            
            if (map.find(c) == map.end() || map[c] < start) {
                // If the character is not in the current substring or is before the starting index
                map[c] = i;
                count = i - start + 1;
            } else {
                // If the character is already in the current substring
                start = map[c] + 1;
                map[c] = i;
                count = i - start + 1;
            }

            // Update the maximum count
            maxCount = max(maxCount, count);
        }

        return maxCount;
    }
};
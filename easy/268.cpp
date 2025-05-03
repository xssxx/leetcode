// 2023.12.03

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        unordered_set<int> set(nums.begin(), nums.end());

        for (int i = 0; i <= nums.size(); i++) {
            if (set.find(i) == set.end()) {
                return i;
            }
        }

        return -1;
    }
};
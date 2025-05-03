// 2023.12.02

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int n = nums.size();
        int out = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j] && i < j) {
                    out++;
                }
            }
        }
        return out;
    }
};
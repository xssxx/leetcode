// 2023.04.02

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int r_sum = reduce(nums.begin(), nums.end());
        int l_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            r_sum -= nums[i];
            if (l_sum == r_sum)
                return i;
            l_sum += nums[i];
        }
        return -1;
    }
};
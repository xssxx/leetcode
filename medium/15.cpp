// 2023.12.22

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> out;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            
            int l = i+1, r = n-1;
            int sum = 0;
            while (l < r) {
                sum = nums[i] + nums[l] + nums[r];
                if (sum > 0) 
                    --r;
                else if (sum < 0) 
                    ++l;
                else {
                    out.push_back({nums[i], nums[l], nums[r]});
                    ++l;
                    while (nums[l] == nums[l - 1] && l < r)
                        ++l;
                }
            }
        }
        return out;
    }
};
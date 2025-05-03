// 2023.12.03

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> map;

        for (auto i : nums)
            map[i]++;

        int n = nums.size();
        for (auto x : map) {
            if (x.second > n / 2)
                return x.first;
        }

        return -1;
    }
};
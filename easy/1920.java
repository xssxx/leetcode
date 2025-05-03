// 2023.12.02

class Solution {
    public int[] buildArray(int[] nums) {
        int n = nums.length;
        int[] out = new int[n];

        for (int i = 0; i < n; i++) {
            out[i] = nums[nums[i]];
        }

        return out;
    }
}
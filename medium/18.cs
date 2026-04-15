public class Solution
{
    public IList<IList<int>> FourSum(int[] nums, int target)
    {
        Array.Sort(nums);
        int n = nums.Length;
        IList<IList<int>> result = new List<IList<int>>();

        for (int i = 0; i < n - 3; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            for (int j = i + 1; j < n - 2; j++)
            {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;
                int l = j + 1,
                    r = n - 1;
                while (l < r)
                {
                    long sum = (long)nums[i] + nums[j] + nums[l] + nums[r];
                    if (sum < target)
                        l++;
                    else if (sum > target)
                        r--;
                    else
                    {
                        result.Add(new List<int> { nums[i], nums[j], nums[l], nums[r] });
                        l++;
                        r--;
                        while (l < r && nums[l] == nums[l - 1])
                            l++;
                        while (l < r && nums[r] == nums[r + 1])
                            r--;
                    }
                }
            }
        }
        return result;
    }
}

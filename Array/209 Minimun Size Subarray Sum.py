# 双指针滑动窗口 O(n)
# 前缀和 + 二分查找 O(nlogn)
import bisect


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        # 从开始元素用一个累加器保存和。将累积和保存在sums中
        sums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]
        if sums[-1] < s:
            return 0
        ans = float("inf")
        # 对每一个起点i, 找到从下标index开始满足sum ≥ s的子数组
        for i in range(1, len(sums)):
            # 用二分查找
            index = bisect.bisect_left(sums, s+sums[i-1])
            if index != len(sums):
                length = index - i + 1
                ans = min(ans, length)
        return ans if ans != float('inf') else 0
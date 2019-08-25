class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def DFS(index, sum, count):
            for i in [1, -1]:
                if index < len(nums) - 1:
                    count = DFS(index+1, sum + i * nums[index], count)
                else:
                    if sum + i * nums[index] == S:
                        count += 1
            return count

        return DFS(0, 0, 0)
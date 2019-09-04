class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        m, n = len(strs), len(strs[0])
        for j in range(n):
            for i in range(1, m):
                if j == len(strs[i]) or strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0]
        
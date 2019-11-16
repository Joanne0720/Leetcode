# 滑动窗口，从字典里找下一个窗口的start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = -1
        r = 0
        for i, c in s:
            if c in d:
                d[c] = i
            else:
                d[c] = i
                r += 1
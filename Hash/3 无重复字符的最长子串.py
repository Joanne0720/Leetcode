# 滑动窗口，从字典里找下一个窗口的start。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        r = 0
        for i, c in enumerate(s):
            if c in d and d[c] >= start:
                start = d[c] + 1
                d[c] = i
            else:
                d[c] = i
                r = max(r, i - start + 1)
        return r
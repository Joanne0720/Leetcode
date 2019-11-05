from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 把字符串中每个字符出现的次数保存在一个散列表中
        count = Counter(s)
        # 再遍历一次字符串，检查遍历的每个字符是不是唯一的
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
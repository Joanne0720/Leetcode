class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        # 用双指针找到一个单词
        i = 0
        while i < n:
            # 找到一个单词末位置
            j = i + 1
            while j < n and s[j] != " ":
                j += 1
            s[i:j] = s[i:j][::-1]
            # 找到下一个单词
            i = j + 1
        return "".join(s)

# 翻转法

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)

        # 翻转数组
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        “““
        相当于
        nums[:k] = nums[:k][::-1]
        ”””

        # 翻转单个单词
        def word_reverse(s):
            # 用双指针找到一个单词
            i = 0
            j = 0
            while i < n:
                # 找到一个单词首字母
                while i < n and s[i] == " ":
                    i += 1
                j = i
                # 找到一个单词末位置
                while j < n and s[j] != " ":
                    j += 1
                reverse(s, i, j - 1)
                i = j

        # 清除多余空格
        def clean_space(s):
            i = 0
            j = 0
            while j < n:
                # 找到一个单词
                while j < n and s[j] == " ":
                    j += 1
                # 单词朝前移
                while j < n and s[j] != " ":
                    s[i] = s[j]
                    i += 1
                    j += 1
                # 移动下一个单词
                while j < n and s[j] == " ":
                    j += 1
                if j < n:
                    s[i] = " "
                    i += 1
            return "".join(s[:i])

        reverse(s, 0, n - 1)
        word_reverse(s)
        return clean_space(s)

"""
暴力匹配的思路，假设现在文本串S匹配到 i 位置，模式串P匹配到 j 位置，则有：

如果当前字符匹配成功（即S[i] == P[j]），则i++，j++，继续匹配下一个字符；
如果失配（即S[i]! = P[j]），令i = i - (j - 1)，j = 0。相当于每次匹配失败时，i 回溯，j 被置为0。
"""

"""
KMP算法：https://www.cnblogs.com/ZuoAndFutureGirl/p/9028287.html
假设现在文本串S匹配到 i 位置，模式串P匹配到 j 位置：
如果j = -1，或者当前字符匹配成功（即S[i] == P[j]），都令i++，j++，继续匹配下一个字符；
如果j != -1，且当前字符匹配失败（即S[i] != P[j]），则令 i 不变，j = next[j]。
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        m, n = len(haystack), len(needle)

        def getNext(p):
            # 构造next数组
            next = [0] * n
            # 1)找前缀后缀最长公共元素长度; 2)求得的值整体右移一位，然后初值赋为-1
            i = 0   # 前缀的指针，next的值
            j = -1  # 后缀的指针，next的检索序列值
            next[i] = j
            # 用递推,已知next [0, ..., i]，求next [i + 1]
            while i < n - 1:
                # 若p[j] == p[i]，则next[i+1] = next [i] + 1 = j + 1
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    next[i] = j
                # 若p[j] ≠ p[i]，如果此时p[next[j]] == p[i]，则next[i+1] =  next[j] + 1, 否则继续递归前缀索引j = next[j]，而后重复此过程。
                else:
                    j = next[j]
            return next

        _next = getNext(needle)
        i, j = 0, 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j != 0:
                j = _next[j]
            else:
                i += 1
        if j == n:
            return i-j
        else:
            return -1

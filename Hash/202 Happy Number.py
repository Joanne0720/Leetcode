"""
最终一定会进入循环
1.如果是快乐数 1，1，1，1，1……
2.如果不是快乐数 4 16 37 58 89 145 42 20循环

如何判断进入哪个循环：
方法一：存入哈希表
方法二：快慢指针
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        class Solution:
            seen = {1}
            while n not in seen:
                seen.add(n)
                n = sum(int(i) ** 2 for i in str(n))
            return n == 1

class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
        return slow == "1"

"""
方法三：尾递归
尾递归：如果一个函数中所有递归形式的调用都出现在函数的末尾，我们称这个递归函数是尾递归的。
当递归调用是整个函数体中最后执行的语句且它的返回值不属于表达式的一部分时，这个递归调用就是尾递归。
尾递归函数的特点是在回归过程中不用做任何操作，这个特性很重要，因为大多数现代的编译器会利用这种特点自动生成优化的代码。
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        return self.isHappy(sum(int(i) ** 2 for i in str(n))) if n > 4 else n == 1

    # [1 ~ 4] 中只有 1 是快乐数，[5 ~ ∞] 的数字要么回归到 1 要么回归到 4 或 3
    # 因此仅需在 n > 4 时调用递归

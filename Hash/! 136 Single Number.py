# 方法一：哈希表
"""
try:
<语句>        #运行别的代码
except <name>：
<语句>        #如果在try部份引发了'name'异常
except <name>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


# 方法二：数学
"""
2∗(a+b+c)−(a+a+b+b+c)=c
"""
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


# 方法三：位操作，异或(i.e.对二进制数的每一位进行操作)
"""
对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
对相同的二进制位做 XOR 运算，返回的结果是 0
XOR 满足交换律和结合律
"""
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
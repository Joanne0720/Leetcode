class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = len(a) - len(b)
        a = '0' * -c + a
        b = '0' * c + b
        r, carry = '', 0
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + carry
            r = str(s % 2) + r
            carry = s // 2
        return '1' + r if carry else r

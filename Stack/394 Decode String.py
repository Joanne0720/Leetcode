class Solution:
    def decodeString(self, s: str) -> str:
        if s == []:
            return []
        stack = []
        for str in s:
            if str == ']':
                s_str = []
                while stack[-1] != '[':
                    s_str.insert(0, stack.pop())
                s_str = ''.join(s_str)
                stack.pop()
                k = []
                while stack and '0' <= stack[-1] <= '9':
                    k.insert(0, stack.pop())
                k = ''.join(k)
                stack.append(s_str * int(k))
            else:
                stack.append(str)
        return ''.join(stack)

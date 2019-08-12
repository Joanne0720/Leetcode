class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack == [] or mapping[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return stack == []
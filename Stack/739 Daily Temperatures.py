class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        for i in range(0, len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

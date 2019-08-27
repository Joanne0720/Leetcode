class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        result = []
        for k in range(m + n + 1):
            temp = []
            for i in range(max(0, k - n), min(m, k) + 1):
                temp.append(matrix[i][k-i])
            if not k % 2:
                temp.reverse()
            result += temp
        return result

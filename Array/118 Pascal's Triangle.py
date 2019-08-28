class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        r = [[1] for i in range(numRows)]
        if numRows == 1:
            return r
        r[1].append(1)
        if numRows == 2:
            return r
        for k in range(2, numRows):
            for l in range(1,k):
                r[k].append(r[k-1][l-1]+r[k-1][l])
            r[k].append(1)
        return r
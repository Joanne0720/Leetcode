class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    r = [1]
    for i in range(1, rowIndex + 1):
        r.insert(0, 0)
        for j in range(i):
            r[j] = r[j] + r[j + 1]
    return r
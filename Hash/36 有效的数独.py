# 在一次迭代中完成对行、列、子数独的检查


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
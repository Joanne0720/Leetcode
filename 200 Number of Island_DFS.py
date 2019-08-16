class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self._DFS(grid, i, j)
        return count

    def _DFS(self, grid, i, j):
        grid[i][j] = '0'
        for direction in self.directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == '1':
                self._DFS(grid, next_i, next_j)

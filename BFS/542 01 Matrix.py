class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        result = [[0 for _ in range(n)] for _ in range(m)]

        def bfs(i, j):
            directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
            q, visited, step = [(i, j)], set(), 0
            visited.add((i, j))
            while q:
                step += 1
                for _ in range(len(q)):
                    cur_i, cur_j = q.pop(0)
                    for d in directions:
                        nxt_i, nxt_j = cur_i + d[0], cur_j + d[1]
                        if 0 <= nxt_i < m and 0 <= nxt_j < n and (nxt_i, nxt_j) not in visited:
                            if matrix[nxt_i][nxt_j] != 0:
                                q.append((nxt_i, nxt_j))
                                visited.add((nxt_i, nxt_j))
                            else:
                                return step

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    result[i][j] = bfs(i, j)
        return result


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        q = [(sr, sc)]
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        while q:
            (cur_x, cur_y) = q.pop()
            for d in directions:
                nxt_x, nxt_y = cur_x + d[0], cur_y + d[1]
                if 0 <= nxt_x < len(image) and 0 <= nxt_y < len(image[0]) and image[nxt_x][nxt_y] == oldColor:
                    image[nxt_x][nxt_y] = newColor
                    q.append((nxt_x, nxt_y))
        return image
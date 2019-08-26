class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(r, visited):
            for i in rooms[r]:
                if i not in visited:
                    visited.append(i)
                    dfs(i, visited)
            return

        visit = [0]
        dfs(0, visit)
        return len(visit) == len(rooms)
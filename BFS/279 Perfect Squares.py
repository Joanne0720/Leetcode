from queue import Queue


class Solution:
    def numSquares(self, n: int) -> int:
        q = Queue()
        used = set()
        step = 0
        q.put((0, step))   #  这样可以省去一层循环
        while 1:
            #  size = q.qsize()
            #  for i in range(size):
            cur, step = q.get()
            step += 1
            j = 1
            while cur + j ** 2 <= n:
                if cur + j ** 2 == n:
                    return step
                if cur + j ** 2 not in used:
                    q.put((cur + j ** 2, step))
                    used.add(cur + j ** 2)
                j += 1
from queue import Queue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        #  初始化
        q = Queue()
        deadends = set(deadends)
        step = -1
        q.put('0000')
        deadends.add('0000')
        #  开始循环
        while not q.empty():
            size = q.qsize()
            step += 1
            for i in range(size):
                cur = q.get()
                if cur == target:
                    return step
                #  8个相邻点
                for j in range(4):
                    for k in (1, -1):
                        next = cur[:j] + str((int(cur[j]) + k) % 10) + cur[j+1:]
                        if next not in deadends:
                            q.put(next)
                            deadends.add(next)
        return -1
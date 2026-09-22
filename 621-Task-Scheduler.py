class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        if n == 0:
            return len(tasks)

        counter = [0] * 26

        for t in tasks:
            counter[ord(t) - ord("A")] += 1

        counter.sort()

        space = counter[25] - 1
        idleSpots = space * n

        for i in range(24, -1, -1):
            idleSpots -= min(space, counter[i])

        if idleSpots > 0:
            return idleSpots + len(tasks)
        else:
            return len(tasks)

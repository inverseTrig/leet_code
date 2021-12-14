class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2

        minutes = 0
        rotten, fresh = list(), list()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ROTTEN:
                    rotten.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh.append((i, j))

        while True:
            changed = list()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i, j in rotten:
                for dx, dy in directions:
                    reference_index = (i + dx, j + dy)
                    if reference_index in fresh:
                        changed.append(reference_index)
                        fresh.remove(reference_index)
            if not changed:
                return -1 if fresh else minutes
            rotten = changed
            minutes += 1

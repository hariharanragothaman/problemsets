import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Core Logic for printing the grid
        # This is BFS
        R = len(grid)
        C = len(grid[0])

        print("The I/P matrix is:")
        for row in grid:
            print(' '.join([str(elem) for elem in row]))

        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        print("The queue is (rotten)", queue)

        def neighbours(r, c):
            """
            Function to get the neighbours
            """
            for nr, nc in ( (r-1, c),
                            (r, c-1),
                            (r+1, c),
                            (r, c+1)
                          ):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc


        # Actual core logic:
        d = 0 
        while queue:
            r, c, d = queue.popleft()
            print ("The value of r is:", r)
            print ("The value of c is:", c)
            print ("The value of d is:" ,d)

            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))


        # Final check to see if anything is healthy still?
        if any(1 in row for row in grid):
            return -1

        return d

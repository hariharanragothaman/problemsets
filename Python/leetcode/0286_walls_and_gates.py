class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return -1
           
        R = len(rooms)
        C = len(rooms[0])
        
        
        for row in rooms:
            print (" ".join([str(c) for c in row]))
            
        # Add elements in the queue wherever it's a gate
        queue = collections.deque()
        
        for r, rows in enumerate(rooms):
            for c, val in enumerate(rows):
                if val == 0:
                    queue.append((r,c))
    
        print(queue)
        
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
        
    
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        
        if len(queue) == 0:
            return rooms
        
        while queue:
            r, c = queue.popleft()
            print (r, c)
            
            for data in dirs:
                new_x, new_y = r+data[0], c+data[1]           
                if new_x >= 0 and new_x <= len(rooms)-1 and new_y >= 0 and new_y <= len(rooms[0])-1:
                    if rooms[new_x][new_y] == 2147483647:
                        queue.append((new_x, new_y))
                        rooms[new_x][new_y] = rooms[r][c] + 1
        return rooms 

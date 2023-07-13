class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int: 
        # get number of rows 
        number_of_rows = len(grid)

        #chek if the grid is empty, then there is no islands
        if number_of_rows == 0:
            return 0
        
        #get number of columns 
        number_of_columns = len(grid[0])

        #initiate visited a bool matrix has same size of grid to check if a particular cell has been visited or not.
        visited = set()

        closed_islands_number = 0

        #visit every single position in the grid
        for row in range(number_of_rows):
            for col in range(number_of_columns):

                #check if the cell contains 0, then traverse and mark it as visited
                if grid[row][col] == 0 and (row, col) not in visited: 
                    
                    q = collections.deque()
                    visited.add((row, col))
                    q.append((row, col))

                    closed = True 

                    #while the queue is not empty then expand the island
                    while q:
                        #check if the cell is an edge then set closed to False 
                        row_, col_ = q.popleft() 

                        if row_ == 0 or row_ == (number_of_rows - 1):
                            closed = False 
                        
                        if col_ == 0 or col_ == (number_of_columns - 1):
                            closed = False 

                        #check the adjacent position of the the cell I've poped  
                        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                        for dr, dc in directions:
                            dr = row_ + dr
                            dc = col_ + dc  
                            if (
                                (dr) in range(number_of_rows) and
                                (dc) in range(number_of_columns) and 
                                grid[dr][dc] == 0 and
                                (dr, dc) not in visited
                                ):
                                    q.append((dr, dc))
                                    visited.add((dr, dc))  
                                    
                    if closed:  
                        closed_islands_number += 1

        return closed_islands_number

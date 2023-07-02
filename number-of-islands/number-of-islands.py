class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # get number of rows 
        number_of_rows = len(grid)

        #chek if the grid is empty, then there is no islands
        if number_of_rows == 0:
            return 0
        
        #get number of columns 
        number_of_columns = len(grid[0])

        #initiate visited a bool matrix has same size of grid to check if a particular cell has been visited or not.
        visited = set()

        islands_number = 0
        #visit every single position in the grid
        for row in range(number_of_rows):
            for col in range(number_of_columns):
                #check if the cell contains 1, them traverse and mark it as visited
                if grid[row][col] == "1" and (row, col) not in visited: 
                    #since bfs is an iterative algorithm not a recursive algorithm, so I'll use queue data structure
                    q = collections.deque()
                    visited.add((row, col))
                    q.append((row, col))

                    #while the queue is not empty then expand the island
                    while q:
                        row_, col_ = q.popleft()
                        #check the adjacent position of the the cell I've poped  
                        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                        for dr, dc in directions:
                            if (
                                (row_ + dr) in range(number_of_rows) and
                                (col_ + dc) in range(number_of_columns) and 
                                grid[row_ + dr][col_ + dc] == "1" and
                                (row_ + dr, col_ + dc) not in visited
                                ):
                                    q.append((row_ + dr, col_ + dc))
                                    visited.add((row_ + dr, col_ + dc))

                    islands_number += 1

        return islands_number


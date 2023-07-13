class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #get grid rows number
        rows_num = len(grid)
        
        #chek if there is no island
        if rows_num == 0:
            return 0
        else:
            #add padding to the grid by 1 with value of 0(water)
            for list_ in grid:
                list_.insert(0, 0)
                list_.append(0)

            #get number of columns
            cols_num = len(grid[0])
            grid.append([0 for zero in range(cols_num)])
            grid.insert(0, [0 for zero in range(cols_num)])

            #upadte number of rows 
            rows_num += 2
        #initiate visited a et to track island blocks
        visited = set()

        island_perimeter = 0
        #visit every single position in the grid to find a land block
        for row in range(rows_num):
            for col in range(cols_num):
                #check if the cell contains 1, them traverse and mark it as visited
                if grid[row][col] == 1 and (row, col) not in visited: 
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
                            dr = row_ + dr
                            dc = col_ + dc 
                            if (
                                (dr) in range(rows_num) and
                                (dc) in range(cols_num) and  
                                (dr, dc) not in visited
                                ): 
                                    if grid[dr][dc] == 0:
                                        island_perimeter += 1
                                    else:
                                        q.append((dr, dc))
                                        visited.add((dr, dc)) 
                    return island_perimeter



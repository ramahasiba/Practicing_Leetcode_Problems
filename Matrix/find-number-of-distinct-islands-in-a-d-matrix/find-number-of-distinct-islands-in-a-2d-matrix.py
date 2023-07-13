import collections

class Solution:
    def number_of_distinct_island(self, grid) -> int:
        distinct_island_number = 0 

        #get number of rows
        rows_number = len(grid)

        #check if there is no grid
        if rows_number == 0:
            return distinct_island_number
        
        #get number of columns 
        cols_number = len(grid[0])

        visited = set()

        islands_detail = []
        directions = [
            [0, 1], 
            [-1, 0],
            [0, -1],
            [1, 0]
        ]
        
        number_of_islands = 0

        #count number of islands using bfs, and store there details such as 
        # (number of ones, island dimension when it is represented as a matrix, and ones position in island matrix)
        for row in range(rows_number):
            for col in range(cols_number):
                if grid[row][col] == 1 and (row, col) not in visited:

                    q = collections.deque()
                    visited.add((row, col))
                    q.append((row, col))

                    island_size = 1

                    rows_value = [row]
                    cols_value = [col]

                    min_row_val = row
                    min_col_val = col

                    max_row_val = row
                    max_col_val = col  

                    while q:
                        curr_row, curr_col = q.popleft()
                        for direction in directions:
                            new_row = curr_row + direction[0]
                            new_col = curr_col + direction[1]
                            if(
                                (new_row >= 0 and new_row < rows_number) and
                                (new_col >= 0 and new_col < cols_number) and 
                                grid[new_row][new_col] == 1 and 
                                (new_row, new_col) not in visited
                            ):
                                q.append((new_row, new_col))
                                visited.add((new_row, new_col))
                                island_size += 1 

                                rows_value.append(new_row)
                                cols_value.append(new_col)

                                #check values to keep the find the maximum and minimum value in the column and row list
                                if min_row_val > row:
                                    min_row_val = row

                                if min_col_val > col:
                                    min_col_val = col 

                                if max_col_val < col:
                                    min_col_val = col

                                if max_row_val < row:
                                    min_row_val = row

                    number_of_islands += 1

                    #get island_ones_positions to compare it with other islands to check for similarity
                    island_ones_positions = set()
                    for index, row_val in enumerate(rows_value):
                        island_ones_positions.add((min_row_val - row_val, min_col_val - cols_value[index]))

                    islands_detail.append({
                        "number of ones": island_size,
                        "matrix dimensions": ((max_row_val - min_row_val) , (max_col_val - min_col_val)), 
                        "island ones positions": island_ones_positions, 
                        "unique": True 
                    })

         
        distinct_island_number =  number_of_islands

        #Count number of distinct islands by decreasing number of islands by one 
        # if two unique islands has the same details
        for index, island in enumerate(islands_detail):
            if island["unique"]:  
                for sec_island in islands_detail[index + 1: ]:
                    if sec_island['unique'] == True: 
                        if (
                            sec_island["number of ones"] == island["number of ones"] and 
                            sec_island["matrix dimensions"] == island["matrix dimensions"]
                        ): 
                            if island["island ones positions"] == sec_island["island ones positions"]:
                                sec_island["unique"] = False
                                distinct_island_number -= 1

        return distinct_island_number
    

grid = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
    ]

grid_2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    ]

grid_3 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
    ]

sol = Solution()

print(sol.number_of_distinct_island(grid_3))
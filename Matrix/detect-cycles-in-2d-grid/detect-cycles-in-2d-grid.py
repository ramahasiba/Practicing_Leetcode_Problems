
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        def bfs(row, col, visited):
            visited[row][col] = 1
            queue = [[[row,col],[-1,-1]]]
            while queue:
                popped = queue.pop(0)
                row, col = popped[0][0], popped[0][1]
                parent_row, parent_col = popped[1][0], popped[1][1]
                
                current_char = grid[row][col]
                for i in range(4):
                    row_ = row + row_directions[i]
                    col_ = col + col_directions[i]
                    
                    if row_ >= 0 and row_ < rows_number and col_ >= 0 and col_ < columns_number and grid[row_][col_] == current_char:
                        if not visited[row_][col_]:
                            visited[row_][col_] = 1
                            queue.append([[row_,col_],[row,col]])
                        elif parent_row != row_ and parent_col != col_:
                            return True
            return False
                
        
        
        rows_number = len(grid)
        columns_number = len(grid[0])
        
        row_directions = [-1,0,1,0]
        col_directions = [0,1,0,-1]

        
        visited = [[0 for _ in range(columns_number)] for _ in range(rows_number)]
        
        for row in range(rows_number):
            for col in range(columns_number):
                if not visited[row][col]:
                    if bfs(row, col, visited):
                        return True
        return False
 
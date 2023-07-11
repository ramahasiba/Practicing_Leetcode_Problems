class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #get image width(numbe of columns)
        rows_num = len(image)

        #check if there is no image 
        if rows_num == 0:
            return image

        #check if the starting pixel color is the same of the given one, then return the same image(matrix)
        if image[sr][sc] == color:
            return image
        else:
            #define visited to track neighbours of the given cell.
            visited = set()

            #get image height(number of rows)
            cols_num = len(image[0])

            src_color = image[sr][sc]
            image[sr][sc] = color

            q = collections.deque()
            visited.add((sr, sc))
            q.append((sr, sc))

            while q:
                current_row, current_column = q.popleft()
                #check if the adjacent position has the same color(src)
                directions = [
                    [1, 0], [-1, 0], [0, 1], [0, -1]
                ]

                for direcrtion_row, direction_col in directions:
                    dr = current_row + direcrtion_row
                    dc = current_column + direction_col
                    if (
                        #check if the given indecies inside matrix dimentions range
                        dr in range(rows_num) and
                        dc in range(cols_num) and
                        #check if the adjacent cell has the same color
                        image[dr][dc] == src_color and
                        #ensure that the cell is not visited yet
                        (dr, dc) not in visited
                    ):
                        image[dr][dc] = color
                        q.append((dr, dc))
                        visited.add((dr, dc))

        return image 
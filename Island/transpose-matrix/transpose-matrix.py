#6 mins

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        flipped_matrix = []

        #get number of columns, and rows  
        number_of_columns = len(matrix[0]) 

        for column_index in range(number_of_columns):
            column_values = [row[column_index] for row in matrix]
            flipped_matrix.append(column_values)
 
        return flipped_matrix



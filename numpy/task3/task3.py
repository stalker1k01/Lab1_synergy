import numpy as np

def get_unique_in_rows(matrix):
    matrix = np.array(matrix)
    result = []
    
    for i in range(matrix.shape[0]):
        unique_elements = np.unique(matrix[i, :])
        result.append(unique_elements)

    return result

def get_unique_in_columns(matrix):
    matrix = np.array(matrix)
    result = []
    
    for j in range(matrix.shape[1]):
        unique_elements = np.unique(matrix[:, j])
        result.append(unique_elements)
    
    return result
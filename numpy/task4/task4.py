import numpy as np
import matplotlib.pyplot as plt

def analyze_matrix(m, n, _await=0, tilt=1):
    matrix = np.random.normal(loc=_await, scale=tilt, size=(m, n))
    
    for j in range(n):
        column = matrix[:, j]
        col_mean = np.mean(column)
        col_var = np.var(column)
        print(f"Столбец {j+1}: МО = {col_mean:.4f}, Дисперсия = {col_var:.4f}")
    
    for i in range(m):
        row = matrix[i, :]
        row_mean = np.mean(row)
        row_var = np.var(row)
        print(f"Строка {i+1}: МО = {row_mean:.4f}, Дисперсия = {row_var:.4f}")
    
    fig, axes = plt.subplots(2, (n+1)//2, figsize=(15, 8))
    if n > 1:
        axes = axes.flatten()
    else:
        axes = [axes]
    
    for j in range(n):
        axes[j].hist(matrix[:, j], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
        axes[j].set_title(f'Гистограмма столбца {j+1}')
        axes[j].set_xlabel('Значения')
        axes[j].set_ylabel('Частота')
    
    for j in range(n, len(axes)):
        axes[j].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    
    fig, axes = plt.subplots(2, (m+1)//2, figsize=(15, 8))
    if m > 1:
        axes = axes.flatten()
    else:
        axes = [axes]
    
    for i in range(m):
        axes[i].hist(matrix[i, :], bins=15, alpha=0.7, color='lightcoral', edgecolor='black')
        axes[i].set_title(f'Гистограмма строки {i+1}')
        axes[i].set_xlabel('Значения')
        axes[i].set_ylabel('Частота')
    
    for i in range(m, len(axes)):
        axes[i].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    
    return matrix

def test_matrix_creation_shape_and_type():
    m, n = 3, 4
    matrix = analyze_matrix(m, n)
        
    assert matrix.shape == (m, n)
    assert matrix.dtype == np.float64
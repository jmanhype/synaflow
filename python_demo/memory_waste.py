"""Module demonstrating inefficient memory usage patterns."""
from typing import List, Dict, Tuple, Optional
import time

def memory_inefficient_dict_handling(n: int) -> Dict[int, str]:
    """Creates a dictionary with inefficient update patterns."""
    result = {}
    for i in range(n):
        temp = result.copy()  # Unnecessary copy
        temp[i] = f"value_{i}"
        result = temp
    return result

def inefficient_list_operations(data: List[int]) -> List[int]:
    """Performs inefficient operations on lists."""
    result = []
    for i in range(1000):
        result.insert(0, i)  # Inserting at beginning is O(n)
    to_remove = []
    for item in result:
        if item % 3 == 0:
            to_remove.append(item)
    for item in to_remove:
        result.remove(item)  # O(n) operation
    return result

def slow_matrix_operations(size: int) -> List[List[int]]:
    """Performs inefficient matrix operations."""
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i * j)
        matrix.append(row)
    transposed = []
    for i in range(size):
        new_row = []
        for j in range(size):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed

if __name__ == "__main__":
    start_time = time.time()
    dict_result = memory_inefficient_dict_handling(1000)
    list_result = inefficient_list_operations(list(range(100)))
    matrix_result = slow_matrix_operations(50)
    elapsed = time.time() - start_time
    print(f"Completed operations in {elapsed:.2f} seconds")
    print(f"Dictionary size: {len(dict_result)}")
    print(f"List size: {len(list_result)}")
    print(f"Matrix size: {len(matrix_result)}x{len(matrix_result[0])}")

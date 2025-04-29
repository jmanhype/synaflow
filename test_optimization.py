"""
This file contains multiple optimization opportunities for testing.
"""
import time
import math
from typing import List, Dict, Any, Optional


def inefficient_list_processing(numbers: List[int]) -> int:
    """
    Process a list of numbers inefficiently.
    
    Args:
        numbers: List of integers to process
        
    Returns:
        Sum of positive numbers multiplied by 2
    """
    # Filter for positive numbers (inefficient)
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    
    # Multiply each by 2 (inefficient)
    doubled = []
    for num in positives:
        doubled.append(num * 2)
    
    # Sum them (inefficient)
    total = 0
    for num in doubled:
        total += num
    
    return total


def inefficient_string_concatenation(words: List[str]) -> str:
    """
    Concatenate strings inefficiently.
    
    Args:
        words: List of strings to concatenate
        
    Returns:
        Concatenated string
    """
    # Inefficient string concatenation
    result = ""
    for word in words:
        result = result + word + " "
    
    return result.strip()


def redundant_calculations(n: int) -> List[float]:
    """
    Perform redundant calculations.
    
    Args:
        n: Number of calculations to perform
        
    Returns:
        List of calculation results
    """
    results = []
    for i in range(n):
        # Redundant calculation of the same value in each iteration
        value = math.sqrt(1764) / 42
        results.append(value * i)
    
    return results


def unnecessary_memory_usage(size: int) -> List[Dict[str, Any]]:
    """
    Use memory inefficiently.
    
    Args:
        size: Size of the data structure
        
    Returns:
        List of dictionaries
    """
    # Create a large data structure unnecessarily
    big_list = []
    for i in range(size):
        # Each dictionary is created with redundant keys
        item = {
            "id": i,
            "id_str": str(i),
            "id_hex": hex(i),
            "id_bin": bin(i),
            "id_oct": oct(i),
            "data": "x" * 100,  # Unnecessarily large string
        }
        big_list.append(item)
    
    return big_list


def inefficient_search(items: List[Dict[str, Any]], target_id: int) -> Optional[Dict[str, Any]]:
    """
    Search for an item inefficiently.
    
    Args:
        items: List of dictionaries to search
        target_id: ID to search for
        
    Returns:
        Found item or None
    """
    # Linear search when a dictionary lookup would be better
    for item in items:
        if item["id"] == target_id:
            # Unnecessary deep copy
            result = {}
            for key in item:
                result[key] = item[key]
            return result
    
    return None


def main():
    """Run example functions with timing."""
    # Inefficient list processing
    start = time.time()
    result1 = inefficient_list_processing(list(range(-1000, 1000)))
    print(f"List processing result: {result1}, Time: {time.time() - start:.4f}s")
    
    # String concatenation
    start = time.time()
    result2 = inefficient_string_concatenation(["This", "is", "a", "test", "of", "string", "concatenation"] * 100)
    print(f"String length: {len(result2)}, Time: {time.time() - start:.4f}s")
    
    # Redundant calculations
    start = time.time()
    result3 = redundant_calculations(1000)
    print(f"Calculations result length: {len(result3)}, Time: {time.time() - start:.4f}s")
    
    # Memory usage
    start = time.time()
    result4 = unnecessary_memory_usage(100)
    print(f"Memory usage result length: {len(result4)}, Time: {time.time() - start:.4f}s")
    
    # Search
    start = time.time()
    result5 = inefficient_search(result4, 50)
    print(f"Search result: {result5 is not None}, Time: {time.time() - start:.4f}s")


if __name__ == "__main__":
    main() 
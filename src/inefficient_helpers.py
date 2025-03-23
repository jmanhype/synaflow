"""Inefficient helper functions for demonstration purposes."""
from typing import List, Dict, Any, Optional, Tuple
import time
import random


def inefficient_string_concat(items: List[str]) -> str:
    """
    Concatenate strings inefficiently using the + operator in a loop.
    
    Args:
        items: A list of strings to concatenate
        
    Returns:
        Concatenated string
    """
    result = ""
    for item in items:
        result = result + item  # Inefficient string concatenation
    return result


def expensive_factorial(n: int) -> int:
    """
    Calculate factorial using an inefficient recursive approach.
    
    Args:
        n: The number to calculate factorial for
        
    Returns:
        The factorial of n
    """
    if n <= 1:
        return 1
    else:
        return n * expensive_factorial(n - 1)  # Inefficient recursive approach


def inefficient_list_builder(size: int) -> List[int]:
    """
    Build a list inefficiently by copying and appending one by one.
    
    Args:
        size: The size of the list to build
        
    Returns:
        A list of integers
    """
    result = []
    for i in range(size):
        result = result + [i * i]  # Inefficient list building
    return result


def slow_search(needle: str, haystack: List[str]) -> bool:
    """
    Search for an item in a list inefficiently using a loop.
    
    Args:
        needle: The string to search for
        haystack: The list to search in
        
    Returns:
        True if found, False otherwise
    """
    found = False
    for item in haystack:
        if item == needle:
            found = True
    return found  # Should return immediately when found


def memory_hog(size: int = 1000) -> Dict[str, List[int]]:
    """
    Create a large dictionary with unnecessary data.
    
    Args:
        size: The size of the data to create
        
    Returns:
        A dictionary with unnecessary data
    """
    big_dict = {}
    temp_list = []
    
    # Create large temporary lists that are immediately thrown away
    for i in range(size):
        temp_list = []
        for j in range(size):
            temp_list.append(j)
        
        # Only use a small portion of the data
        big_dict[f"key_{i}"] = temp_list[:10]
    
    return big_dict


def main() -> None:
    """Run sample code that demonstrates inefficient patterns."""
    # Test string concatenation
    words = ["This", " ", "is", " ", "an", " ", "inefficient", " ", "way", " ", "to", " ", "concat", " ", "strings"]
    result = inefficient_string_concat(words)
    print(f"Concatenated: {result}")
    
    # Test factorial
    n = 5
    fact = expensive_factorial(n)
    print(f"Factorial of {n}: {fact}")
    
    # Build list inefficiently
    numbers = inefficient_list_builder(10)
    print(f"List: {numbers}")
    
    # Slow search
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    found = slow_search("cherry", items)
    print(f"Found cherry: {found}")
    
    # Create unnecessary memory usage
    data = memory_hog(10)
    print(f"Memory hog sample: {list(data.keys())[:3]}...")


if __name__ == "__main__":
    main()

"""
This module contains deliberately inefficient code to test optimization processes.
"""
from typing import List, Dict, Any, Optional
import time


def slow_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a very inefficient recursive approach.
    
    Args:
        n: The position in the Fibonacci sequence to calculate
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)


def inefficient_string_concatenation(n: int) -> str:
    """
    Build a long string by repeatedly concatenating in a loop.
    
    Args:
        n: The number of strings to concatenate
        
    Returns:
        The concatenated string
    """
    result = ""
    for i in range(n):
        result = result + str(i) + "-"
    return result


def slow_search(items: List[Any], target: Any) -> bool:
    """
    Perform a linear search through the list.
    
    Args:
        items: List to search through
        target: Item to find
        
    Returns:
        True if the item is found, False otherwise
    """
    found = False
    for item in items:
        if item == target:
            found = True
            break
    return found


def nested_loops_processing(data: List[int]) -> List[int]:
    """
    Process data using nested loops instead of list comprehensions.
    
    Args:
        data: List of integers to process
        
    Returns:
        Processed list of squared even numbers
    """
    filtered = []
    for item in data:
        if item % 2 == 0:
            filtered.append(item)
    
    result = []
    for item in filtered:
        result.append(item * item)
    
    return result


def repeated_calculations(data: List[int], threshold: int = 10) -> Dict[int, float]:
    """
    Perform repeated calculations on the same data multiple times.
    
    Args:
        data: Input data to process
        threshold: Minimum value to include in results
        
    Returns:
        Dictionary mapping values to their processed results
    """
    results = {}
    for i, value in enumerate(data):
        if len(data) > threshold:  # Repeated calculation of len(data)
            if value > threshold:  # Repeated comparison
                # Calculate average each time unnecessarily
                avg = sum(data) / len(data)
                results[value] = value / avg
    return results


def global_variable_function() -> None:
    """
    Function that uses and modifies global variables.
    """
    global counter
    counter += 1
    print(f"Counter is now {counter}")


# Global variable
counter = 0


class InefficientClass:
    """A class with inefficient methods and attribute access."""
    
    def __init__(self, name: str, values: Optional[List[int]] = None):
        """Initialize with a name and optional values.
        
        Args:
            name: The name of this instance
            values: Optional list of values
        """
        self.name = name
        self.values = values or []
        self.processed = {}
        
    def process_values(self) -> Dict[int, int]:
        """
        Process values inefficiently by repeatedly accessing object attributes.
        
        Returns:
            Dictionary of processed values
        """
        for i in range(len(self.values)):
            # Inefficient: repeatedly accessing self.values and self.processed
            self.processed[self.values[i]] = self.values[i] * 2
        return self.processed
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Calculate statistics on the values.
        
        Returns:
            Dictionary of statistics
        """
        if not self.values:
            return {"count": 0, "average": 0}
        
        # Inefficient: recalculating sum and length multiple times
        return {
            "count": len(self.values),
            "sum": sum(self.values),
            "average": sum(self.values) / len(self.values),
            "max": max(self.values),
            "min": min(self.values)
        }


if __name__ == "__main__":
    # Test with some sample data
    numbers = list(range(20))
    
    # Inefficient string operation
    result1 = inefficient_string_concatenation(1000)
    print(f"Generated a string of length {len(result1)}")
    
    # Inefficient data processing
    result2 = nested_loops_processing(numbers)
    print(f"Processed {len(result2)} numbers")
    
    # Slow Fibonacci calculation
    start = time.time()
    fib = slow_fibonacci(20)
    end = time.time()
    print(f"Fibonacci calculation took {end - start:.4f} seconds")
    
    # Inefficient class usage
    obj = InefficientClass("test", numbers)
    obj.process_values()
    stats = obj.get_stats()
    print(f"Object stats: {stats}") 
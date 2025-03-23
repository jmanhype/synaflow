# Inefficient Python code for optimization testing
# Modified version for testing automatic optimization

def slow_function(n):
    """A deliberately inefficient function that builds a list of strings."""
    result = []
    for i in range(n):
        s = ""
        for j in range(i):
            s = s + str(j) + "-"
        result.append(s)
    return result

def inefficient_data_processing(data):
    """Process data inefficiently using multiple loops."""
    filtered = []
    for item in data:
        if item % 2 == 0:
            filtered.append(item)
    result = []
    for item in filtered:
        result.append(item * item)
    return result

def slow_search(lst, item):
    """A deliberately slow search algorithm."""
    found = False
    for element in lst:
        if element == item:
            found = True
            break
    return found

def extra_inefficient_func(data, threshold=10):
    """A new inefficient function for testing."""
    result = []
    # Inefficient loop with string concatenation
    for i, value in enumerate(data):
        if value > threshold:
            temp_str = ""
            for j in range(value):
                temp_str += str(j) + ","
            result.append(temp_str)
    return result

if __name__ == "__main__":
    numbers = list(range(1000))
    result1 = slow_function(100)
    result2 = inefficient_data_processing(numbers)
    result3 = [slow_search(numbers, i) for i in range(100)]
    result4 = extra_inefficient_func(numbers[:20], 5)
    print(f"Generated {len(result1)} strings")
    print(f"Processed {len(result2)} numbers")
    print(f"Found {sum(result3)} items")
    print(f"Extra inefficient results: {len(result4)}")

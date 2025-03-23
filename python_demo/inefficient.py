# Inefficient Python code for optimization testing

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

if __name__ == "__main__":
    numbers = list(range(1000))
    result1 = slow_function(100)
    result2 = inefficient_data_processing(numbers)
    result3 = [slow_search(numbers, i) for i in range(100)]
    print(f"Generated {len(result1)} strings")
    print(f"Processed {len(result2)} numbers")
    print(f"Found {sum(result3)} items")

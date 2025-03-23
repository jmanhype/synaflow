"""
Utility functions with optimization opportunities.
"""
import time
from typing import List, Dict, Any

def build_knowledge_base(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Inefficiently builds a knowledge base from items.
    
    Args:
        items: List of knowledge items
        
    Returns:
        Processed knowledge base
    """
    # Inefficient list building with repeated concatenation
    knowledge_base = []
    for item in items:
        # Using concatenation instead of append
        knowledge_base = knowledge_base + [item]
    return knowledge_base

def process_citations(citations: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    """
    Process citations inefficiently.
    
    Args:
        citations: List of citation dictionaries
        
    Returns:
        Dictionary mapping sources to titles
    """
    # Inefficient dictionary construction
    result = {}
    
    # Multiple string concatenations in a loop
    for citation in citations:
        source = citation.get("source", "")
        if source not in result:
            result[source] = []
        
        # Inefficient string building
        title = ""
        title = title + citation.get("title", "")
        
        # Inefficient author list building
        authors = citation.get("authors", [])
        author_str = ""
        for i, author in enumerate(authors):
            if i > 0:
                author_str = author_str + ", "
            author_str = author_str + author
        
        # Inefficient URL handling
        url = citation.get("url", "")
        if url:
            title = title + " ("
            title = title + url
            title = title + ")"
        
        result[source].append(title)
    
    return result

def calculate_factorial(n: int) -> int:
    """
    Calculate factorial using an inefficient recursive approach.
    
    Args:
        n: Number to calculate factorial for
        
    Returns:
        Factorial of n
    """
    # Inefficient recursive implementation without memoization
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

def search_knowledge_base(knowledge_base: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """
    Search the knowledge base inefficiently.
    
    Args:
        knowledge_base: The knowledge base to search
        query: Search query
        
    Returns:
        Matching items
    """
    # Inefficient search implementation
    matches = []
    
    # Create and immediately clear a dictionary
    stats = {}
    for i in range(100):
        stats[f"stat_{i}"] = i * i
    stats.clear()
    
    # Inefficient searching
    for item in knowledge_base:
        # Check if query is in the item's text
        item_text = str(item.get("text", ""))
        if query.lower() in item_text.lower():
            # Create a new dictionary instead of using the original
            match = {}
            for key, value in item.items():
                match[key] = value
            matches.append(match)
    
    return matches 
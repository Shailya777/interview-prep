"""
Implement a function that performs Min-Max Normalization on a list of integers, scaling all values according to the formula. 
Min-Max normalization helps ensure that all features contribute equally to a model by scaling them to a common range.

Example:
Input:
min_max([1, 2, 3, 4, 5])
Output:
[0.0, 0.25, 0.5, 0.75, 1.0]
"""

# Solution:
def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    minimum = min(x)
    maximum = max(x)
    range_ = maximum - minimum

    if range_ == 0:
        return [0.0] * len(x)

    return [(item - minimum) / range_ for item in x]
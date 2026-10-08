import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    sum = 0 
    for i in range(len(x)):
            product=x[i]*y[i]
            sum = sum+product
    return float(sum)
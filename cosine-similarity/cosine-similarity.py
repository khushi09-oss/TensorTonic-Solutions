import numpy as np
from math import sqrt
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    ab= 0
    for i in range(len(a)):
        product=a[i]*b[i]
        ab=ab+product
    magnitude_a=0
    for y in range(len(a)):
        product_a=a[y]*a[y]
        magnitude_a=magnitude_a+product_a

    magnitude_b=0
    for x in range(len(b)):
        product_b=b[x]*b[x]
        magnitude_b=magnitude_b+product_b
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return float(ab/(sqrt(magnitude_a)*sqrt(magnitude_b)))
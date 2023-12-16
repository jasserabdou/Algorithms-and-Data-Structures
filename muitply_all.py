def multall(arr):
    """
    Recursively multiplies all elements in a nested list.

    Args:
        arr: The nested list of elements to be multiplied.

    Returns:
        int: The product of all elements in the nested list.
    """

    product = 1
    for factor in arr:
        # Check if the element is a list, recursively call the function to compute its product.
        if isinstance(factor, list):
            product *= multall(factor)
        # If the element is not a list, multiply it directly with the current product.
        else:
            product *= factor
    return product


# Example usage: Multiply all elements in the nested list [1, 5, 6, [2, 3, [5, 4]]].
test_arr = [1, 5, 6, [2, 3, [5, 4]]]
res = multall(test_arr)
print(res) 


